import tkinter as tk
from tkinter import ttk
import sqlite3

def mostrar_app():
    def cargar_datos(ciudad):
        for row in tree.get_children():
            tree.delete(row)
        conn = sqlite3.connect("data/clima.db")
        c = conn.cursor()
        c.execute("SELECT * FROM clima WHERE ciudad=?", (ciudad,))
        for row in c.fetchall():
            tree.insert("", tk.END, values=row)
        conn.close()

    root = tk.Tk()
    root.title("Clima - Próximos 7 días")
    root.geometry("700x400")

    label = ttk.Label(root, text="Seleccione una ciudad:", font=("Arial", 14))
    label.pack(pady=10)

    ciudad_var = tk.StringVar(value="Madrid")
    ciudades = [
        "Madrid", "Sevilla", "Barcelona",
        "Cordoba", "Lugo", "Toledo",
        "Leon", "Soria", "Zaragoza", "Palencia"
    ]
    combo = ttk.Combobox(root, textvariable=ciudad_var, values=ciudades)
    combo.pack()
    combo.bind("<<ComboboxSelected>>", lambda e: cargar_datos(ciudad_var.get()))

    columns = ("ciudad", "fecha", "temp_max", "temp_min", "descripcion")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col.capitalize())
    tree.pack(expand=True, fill="both", pady=10)

    # Pongo por defecto la ciudad madrid para que aparezcan datos al inicar el programa
    cargar_datos("Madrid")

    root.mainloop()