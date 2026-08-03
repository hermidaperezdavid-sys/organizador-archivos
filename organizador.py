# ============================================================
#  ORGANIZADOR DE ARCHIVOS — V3 (check 1: resumen final)
# ============================================================

# 'sys' nos deja leer lo que se escribe al ejecutar el script
# (lo usamos para saber qué carpeta hay que ordenar).
import sys

# 'Path' viene de pathlib y es nuestra herramienta para
# trabajar con carpetas y archivos de forma cómoda.
from pathlib import Path


# ------------------------------------------------------------
#  REGLAS DE CLASIFICACIÓN
# ------------------------------------------------------------
# Para cada carpeta de destino, la lista de extensiones que le
# corresponden. Separado de la lógica para poder añadir o quitar
# tipos sin tocar nada más. (Extensiones en minúsculas y con punto.)
CATEGORIAS = {
    "Imágenes":     [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg"],
    "Documentos":   [".pdf", ".doc", ".docx", ".txt", ".odt", ".xlsx", ".pptx"],
    "Instaladores": [".exe", ".msi", ".dmg", ".pkg", ".deb"],
    "Comprimidos":  [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Música":       [".mp3", ".wav", ".flac", ".ogg"],
    "Vídeos":       [".mp4", ".mkv", ".avi", ".mov"],
}

# Carpeta comodín: para extensiones que no aparecen en ninguna lista.
CARPETA_OTROS = "Otros"


# ------------------------------------------------------------
#  FUNCIÓN: ¿a qué carpeta va este archivo?
# ------------------------------------------------------------
def categoria_de(archivo):
    # archivo.suffix es la extensión (p.ej. ".JPG").
    # .lower() la pasa a minúsculas para que ".JPG" y ".jpg"
    # se traten igual.
    extension = archivo.suffix.lower()

    # Buscamos en qué lista encaja la extensión.
    for nombre_categoria, extensiones in CATEGORIAS.items():
        if extension in extensiones:
            return nombre_categoria

    # Si no encaja en ninguna, va a "Otros".
    return CARPETA_OTROS


# ------------------------------------------------------------
#  FUNCIÓN: buscar un nombre que no esté ocupado (V2 · check 3)
# ------------------------------------------------------------
# IMPORTANTE: esta función va DEFINIDA AQUÍ ARRIBA, antes de
# organizar(), porque organizar() la usa. Python lee de arriba
# abajo: hay que definir una función antes de llamarla.
def ruta_libre(carpeta_destino, nombre):
    # 'nombre' es algo como "informe.pdf".
    candidato = carpeta_destino / nombre

    # Si no hay nada con ese nombre, lo devolvemos tal cual.
    if not candidato.exists():
        return candidato

    # Si ya existe, separamos nombre y extensión:
    #   .stem   -> "informe"   .suffix -> ".pdf"
    tronco = candidato.stem
    extension = candidato.suffix

    # Probamos "informe (1).pdf", "informe (2).pdf"... hasta uno libre.
    contador = 1
    while True:
        nuevo_nombre = f"{tronco} ({contador}){extension}"
        candidato = carpeta_destino / nuevo_nombre
        if not candidato.exists():
            return candidato
        contador += 1


# ------------------------------------------------------------
#  FUNCIÓN PRINCIPAL: ordenar la carpeta
# ------------------------------------------------------------
def organizar(carpeta):
    # Convertimos el texto de la ruta en un objeto Path.
    carpeta = Path(carpeta)

    # Red de seguridad: si no es una carpeta real, avisamos y salimos.
    if not carpeta.is_dir():
        print(f"❌ La carpeta '{carpeta}' no existe o no es una carpeta.")
        return

    print(f"📂 Organizando: {carpeta.resolve()}\n")

    # Primero la lista de archivos, luego los movemos (no se modifica
    # la carpeta mientras se recorre). Solo archivos, no subcarpetas.
    archivos = [elemento for elemento in carpeta.iterdir() if elemento.is_file()]

    # 🆕 V3 · CHECK 1: contador por categoría. Vacío y FUERA del bucle
    # (si estuviera dentro, se reiniciaría en cada vuelta).
    conteo = {}

    for archivo in archivos:
        # 1) Categoría del archivo.
        categoria = categoria_de(archivo)

        # 2) Subcarpeta de destino (el "/" une rutas).
        destino = carpeta / categoria

        # 3) Creamos la subcarpeta (exist_ok: no falla si ya existía).
        destino.mkdir(parents=True, exist_ok=True)

        # 4) Pedimos una ruta libre y movemos ahí (sin pisar nada).
        destino_final = ruta_libre(destino, archivo.name)
        archivo.rename(destino_final)

        # 5) 🆕 Sumamos 1 a esta categoría.
        #    .get(categoria, 0) devuelve lo que haya, o 0 si es la
        #    primera vez (así no da error al no existir aún la clave).
        conteo[categoria] = conteo.get(categoria, 0) + 1

        # Mostramos el nombre final (cambia solo si hubo que renombrar).
        print(f"  → {archivo.name}  ➜  {categoria}/{destino_final.name}")

    # ----------------------------------------------------------
    #  🆕 V3 · CHECK 1: resumen final
    # ----------------------------------------------------------
    # Total = suma de todos los valores del diccionario.
    total = sum(conteo.values())

    # Caso especial: carpeta vacía, para no mostrar un resumen feo.
    if total == 0:
        print("\n✅ Listo. No había archivos que mover.")
        return

    # Montamos ["3 Imágenes", "2 Documentos", ...] y lo unimos con comas.
    partes = [f"{cantidad} {categoria}" for categoria, cantidad in conteo.items()]
    resumen = ", ".join(partes)

    print(f"\n✅ Listo. {total} archivos movidos: {resumen}")


# ------------------------------------------------------------
#  PUNTO DE ARRANQUE DEL PROGRAMA (siempre al final del archivo)
# ------------------------------------------------------------
if __name__ == "__main__":
    # La carpeta se indica al ejecutar (V2 · check 1):
    #   python organizador.py Descargas
    # Si no se indica nada, usamos "carpeta_prueba".
    if len(sys.argv) > 1:
        carpeta_a_ordenar = sys.argv[1]
    else:
        carpeta_a_ordenar = "carpeta_prueba"

    organizar(carpeta_a_ordenar)