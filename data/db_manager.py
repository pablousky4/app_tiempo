import sqlite3
import csv
import os

def cargar_en_db():
    conn = sqlite3.connect("data/clima.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS clima (
            ciudad TEXT,
            fecha TEXT,
            temperatura_max INTEGER,
            temperatura_min INTEGER,
            descripcion TEXT
        )
    """)
    with open("data/clima.csv", newline="") as file:
        reader = csv.DictReader(file)
        rows = [(r["ciudad"], r["fecha"], r["temperatura_max"], r["temperatura_min"], r["descripcion"]) for r in reader]
        c.execute("DELETE FROM clima")
        c.executemany("INSERT INTO clima VALUES (?, ?, ?, ?, ?)", rows)
    conn.commit()
    conn.close()