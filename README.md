<h1 align="center">📁 Organizador de Archivos</h1>

<p align="center">
  <em>Ordena automáticamente una carpeta moviendo cada archivo a una subcarpeta según su tipo.</em>
</p>

<p align="center">
  <img alt="Versión" src="https://img.shields.io/badge/versión-1.0-success">
  <img alt="Estado" src="https://img.shields.io/badge/estado-terminado-brightgreen">
  <img alt="Python" src="https://img.shields.io/badge/Python-3-blue?logo=python&logoColor=white">
  <img alt="Dependencias" src="https://img.shields.io/badge/dependencias-0-lightgrey">
  <img alt="Licencia" src="https://img.shields.io/badge/licencia-MIT-informational">
</p>

---

## ✨ ¿Qué hace?

Le indicas una carpeta (por ejemplo, la de **Descargas**) y el programa recorre
todos los archivos que hay dentro y los reparte en subcarpetas ordenadas por
tipo: las imágenes a `Imágenes/`, los PDF a `Documentos/`, los instaladores a
`Instaladores/`, etc.

En pocas palabras, convierte esto…

```
📂 Descargas/
├── foto_vacaciones.jpg
├── factura_marzo.pdf
├── instalador_app.exe
├── cancion.mp3
└── apuntes.txt
```

…en esto:

```
📂 Descargas/
├── 📁 Imágenes/      → foto_vacaciones.jpg
├── 📁 Documentos/    → factura_marzo.pdf, apuntes.txt
├── 📁 Instaladores/  → instalador_app.exe
└── 📁 Música/        → cancion.mp3
```

---

## 🚀 Características

| | Función |
|:--:|:--|
| 🗂️ | **Clasifica por tipo** según la extensión de cada archivo. |
| ⚙️ | **Reglas configurables** desde un archivo aparte (`categorias.json`), sin tocar el código. |
| 📌 | **Elige la carpeta al ejecutar**, o usa `carpeta_prueba` por defecto. |
| 🏗️ | **Crea las subcarpetas** automáticamente si no existen. |
| 🛡️ | **No pisa archivos**: si ya existe uno con el mismo nombre, lo guarda como `nombre (1).ext`. |
| 🧺 | **Carpeta `Otros`** para las extensiones que no encajan en ninguna categoría. |
| 📊 | **Resumen final** al terminar (ej: *"5 archivos movidos: 2 imágenes, 2 documentos, 1 música"*). |
| 📝 | **Registro (log)** de todo lo que hace, en pantalla y en `organizador.log`. |

---

## 🖥️ Ejemplo de ejecución

```text
03/08/2026 09:31:56 | INFO | 📂 Organizando: C:\Users\dhermidap\Downloads
03/08/2026 09:31:56 | INFO |   → foto_vacaciones.jpg  ➜  Imágenes/foto_vacaciones.jpg
03/08/2026 09:31:56 | INFO |   → factura_marzo.pdf    ➜  Documentos/factura_marzo.pdf
03/08/2026 09:31:56 | INFO |   → instalador_app.exe   ➜  Instaladores/instalador_app.exe
03/08/2026 09:31:56 | INFO |   → cancion.mp3          ➜  Música/cancion.mp3
03/08/2026 09:31:56 | INFO |   → apuntes.txt          ➜  Documentos/apuntes.txt
03/08/2026 09:31:56 | INFO | ✅ Listo. 5 archivos movidos: 2 Imágenes, 2 Documentos, 1 Música
```

---

## 🛠️ Tecnologías

Todo con la **librería estándar de Python**, sin instalar nada aparte:

