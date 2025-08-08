## 🇬🇧 English

A lightweight and fast Python tool designed to quickly detect common security misconfigurations and sensitive data exposures on web servers.

### ✨ Features

This tool performs the following checks:

-   **🕵️‍♂️ Information Disclosure:** Detects HTTP headers that leak sensitive information, such as `Server` version and `X-Powered-By` technology.
-   **🛡️ Missing Security Headers:** Reports the absence of critical security headers like `Content-Security-Policy`, `Strict-Transport-Security` (HSTS), etc.
-   **📂 Sensitive File Scanning:** Scans for dangerously exposed files and directories, such as `.env`, `.git`, `wp-config.php`, etc.
-   **⚡ Fast Scans:** Utilizes multithreading (`ThreadPool`) to scan for multiple files concurrently, significantly speeding up the process.
-   **📄 JSON Reporting:** Provides an option to save all findings into a structured JSON file for later analysis or record-keeping.

### 🚀 Installation & Usage

**1. Clone the Repository:**
```bash
# Replace 'WebConfig-Analyzer' with your repository name
git clone [https://github.com/ReazGan/WebConfig-Analyzer.git](https://github.com/ReazGan/WebConfig-Analyzer.git)
cd WebConfig-Analyzer
2. Install Dependencies:

Bash

pip install -r requirements.txt
(Note: To create the requirements.txt file, run this command in your project folder: pip freeze > requirements.txt)

3. Run the Analyzer:

Using Python:

Bash

# For a quick scan displayed in the console
python analyzer.py [http://example.com](http://example.com)

# To scan and save the report as a JSON file
python analyzer.py [http://example.com](http://example.com) -o report.json
Using Batch Scripts (for Windows users):
Simply double-click the .bat files in the project directory.

scan.bat: Prompts for a URL and performs a quick scan.

scan_and_save.bat: Prompts for a URL and a filename, then saves the report.



🇹🇷 Türkçe
Web sunucularındaki yaygın güvenlik yapılandırma hatalarını ve hassas veri sızıntılarını hızla tespit etmek için tasarlanmış hafif ve hızlı bir Python aracı.

✨ Özellikler
Bu araç aşağıdaki kontrolleri gerçekleştirir:

🕵️‍♂️ Bilgi Sızıntısı Tespiti: Sunucu versiyonu (Server) ve kullanılan teknoloji (X-Powered-By) gibi bilgileri sızdıran HTTP başlıklarını bulur.

🛡️ Eksik Güvenlik Başlıkları: Content-Security-Policy, HSTS gibi kritik güvenlik başlıklarının eksikliğini raporlar.

📂 Hassas Dosya Taraması: Yanlışlıkla herkese açık bırakılmış .env, .git, wp-config.php gibi tehlikeli dosyaları ve yolları tespit eder.

⚡ Hızlı Tarama: ThreadPool kullanarak çok sayıda dosyayı eş zamanlı olarak tarar ve süreci ciddi şekilde hızlandırır.

📄 JSON Raporlama: Tüm bulguları detaylı bir JSON dosyasına kaydederek analiz ve arşivleme imkanı sunar.

🚀 Kurulum ve Kullanım
1. Projeyi Klonlayın:

Bash

# 'WebConfig-Analyzer' kısmını kendi repo adınızla değiştirin
git clone [https://github.com/ReazGan/WebConfig-Analyzer.git](https://github.com/ReazGan/WebConfig-Analyzer.git)
cd WebConfig-Analyzer
2. Gerekli Kütüphaneleri Yükleyin:

Bash

pip install -r requirements.txt
(Not: requirements.txt dosyasını oluşturmak için proje klasöründe şu komutu çalıştırın: pip freeze > requirements.txt)

3. Tarayıcıyı Çalıştırın:

Python ile:

Bash

# Konsolda hızlı bir tarama için
python analyzer.py [http://hedefsite.com](http://hedefsite.com)

# Tarayıp sonucu JSON dosyasına kaydetmek için
python analyzer.py [http://hedefsite.com](http://hedefsite.com) -o rapor.json
Batch Scriptleri ile (Windows kullanıcıları için):
Proje klasöründeki .bat dosyalarına çift tıklamanız yeterlidir.

scan.bat: URL sorar ve hızlı bir tarama yapar.

scan_and_save.bat: URL ve dosya adı sorar, ardından raporu kaydeder.
