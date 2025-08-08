import requests
import argparse
import json
from rich.console import Console
from urllib.parse import urljoin
from datetime import datetime
import concurrent.futures

console = Console()

# analyze_headers ve analyze_security_headers fonksiyonları aynı kaldığı için buraya eklemedim.
# Kodunda o kısımları değiştirmeden bırakabilirsin.

def analyze_headers(headers):
    console.print("\n[bold cyan][+] Bilgi Sızdıran Başlıklar[/bold cyan]")
    findings = []
    
    server_header = headers.get('Server')
    powered_by_header = headers.get('X-Powered-By')
    
    if server_header:
        message = f"Sunucu bilgisi paylaşıyor: {server_header}"
        console.print(f"  [yellow]UYARI[/yellow]: {message}")
        findings.append({"type": "leaked_header", "severity": "low", "detail": message})

    if powered_by_header:
        message = f"Teknoloji bilgisi paylaşıyor: {powered_by_header}"
        console.print(f"  [yellow]UYARI[/yellow]: {message}")
        findings.append({"type": "leaked_header", "severity": "low", "detail": message})

    if not findings:
        console.print("  [green]GÜVENLİ[/green]: Bilgi sızdıran temel başlıklar bulunamadı.")
    
    return findings

def analyze_security_headers(headers):
    console.print("\n[bold cyan][+] Eksik Güvenlik Başlıkları[/bold cyan]")
    findings = []
    
    security_headers = {
        "Strict-Transport-Security": "Tarayıcıların siteyle sadece HTTPS üzerinden iletişim kurmasını zorunlu kılar.",
        "Content-Security-Policy": "XSS gibi saldırıları önlemek için hangi kaynakların yüklenebileceğini kısıtlar.",
        "X-Frame-Options": "Sitenin başka bir site içinde `<iframe>` ile açılmasını engelleyerek 'clickjacking' saldırılarını önler.",
        "X-Content-Type-Options": "Tarayıcının dosya tiplerini 'koklamasını' (MIME-sniffing) engeller."
    }
    
    for header, desc in security_headers.items():
        if header not in headers:
            message = f"`{header}` başlığı eksik."
            console.print(f"  [yellow]UYARI[/yellow]: {message} [italic]({desc})[/italic]")
            findings.append({"type": "missing_header", "severity": "medium", "detail": message, "description": desc})
            
    if not findings:
        console.print("  [green]GÜVENLİ[/green]: Temel güvenlik başlıkları mevcut görünüyor.")
        
    return findings

def fetch_url(url):
    """Tek bir URL'yi kontrol eden yardımcı fonksiyon."""
    try:
        response = requests.get(url, timeout=3, headers={'User-Agent': 'WebConfig-Analyzer'}, stream=True, allow_redirects=False)
        if response.status_code == 200:
            return url  # Eğer dosya bulunduysa URL'yi döndür
    except requests.exceptions.RequestException:
        pass
    return None # Bulunamazsa veya hata olursa None döndür

def check_sensitive_files(url):
    console.print("\n[bold cyan][+] Hassas Dosya ve Klasör Taraması (Hızlandırıldı)[/bold cyan]")
    findings = []

    common_paths = [
        "/.git/HEAD", "/.env", "/.docker-compose.yml", "/docker-compose.yml",
        "/app/config/parameters.yml", "/wp-config.php", "/config.php",
        "/admin.php", "/phpinfo.php"
    ]
    
    # Tam URL'lerin bir listesini oluşturuyoruz
    full_urls = [urljoin(url, path) for path in common_paths]
    
    # Eş zamanlı olarak 10 işçi (thread) ile tarama yapıyoruz
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # executor.map, fetch_url fonksiyonunu her bir URL için çalıştırır
        results = executor.map(fetch_url, full_urls)
        
        for found_url in results:
            if found_url:
                message = f"Hassas dosya bulundu: {found_url}"
                console.print(f"  [bold red]KRİTİK[/bold red]: {message}")
                findings.append({"type": "sensitive_file", "severity": "high", "detail": message})

    if not findings:
        console.print("  [green]GÜVENLİ[/green]: Bilinen hassas dosyalardan hiçbiri bulunamadı.")
    
    return findings

# __main__ bloğu da aynı kaldığı için buraya eklemedim.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Web uygulamaları için temel konfigürasyon zafiyet tarayıcısı.")
    parser.add_argument("target_url", help="Analiz edilecek hedef URL (örn: http://example.com)")
    parser.add_argument("-o", "--output", help="Sonuçları kaydetmek için JSON dosyasının adı (örn: rapor.json)")
    args = parser.parse_args()
    
    target = args.target_url
    output_file = args.output
    
    all_findings = []
    
    console.print(f"[bold]Hedef: {target} için analiz başlatıldı.[/bold]")
    
    try:
        response = requests.get(target, timeout=5, headers={'User-Agent': 'WebConfig-Analyzer'})
        
        all_findings.extend(analyze_headers(response.headers))
        all_findings.extend(analyze_security_headers(response.headers))
        all_findings.extend(check_sensitive_files(target))

        if output_file:
            report = {
                "target": target,
                "scan_date": datetime.now().isoformat(),
                "summary": {
                    "total_findings": len(all_findings),
                    "high": len([f for f in all_findings if f['severity'] == 'high']),
                    "medium": len([f for f in all_findings if f['severity'] == 'medium']),
                    "low": len([f for f in all_findings if f['severity'] == 'low']),
                },
                "findings": all_findings
            }
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=4, ensure_ascii=False)
            
            console.print(f"\n[bold green]✓ Rapor başarıyla '{output_file}' dosyasına kaydedildi.[/bold green]")

    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]HATA:[/] Hedefe ulaşılamadı. URL'yi veya bağlantını kontrol et.[/bold red]")