# 📁 Organizador de Archivos

Un pequeño script en **Python** que recorre una carpeta y trabaja con los
archivos que hay dentro. La idea final es ordenar automáticamente los archivos
de una carpeta (por ejemplo, la de *Descargas*) en subcarpetas según su tipo:
las imágenes a un sitio, los PDFs a otro, los instaladores a otro, etc.

Es mi primer proyecto en Python, y lo estoy construyendo **por versiones**: cada
versión funciona por sí sola antes de pasar a la siguiente.

---

## 🚧 Estado del proyecto

**Versión actual: V1 — primer paso funcionando.**

Ahora mismo el script es capaz de **recorrer una carpeta y mostrar por pantalla
todos los archivos que contiene**. Este es el cimiento sobre el que se construirá
todo lo demás: antes de mover o clasificar nada, el programa tiene que ser capaz
de *ver* qué hay dentro de la carpeta.

Mover los archivos a subcarpetas según su tipo es el siguiente objetivo (ver la
sección *Hoja de ruta* más abajo).

---

## ✨ ¿Qué hace ahora mismo?

- Se conecta a una carpeta indicada en el propio código.
- Recorre uno por uno todos los elementos que hay dentro de esa carpeta.
- Muestra por pantalla la ruta de cada archivo encontrado.

De momento el script **no modifica ni mueve nada**: solo lee y muestra. Esto es
intencionado, porque permite probarlo sin ningún riesgo para los archivos.

---

## 🛠️ Tecnologías

- **Python 3**
- **[pathlib](https://docs.python.org/es/3/library/pathlib.html)** — módulo de la
  librería estándar de Python para trabajar con rutas, carpetas y archivos. Viene
  incluido con Python, no hay que instalar nada aparte.

---

## ▶️ Cómo usarlo

1. Asegúrate de tener **Python 3** instalado. Puedes comprobarlo con:

   ```bash
   python --version
   ```

2. Descarga o clona este repositorio.

3. Crea una carpeta de prueba llamada `carpeta_prueba` dentro del proyecto y mete
   dentro algunos archivos de ejemplo (unas imágenes, un PDF, lo que quieras).

4. Desde la carpeta del proyecto, ejecuta el script:

   ```bash
   python organizador.py
   ```

5. Verás en la terminal la lista de todos los archivos que hay dentro de
   `carpeta_prueba`.

> 💡 **Nota:** el script busca la carpeta `carpeta_prueba` en el mismo sitio desde
> el que lo ejecutas. Si te da un error de "carpeta no encontrada", asegúrate de
> estar situado en la carpeta del proyecto al lanzarlo.

---

## 📂 Estructura del proyecto

```
organizador-archivos/
├── organizador.py      # El script principal
├── carpeta_prueba/     # Carpeta de pruebas con archivos de ejemplo (no se sube al repo)
├── .gitignore          # Archivos y carpetas que Git debe ignorar
└── README.md           # Este archivo
```

---

## 🗺️ Hoja de ruta

El proyecto está pensado para crecer en tres versiones:

**V1 — Lo mínimo que funcione**
- [x] Recorrer una carpeta y listar sus archivos.
- [ ] Detectar la extensión de cada archivo (`.jpg`, `.pdf`, `.exe`...).
- [ ] Mover cada archivo a una subcarpeta según su tipo (Imágenes, Documentos,
  Instaladores...).

**V2 — Más útil**
- [ ] Que la carpeta a ordenar no esté fija en el código, sino que se indique al
  ejecutar el script.
- [ ] Que cree las subcarpetas automáticamente si no existen.
- [ ] Que gestione bien los archivos con nombre repetido, sin dar errores.

**V3 — Acabado profesional**
- [ ] Mostrar un resumen al terminar (ej: *"15 archivos movidos: 8 imágenes,
  5 PDFs, 2 instaladores"*).
- [ ] Guardar un registro (log) de lo que hace el programa.
- [ ] Poder configurar las reglas de clasificación en un archivo aparte.

---

## 📝 Notas

Este es un proyecto de aprendizaje. Lo hago paso a paso, entendiendo cada parte
del código antes de seguir con la siguiente. El objetivo no es solo que funcione,
sino comprender por qué funciona.
