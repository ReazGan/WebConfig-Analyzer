@echo off
title REAZGAN - Web Analyzer

echo. Created by ReazGan

set /p target_url="Lutfen taranacak URL'yi girin (ornek: http://example.com): "
set /p output_file="Rapor hangi dosyaya kaydedilsin? (ornek: rapor.json): "

echo.
echo Taranan Hedef: %target_url%
echo Rapor Dosyasi: %output_file%
echo --------------------------------------------------
echo.

python analyzer.py %target_url% -o %output_file%

echo.
echo --------------------------------------------------
echo Tarama tamamlandi. Kapatmak icin bir tusa basin.
pause > nul