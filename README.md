DE GERMAN

# n8nCam – Moderne Kamera- und Alarmsteuerung mit KI-Unterstützung

Willkommen zu **n8nCam** – Ihrer einfachen, dockerfähigen Kamera- und Alarm-Management-Lösung mit KI-Features für Gesichtserkennung, Profilverwaltung und Alarmsicherung.

---

## 🚀 **Features**
- **Gesichtserkennung (mit Profil-Verwaltung)**
- **Einfache Benutzeroberfläche im Browser**
- **Audio-Alarm bei unbekannten Personen (Voice + Sirene)**
- **Chat-Funktion & Sprachsteuerung**
- **Dark-/Lightmode, Debug, Live-Status**
- **Alle Daten sicher in Ihrer eigenen Postgres-Datenbank**

---

## 🛠️ **Installation & Setup**

### **Docker (empfohlen)**
1. **Repo klonen:**
   ```bash
   git clone https://github.com/sixdevDE/n8nCamSec.git
   cd n8nCam
.env anlegen (nach Muster .env_example):

bash
Kopieren
Bearbeiten
cp .env_example .env
Tragen Sie Ihre Postgres-DB-Infos & PROJECT_NAME ein.

Docker Compose starten:

bash
Kopieren
Bearbeiten
docker compose up --build
Das Frontend ist dann auf http://localhost:5001 erreichbar.

Hinweis: Standardmäßig erwartet n8nCam eine laufende externe Postgres-DB (z. B. db-Service in compose auskommentieren, siehe docker-compose.yaml).

Manuell (ohne Docker, z. B. für Windows)
Python 3.9+ und pip installieren

Virtuelle Umgebung (optional):

bash
Kopieren
Bearbeiten
python -m venv venv
venv\Scripts\activate  # Windows
Abhängigkeiten installieren:

bash
Kopieren
Bearbeiten
pip install -r requirements.txt
.env wie oben anlegen

Starten:

bash
Kopieren
Bearbeiten
python main.py
⚙️ Funktionen
Profil anlegen: Name und Abteilung eintragen, speichern → für Wiedererkennung.

Alarmanlage:

Scharfschalten über das Web-Panel.

Wird eine unbekannte Person erkannt:

Sprach-Warnung ("Achtung, Sie sind nicht berechtigt…")

Sirene

Kameraaufnahme während Alarm (Video im Container gespeichert)

Debug: Gesichtslandmarks live einblenden.

Chat & Sprachsteuerung: Eingaben per Text oder Mikrofon (nur, wenn im Browser unterstützt).

Dark/Lightmode: Über Toggle oben rechts umschaltbar.

🔒 Sicherheit & Anpassung
Alle Zugangsdaten und Projektname über .env konfigurierbar (keine Hardcodierung!)

Docker-Volumes: Für DB und Videofiles anpassen, falls extern persistiert werden soll.

Projektname: Über PROJECT_NAME in der .env steuerbar, z. B. für White-Label-Branding.

❓ FAQ / Fehlerbehebung
Kamera wird nicht gefunden: Prüfen, ob sie frei ist & nicht anderweitig genutzt wird.

Audio wird nicht abgespielt: Browser prüfen (Autoplay, Rechte), MP3s im /static-Ordner lassen.

Fehlende Abhängigkeiten:

Prüfen, ob alle Pakete aus requirements.txt installiert sind (Python, mediapipe, opencv, fastapi usw.)

Docker-Probleme:

Ports, DB-URL, ENV-Variablen prüfen. Logs per docker compose logs einsehen.

📞 Support
Offizielles Projekt: sixdev.de/n8nCam

Kontakt: moebius.games@gmail.com

Github-Issues für Fehler oder Feature-Wünsche nutzen!

Viel Spaß mit n8nCam!

yaml
Kopieren
Bearbeiten

---

## 3. **Empfohlene Kleinigkeiten (optional)**
- **requirements.txt** anlegen mit:
fastapi
uvicorn
opencv-python
mediapipe
numpy
sqlalchemy
psycopg2-binary

_____________________________________________________________________________________________

EN ENGLISH

# n8nCam

**n8nCam** is an AI-based security and vision system with integrated browser UI, voice/alarm features, face detection/recognition, and direct integration with PostgreSQL – ready to use in Docker.

- **Browser-based interface:** Clean, modern design, supports dark and light mode.
- **Face recognition:** Profiles are stored in PostgreSQL.
- **Alarm mode:** Automatically triggers audio alarms and starts video recording for unknown persons when the alarm system is armed.
- **Webhooks:** Ready to connect to n8n or other systems.
- **Runs everywhere:** Dockerized and tested on Linux & Windows (WSL recommended for Linux; native on Windows).

## Quick Start

1. **Copy `.env_example` to `.env` and fill in your credentials:**
    ```
    cp .env_example .env
    # Then edit .env and set your POSTGRES_* and PROJECT_NAME
    ```

2. **Build & run the Docker container:**
    ```
    docker-compose up --build
    ```

3. **Open your browser:**  
   Go to [http://localhost:5001](http://localhost:5001) (or your server’s IP).

4. **First Steps:**
    - Register a new face profile (see left panel).
    - Arm the alarm system via the command button.
    - If an unknown person is detected, the alarm will sound and video will be recorded.

## Features

- **Face recognition and registration**
- **Alarm system with audio alert** (`/static/alarm_voice.mp3` + `/static/alarm.mp3`)
- **Automatic video recording of intruders**
- **Live camera feed and debug overlay**
- **Full dark/light mode**
- **Data stored in PostgreSQL (external DB supported)**

## License

Commercial License – **You may use but not modify, resell, or redistribute this software.**  
See [LICENSE.txt](LICENSE.txt).

If you need additional rights, please contact the author:  
[moebius.games@gmail.com](mailto:moebius.games@gmail.com)

---

**Made by sixdev – [https://sixdev.de/n8nCam](https://sixdev.de/n8nCam)**