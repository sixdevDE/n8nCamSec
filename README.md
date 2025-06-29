# n8nCamSec – Moderne Kamera- und Alarmsteuerung mit KI-Unterstützung

Willkommen zu **n8nCamSec** – Ihrer einfachen, dockerfähigen Kamera- und Alarm-Management-Lösung mit KI-Features für Gesichtserkennung, Profilverwaltung und Alarmsicherung.

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
   cd n8nCamSec
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

Hinweis: Standardmäßig erwartet n8nCamSec eine laufende externe Postgres-DB (z. B. db-Service in compose auskommentieren, siehe docker-compose.yaml).

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
Offizielles Projekt: sixdev.de/n8ncam

Kontakt: moebius.games@gmail.com

Github-Issues für Fehler oder Feature-Wünsche nutzen!

Viel Spaß mit n8nCamSec!

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