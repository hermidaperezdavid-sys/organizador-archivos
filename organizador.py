# ============================================================
#  ORGANIZADOR DE ARCHIVOS — V2 (hasta el check 2)
# ============================================================

# 'sys' nos deja leer lo que se escribe al ejecutar el script
# (lo usaremos para saber qué carpeta hay que ordenar).
import sys

# 'Path' viene de pathlib y es nuestra herramienta para
# trabajar con carpetas y archivos de forma cómoda.
from pathlib import Path


# ------------------------------------------------------------
#  REGLAS DE CLASIFICACIÓN
# ------------------------------------------------------------
# Un diccionario donde, para cada carpeta de destino,
# guardamos la lista de extensiones que le corresponden.
# Lo tenemos aquí arriba y separado del resto para que
# añadir o quitar tipos sea fácil, sin tocar la lógica.
# (Las extensiones van en minúsculas y con el punto delante.)
CATEGORIAS = {
    "Imágenes":     [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg"],
    "Documentos":   [".pdf", ".doc", ".docx", ".txt", ".odt", ".xlsx", ".pptx"],
    "Instaladores": [".exe", ".msi", ".dmg", ".pkg", ".deb"],
    "Comprimidos":  [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Música":       [".mp3", ".wav", ".flac", ".ogg"],
    "Vídeos":       [".mp4", ".mkv", ".avi", ".mov"],
}

# Carpeta comodín: aquí van los archivos cuya extensión
# no aparece en ninguna de las listas de arriba.
CARPETA_OTROS = "Otros"


# ------------------------------------------------------------
#  FUNCIÓN: ¿a qué carpeta va este archivo?
# ------------------------------------------------------------
def categoria_de(archivo):
    # archivo.suffix es la extensión (por ejemplo ".JPG").
    # Le ponemos .lower() para pasarla a minúsculas, así
    # ".JPG" y ".jpg" se tratan igual y no se nos escapa nada.
    extension = archivo.suffix.lower()

    # Recorremos las categorías buscando en qué lista encaja.
    for nombre_categoria, extensiones in CATEGORIAS.items():
        if extension in extensiones:
            return nombre_categoria  # la encontramos: devolvemos su nombre

    # Si el bucle termina sin encontrar nada, va a "Otros".
    return CARPETA_OTROS


# ------------------------------------------------------------
#  FUNCIÓN PRINCIPAL: ordenar la carpeta
# ------------------------------------------------------------
def organizar(carpeta):
    # Convertimos el texto de la ruta en un objeto Path,
    # que es con lo que sabe trabajar pathlib.
    carpeta = Path(carpeta)

    # Red de seguridad: si eso no es una carpeta real,
    # avisamos y salimos sin hacer nada más.
    if not carpeta.is_dir():
        print(f"❌ La carpeta '{carpeta}' no existe o no es una carpeta.")
        return

    print(f"📂 Organizando: {carpeta.resolve()}\n")

    # Hacemos PRIMERO la lista de archivos y LUEGO los movemos.
    # ¿Por qué? Porque si fuéramos leyendo y moviendo a la vez,
    # estaríamos cambiando la carpeta mientras la recorremos,
    # y eso puede dar resultados raros. Nos quedamos solo con
    # los archivos (is_file), dejando las subcarpetas en paz.
    archivos = [elemento for elemento in carpeta.iterdir() if elemento.is_file()]

    for archivo in archivos:
        # 1) Averiguamos su categoría con la función de arriba.
        categoria = categoria_de(archivo)

        # 2) Construimos la ruta de la subcarpeta de destino.
        #    El operador "/" une rutas: carpeta / "Imágenes".
        destino = carpeta / categoria

        # 3) *** ESTE ES EL CHECK 2 ***
        #    Creamos la subcarpeta de destino.
        #      exist_ok=True  -> si YA existía (de otra ejecución),
        #                        no da error; simplemente sigue.
        #      parents=True   -> crea carpetas intermedias si hicieran falta.
        destino.mkdir(parents=True, exist_ok=True)

        # 4) Movemos el archivo dentro de su subcarpeta.
        #    (Si en el destino ya hubiera un archivo con el mismo
        #     nombre, esto podría dar problemas: eso lo arreglará
        #     el check 3, aún no lo tocamos.)
        archivo.rename(destino / archivo.name)

      # AHORA (check 3): primero pedimos una ruta libre en el destino,
        # y movemos ahí. Así nunca pisamos un archivo que ya existía.
        destino_final = ruta_libre(destino, archivo.name)
        archivo.rename(destino_final)

        # Mostramos el nombre CON el que ha quedado guardado
        # (será distinto solo si hubo que renombrarlo).
        print(f"  → {archivo.name}  ➜  {categoria}/{destino_final.name}")
    print("\n✅ Listo.")


# ------------------------------------------------------------
#  PUNTO DE ARRANQUE DEL PROGRAMA
# ------------------------------------------------------------
# Esto solo se ejecuta cuando lanzas el script directamente.
if __name__ == "__main__":

    # *** CHECK 1 ***: la carpeta se indica al ejecutar.
    # Al escribir  python organizador.py Descargas
    # Python guarda las palabras en sys.argv:
    #   sys.argv = ["organizador.py", "Descargas"]
    # Si hay algo detrás del nombre del script, lo usamos;
    # si no, tiramos de "carpeta_prueba" por defecto.
    if len(sys.argv) > 1:
        carpeta_a_ordenar = sys.argv[1]
    else:
        carpeta_a_ordenar = "carpeta_prueba"

    # Y arrancamos.
    organizar(carpeta_a_ordenar)
    # ------------------------------------------------------------
#  FUNCIÓN: buscar un nombre que no esté ocupado (CHECK 3)
# ------------------------------------------------------------
def ruta_libre(carpeta_destino, nombre):
    # 'nombre' es algo como "informe.pdf".
    # Construimos la ruta candidata: destino / "informe.pdf".
    candidato = carpeta_destino / nombre

    # Si ahí no hay nada con ese nombre, genial: lo devolvemos tal cual.
    if not candidato.exists():
        return candidato

    # Si YA existe, separamos el nombre en dos trozos:
    #   .stem   -> "informe"  (nombre sin la extensión)
    #   .suffix -> ".pdf"     (la extensión)
    tronco = candidato.stem
    extension = candidato.suffix

    # Vamos probando "informe (1).pdf", "informe (2).pdf"...
    # hasta encontrar uno que NO exista.
    contador = 1
    while True:
        nuevo_nombre = f"{tronco} ({contador}){extension}"
        candidato = carpeta_destino / nuevo_nombre
        if not candidato.exists():
            return candidato   # este está libre: lo devolvemos
        contador += 1          # ocupado también: probamos el siguiente número