@echo off
title REAZGAN - Web Analyzer

echo. Created by ReazGan

set /p target_url="Lutfen taranacak URL'yi girin (ornek: http://example.com): "

echo.
echo Taranan Hedef: %target_url%
echo --------------------------------------------------
echo.

python analyzer.py %target_url%

echo.
echo --------------------------------------------------
echo Tarama tamamlandi. Kapatmak icin bir tusa basin.
pause > nul