from pathlib import Path
import shutil

carpeta = Path("carpeta_prueba")

reglas = {
    ".jpg": "Imagenes",
    ".png": "Imagenes",
    ".pdf": "Documentos",
    ".docx": "Documentos",
    ".exe": "Instaladores",
    ".msi": "Instaladores",
}

for archivo in carpeta.iterdir():
    if archivo.is_dir():                     # nos saltamos las carpetas
        continue
    extension = archivo.suffix.lower()
    destino = reglas.get(extension, "Otros")
    carpeta_destino = carpeta / destino
    carpeta_destino.mkdir(exist_ok=True)     # crea la carpeta destino si no existe
    shutil.move(archivo, carpeta_destino / archivo.name)
    print(archivo.name, "->", destino)