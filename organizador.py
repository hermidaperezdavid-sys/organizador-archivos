# ============================================================
#  ORGANIZADOR DE ARCHIVOS
# ------------------------------------------------------------
#     [V1] Listar/mover archivos y clasificarlos por tipo.
#     [V2] Carpeta por argumento, crear subcarpetas, nombres repetidos.
#     [V3] Resumen final, registro (log) y reglas en archivo aparte.
# ============================================================

# --- IMPORTS ---
import sys                    # [V2] leer la carpeta indicada al ejecutar
import json                   # [V3] leer las reglas desde categorias.json
from pathlib import Path      # [V1] trabajar con carpetas y archivos
import logging                # [V3] registro (log) en pantalla y archivo


# ------------------------------------------------------------
#  CONSTANTES
# ------------------------------------------------------------
CARPETA_OTROS = "Otros"        # [V1] comodín para extensiones desconocidas
NOMBRE_LOG = "organizador.log" # [V3] archivo de registro


# ------------------------------------------------------------
#  FUNCIÓN: encender el registro                          [V3]
# ------------------------------------------------------------
def configurar_registro():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%d/%m/%Y %H:%M:%S",
        handlers=[
            logging.FileHandler(NOMBRE_LOG, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )


# ------------------------------------------------------------
#  FUNCIÓN: cargar las reglas desde el JSON               [V3]
# ------------------------------------------------------------
def cargar_categorias(ruta_config="categorias.json"):
    config = Path(ruta_config)

    if not config.exists():
        logging.error(f"No encuentro el archivo de reglas '{ruta_config}'.")
        return None

    with open(config, encoding="utf-8") as f:
        return json.load(f)


# ------------------------------------------------------------
#  FUNCIÓN: ¿a qué carpeta va este archivo?               [V1]
# ------------------------------------------------------------
def categoria_de(archivo, categorias):
    extension = archivo.suffix.lower()
    for nombre_categoria, extensiones in categorias.items():
        if extension in extensiones:
            return nombre_categoria
    return CARPETA_OTROS


# ------------------------------------------------------------
#  FUNCIÓN: buscar un nombre que no esté ocupado          [V2]
# ------------------------------------------------------------
def ruta_libre(carpeta_destino, nombre):
    candidato = carpeta_destino / nombre
    if not candidato.exists():
        return candidato

    tronco = candidato.stem
    extension = candidato.suffix

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
def organizar(carpeta, categorias):
    carpeta = Path(carpeta)                                   # [V1]

    if not carpeta.is_dir():                                  # [V2]
        logging.error(f"La carpeta '{carpeta}' no existe o no es una carpeta.")
        return

    logging.info(f"📂 Organizando: {carpeta.resolve()}")      # [V1]

    archivos = [elemento for elemento in carpeta.iterdir() if elemento.is_file()]  # [V1]

    conteo = {}                                              # [V3]

    for archivo in archivos:
        categoria = categoria_de(archivo, categorias)         # [V1]/[V3]
        destino = carpeta / categoria                         # [V1]
        destino.mkdir(parents=True, exist_ok=True)            # [V2]

        destino_final = ruta_libre(destino, archivo.name)     # [V2]
        archivo.rename(destino_final)                         # [V1]

        conteo[categoria] = conteo.get(categoria, 0) + 1      # [V3]

        logging.info(f"  → {archivo.name}  ➜  {categoria}/{destino_final.name}")

    total = sum(conteo.values())                             # [V3]

    if total == 0:
        logging.info("✅ Listo. No había archivos que mover.")
        return

    partes = [f"{cantidad} {categoria}" for categoria, cantidad in conteo.items()]
    resumen = ", ".join(partes)

    logging.info(f"✅ Listo. {total} archivos movidos: {resumen}")


# ------------------------------------------------------------
#  PUNTO DE ARRANQUE (siempre al final del archivo)
# ------------------------------------------------------------
if __name__ == "__main__":
    configurar_registro()                    # [V3]

    categorias = cargar_categorias()         # [V3] leer reglas del JSON
    if categorias is None:                   # [V3] sin reglas, no seguimos
        sys.exit(1)

    if len(sys.argv) > 1:                     # [V2]
        carpeta_a_ordenar = sys.argv[1]
    else:
        carpeta_a_ordenar = "carpeta_prueba"

    organizar(carpeta_a_ordenar, categorias) # [V1]/[V3]