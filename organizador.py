from pathlib import Path

# La carpeta que quiero ordenar (de momento, fija)
carpeta = Path("carpeta_prueba")

# Recorro cada elemento que hay dentro
for archivo in carpeta.iterdir():
    print(archivo.name, "->", archivo.suffix)