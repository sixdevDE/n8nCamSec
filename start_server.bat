@echo off
cd /d "%~dp0"

REM Prüfen ob venv existiert
IF NOT EXIST "venv\Scripts\activate.bat" (
    echo [INFO] Erstelle virtuelle Umgebung...
    python -m venv venv
)

REM Aktivieren
call venv\Scripts\activate.bat

REM Pakete installieren
echo [INFO] Installiere erforderliche Pakete...
pip install --upgrade pip
pip install fastapi uvicorn mediapipe opencv-python numpy

REM Server starten
echo [INFO] Starte Server...
uvicorn lumin_vision_server:app --reload

pause