- **[pathlib](https://docs.python.org/es/3/library/pathlib.html)** — rutas, carpetas y archivos.
- **[json](https://docs.python.org/es/3/library/json.html)** — leer las reglas de clasificación desde `categorias.json`.
- **[logging](https://docs.python.org/es/3/library/logging.html)** — el registro en pantalla y en archivo.
- **[sys](https://docs.python.org/es/3/library/sys.html)** — leer la carpeta indicada al ejecutar.

---

## 📦 Requisitos

- **Python 3** instalado. Puedes comprobarlo con:

  ```bash
  python --version
  ```

---

## ▶️ Cómo usarlo

1. **Descarga o clona** este repositorio:

   ```bash
   git clone https://github.com/tu-usuario/organizador-archivos.git
   cd organizador-archivos
   ```

2. Asegúrate de que junto a `organizador.py` está el archivo **`categorias.json`**
   (viene incluido en el repo).

3. **Ejecuta el script** indicándole la carpeta que quieres ordenar:

   ```bash
   python organizador.py "C:\Users\TuUsuario\Downloads"
   ```

   O, si no indicas ninguna carpeta, ordenará una llamada `carpeta_prueba`:

   ```bash
   python organizador.py
   ```

> ⚠️ **Pruébalo primero sin miedo.** Crea una carpeta `carpeta_prueba`, mete
> dentro archivos de ejemplo y ejecútalo sobre ella antes de lanzarlo contra tu
> carpeta de Descargas real.

> 💡 **Nota:** el script busca `categorias.json`, `organizador.log` y
> `carpeta_prueba` **desde el sitio donde lo ejecutas**. Si te da un error de
> "archivo no encontrado", asegúrate de estar situado en la carpeta del proyecto.

---

## ⚙️ Configurar las reglas de clasificación

Las categorías **no están dentro del código**: viven en `categorias.json`, para
que puedas cambiarlas sin tocar Python. Su formato es un diccionario donde cada
clave es el nombre de la carpeta de destino y su valor es la lista de extensiones
que le corresponden:

```json
{
    "Imágenes":     [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg"],
    "Documentos":   [".pdf", ".doc", ".docx", ".txt", ".odt", ".xlsx", ".pptx"],
    "Instaladores": [".exe", ".msi", ".dmg", ".pkg", ".deb"],
    "Comprimidos":  [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Música":       [".mp3", ".wav", ".flac", ".ogg"],
    "Vídeos":       [".mp4", ".mkv", ".avi", ".mov"]
}
```

**¿Quieres una categoría nueva?** Añádela y guarda. Por ejemplo, para libros
electrónicos:

```json
    "Vídeos":       [".mp4", ".mkv", ".avi", ".mov"],
    "Libros":       [".epub", ".mobi", ".azw3"]
```

Reglas del formato JSON que hay que respetar:

- ✅ Usa **comillas dobles** (`"`), nunca simples.
- ✅ **No** pongas coma después del **último** elemento.
- ✅ Las extensiones van en **minúsculas y con el punto** delante (`.pdf`).

Cualquier archivo cuya extensión no esté en ninguna lista se moverá a la carpeta
**`Otros`**.

---

## 📄 El registro (log)

Cada ejecución deja constancia en **`organizador.log`**, con fecha, hora y nivel
de cada acción. Las líneas nuevas se **añaden al final** del archivo, así que
tienes un historial completo de todas las veces que lo has usado. Si algo falla
(por ejemplo, la carpeta no existe), se registra como `ERROR`, para que salte a
la vista.

---

## 📂 Estructura del proyecto

```
organizador-archivos/
├── organizador.py      # El script principal
├── categorias.json     # Reglas de clasificación (editable)
├── carpeta_prueba/     # Carpeta de pruebas (ignorada por Git)
├── organizador.log     # Registro de actividad (ignorado por Git)
├── .gitignore          # Archivos y carpetas que Git debe ignorar
└── README.md           # Este archivo
```

---

## 🗺️ Hoja de ruta

El proyecto se construyó por versiones. **Todas completadas** ✅

<details open>
<summary><strong>V1 — Lo mínimo que funcione</strong></summary>

- [x] Recorrer una carpeta y listar sus archivos.
- [x] Detectar la extensión de cada archivo (`.jpg`, `.pdf`, `.exe`…).
- [x] Mover cada archivo a una subcarpeta según su tipo.

</details>

<details open>
<summary><strong>V2 — Más útil</strong></summary>

- [x] Indicar la carpeta a ordenar al ejecutar el script.
- [x] Crear las subcarpetas automáticamente si no existen.
- [x] Gestionar los archivos con nombre repetido sin dar errores.

</details>

<details open>
<summary><strong>V3 — Acabado profesional</strong></summary>

- [x] Mostrar un resumen al terminar.
- [x] Guardar un registro (log) de lo que hace el programa.
- [x] Configurar las reglas de clasificación en un archivo aparte.

</details>

### 🔭 Posibles mejoras futuras

Ideas para seguir aprendiendo más adelante:

- [ ] Modo "simulación" que enseñe qué movería **sin mover nada**.
- [ ] Ordenar también las subcarpetas de forma recursiva.
- [ ] Interfaz gráfica sencilla para elegir la carpeta.

---

## 📝 Sobre el proyecto

Este es mi **primer proyecto en Python**, construido paso a paso, entendiendo
cada parte del código antes de seguir con la siguiente. El objetivo no era solo
que funcionara, sino comprender **por qué** funciona.

---

<p align="center"><sub>Hecho con 🐍 y muchas ganas de aprender · Versión 1.0</sub></p>
