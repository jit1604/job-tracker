from fastapi import FastAPI
from models import JobApplication
from database import get_connection
from psycopg2.extras import RealDictCursor
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://project-launchpad-frontend.vercel.app"],
    allow_methods=["*"],
    allow_headers=["*"],
)

applications = []

@app.get("/")
def read_root():
    return {"message": "Project LaunchPad is live"}


@app.get("/applications")
def get_applications():
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM applications")
    rows = cursor.fetchall()
    conn.close()
    return rows




@app.post("/applications")
def add_application(application: JobApplication):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO applications (company, role, status, deadline, priority, notes) VALUES (%s, %s, %s, %s, %s, %s)",
        (application.company, application.role, application.status, application.deadline, application.priority, application.notes)
    )
    conn.commit()
    conn.close()
    return application

@app.delete("/applications/{id}")
def delete_application(id : int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM applications WHERE id = %s", (id,))
    conn.commit()
    conn.close()

@app.put("/applications/{id}")
def update_application(id : int, application: JobApplication):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE applications SET company = %s, role = %s, status = %s, deadline = %s, priority = %s, notes = %s WHERE id = %s", (application.company, application.role, application.status, application.deadline, application.priority, application.notes, id))
    conn.commit()
    conn.close()
    return {"message": "Application updated successfully"}

