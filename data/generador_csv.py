import csv
from datetime import datetime, timedelta
import os

def generar_csv():
    ciudades = [
        "Madrid", "Sevilla", "Barcelona",
        "Cordoba", "Lugo", "Toledo",
        "Leon", "Soria", "Zaragoza", "Palencia"
    ]
    hoy = datetime.now().date()
    os.makedirs("data", exist_ok=True)
    with open("data/clima.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ciudad", "fecha", "temperatura_max", "temperatura_min", "descripcion"])
        for ciudad in ciudades:
            for i in range(8):
                fecha = hoy + timedelta(days=i)
                t_max = 20 + i
                t_min = 10 + i
                descripcion = "Soleado" if i % 2 == 0 else "Nublado"
                writer.writerow([ciudad, fecha, t_max, t_min, descripcion])