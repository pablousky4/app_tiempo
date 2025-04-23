import csv
from datetime import datetime, timedelta
import os
import random

def generar_csv():
    ciudades = [
        "Madrid", "Sevilla", "Barcelona",
        "Cordoba", "Lugo", "Toledo",
        "Leon", "Soria", "Zaragoza", "Palencia"
    ]
    descripciones = ["Soleado", "Nublado", "Lluvia", "Tormenta", "Niebla"]
    hoy = datetime.now().date()
    os.makedirs("data", exist_ok=True)
    with open("data/clima.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ciudad", "fecha", "temperatura_max", "temperatura_min", "descripcion"])
        for ciudad in ciudades:
            for i in range(8):
                fecha = hoy + timedelta(days=i)
                t_min = random.randint(0, 20)
                t_max = random.randint(10, 35)
                if t_min > t_max:
                    t_min, t_max = t_max, t_min
                descripcion = random.choice(descripciones)
                writer.writerow([ciudad, fecha, t_max, t_min, descripcion])