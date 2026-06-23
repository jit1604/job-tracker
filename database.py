from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

def get_connection():
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    return conn

