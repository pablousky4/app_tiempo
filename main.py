from data.generador_csv import generar_csv
from data.db_manager import cargar_en_db
from ui.app import mostrar_app

if __name__ == "__main__":
    generar_csv()
    cargar_en_db()
    mostrar_app()
