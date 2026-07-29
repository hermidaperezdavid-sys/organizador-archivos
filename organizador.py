from pathlib import Path

carpeta = Path("carpeta_prueba")

# Diccionario: qué extensión va a qué carpeta
reglas = {
    ".jpg": "Imagenes",
    ".png": "Imagenes",
    ".pdf": "Documentos",
    ".docx": "Documentos",
    ".exe": "Instaladores",
    ".msi": "Instaladores",
}

for archivo in carpeta.iterdir():
    extension = archivo.suffix.lower()      # .JPG y .jpg cuentan igual
    destino = reglas.get(extension, "Otros")
    print(archivo.name, "->", destino)