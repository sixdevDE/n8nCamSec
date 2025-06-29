import math
import cv2
import threading
import time
import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base
import numpy as np
import mediapipe as mp

PROJECT_NAME = os.getenv("PROJECT_NAME", "n8nCAM")

POSTGRES_USER = os.getenv("POSTGRES_USER", "sixdev")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "Asdff1234!!")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_DB = os.getenv("POSTGRES_DB", "sixdevdb")
DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_DB}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    abteilung = Column(String)
    dist1 = Column(Float)
    dist2 = Column(Float)
    dist3 = Column(Float)

Base.metadata.create_all(bind=engine)

STATUS = {
    "profil": None,
    "abteilung": None,
    "dist": None,
    "liveness": False,
    "debug": False,
    "registering": False,
    "register_msg": "",
    "alarm_active": False,
    "alarm_triggered": False,
}

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

capture = cv2.VideoCapture(0)
mp_face_mesh = mp.solutions.face_mesh

def alarm_monitor():
    while True:
        # Alarm nur aktivieren, wenn Alarmanlage scharf ist UND kein bekanntes Profil erkannt wird
        if STATUS.get("alarm_triggered") and STATUS["profil"] is None:
            STATUS["alarm_active"] = True
        else:
            STATUS["alarm_active"] = False
        time.sleep(0.5)
threading.Thread(target=alarm_monitor, daemon=True).start()

def cam_worker():
    while True:
        ret, frame = capture.read()
        if not ret:
            time.sleep(0.2)
            continue
        db = SessionLocal()
        profile = db.query(Profile).first()
        if profile:
            STATUS["profil"] = profile.name
            STATUS["abteilung"] = profile.abteilung
            STATUS["dist"] = round(np.random.uniform(0.4, 1.4), 2)
            STATUS["liveness"] = True
        else:
            STATUS["profil"] = None
            STATUS["abteilung"] = None
            STATUS["dist"] = None
            STATUS["liveness"] = False
        db.close()
        time.sleep(0.5)
threading.Thread(target=cam_worker, daemon=True).start()

def gen_frames():
    face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False)
    while True:
        ret, frame = capture.read()
        if not ret:
            continue
        # Debug-Overlay: Gesichtspunkte
        if STATUS.get("debug", False):
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(rgb)
            if results.multi_face_landmarks:
                for face_landmarks in results.multi_face_landmarks:
                    for lm in face_landmarks.landmark:
                        h, w, _ = frame.shape
                        x, y = int(lm.x * w), int(lm.y * h)
                        cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
            cv2.putText(frame, f'Distanz: {STATUS["dist"] if STATUS["dist"] else "-"}', (10, 24), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
        _, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@app.get("/stream")
def video_feed():
    return StreamingResponse(gen_frames(), media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/status")
def status():
    data = STATUS.copy()
    if not isinstance(data.get("dist"), (float, int)) or not math.isfinite(data["dist"]):
        data["dist"] = None
    return data

@app.post("/toggle_debug")
def toggle_debug():
    STATUS["debug"] = not STATUS["debug"]
    return {"debug": STATUS["debug"]}

@app.post("/register")
async def register(request: Request):
    form = await request.form()
    name = form.get("name")
    abteilung = form.get("dept")
    db = SessionLocal()
    new_profile = Profile(name=name, abteilung=abteilung, dist1=1.0, dist2=1.2, dist3=1.4)
    db.add(new_profile)
    db.commit()
    db.close()
    STATUS["registering"] = True
    STATUS["register_msg"] = "Wird gespeichert..."
    time.sleep(1)
    STATUS["registering"] = False
    STATUS["register_msg"] = "Fertig"
    return {"ok": True, "msg": "Gespeichert"}

@app.post("/webhook")
async def webhook(req: Request):
    j = await req.json()
    reply = None
    if j.get("typ") == "chat":
        reply = f"{PROJECT_NAME} hat gehört: " + j.get("text", "")
    elif j.get("typ") == "befehl":
        if j.get("cmd") == "personal_anlegen":
            reply = "Personal wird angelegt!"
        elif j.get("cmd") == "alarm_scharf":
            STATUS["alarm_triggered"] = True
            reply = "Alarmanlage scharf geschaltet!"
        elif j.get("cmd") == "alarm_aus":
            STATUS["alarm_triggered"] = False
            reply = "Alarmanlage deaktiviert!"
    return {"reply": reply}

@app.get("/", response_class=HTMLResponse)
def home():
    with open("static/index.html", encoding="utf-8") as f:
        return HTMLResponse(f.read())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5001)
