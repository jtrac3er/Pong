
@echo off


where /q pip
if errorlevel 1 (echo pip ist nicht im Pfad vorhanden. Bitte hinzufuegen & pause & exit)


pip install pygame
pip install numpy
:: unnötig, aber zur Sicherheit

pip install tkinter


echo Abhaengigkeiten wurden installiert
pause
exit