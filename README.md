# Sistema de Recomendación Basado en Contenido

Este programa implementa un **modelo de recomendación basado en contenido (Content-Based Filtering)**, utilizando un conjunto de documentos de texto para calcular la **relevancia semántica** entre ellos a partir de medidas como **TF**, **IDF** y **TF-IDF**.

El sistema permite analizar documentos, eliminar palabras irrelevantes (*stop words*), aplicar **lematización**, y construir tablas de ponderaciones para cada documento.
Su objetivo es identificar qué documentos comparten más contenido o temas en común.

---

## Estructura del proyecto

```
.
├── data/                        # Datos y ejemplos
│   ├── corpus/                  # Corpus en distintos idiomas (JSON)
│   ├── examples-documents/      # Documentos de ejemplo
│   │   ├── new-documents/       # Nuevos documentos para probar
│   │   └── original-documents/  # Documentos base originales
│   └── stop-words/              # Ficheros de stop words en distintos idiomas
├── docs/                        # Documentación y enunciado del proyecto
├── pyproject.toml               # Configuración del proyecto y dependencias
├── README.md
├── src/                         # Código fuente
│   ├── main.py                  # Punto de entrada principal
│   ├── cli.py                   # Parser de argumentos CLI
│   ├── etl.py                   # Pipeline ETL: lectura, limpieza y lematización
│   ├── output.py                # Funciones de salida y visualización de resultados
│   ├── statistics_functions.py  # Cálculos de TF, IDF, TF-IDF y normalización
│   └── content_based_filtering_model/
│       └── __init__.py
└── uv.lock                      # Archivo de lock de uv
```

---

## Requisitos previos

* Python **3.12+**
* Git (opcional)
* Conexión a Internet para instalar dependencias

---

## Instalación y despliegue con uv

1. Clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd content-based-filtering-model
```

2. Instalar **uv** si no está instalado:

### Usando los instaladores oficiales

**macOS / Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Usando PyPI o pipx

**Con pip:**

```bash
pip install uv
```

**Con pipx:**

```bash
pipx install uv
```

> Para actualizar `uv` a la última versión:
>
> ```bash
> uv self update
> ```

3. Sincronizar dependencias y crear el entorno virtual:

```bash
uv sync
uv sync --group dev   # opcional, instala herramientas de desarrollo
```

> Esto creará un entorno virtual `.venv` e instalará las dependencias declaradas en `pyproject.toml`.

---

## Ejemplo de ejecución

Usando el entrypoint definido en `pyproject.toml`:

```bash
uv run content-based-filtering -d data/examples-documents/original-documents/*.txt -s data/stop-words/stop-words-es.txt -l data/corpus/corpus-es.json
```

O ejecutando directamente el script principal:

```bash
uv run src/main.py -d data/examples-documents/original-documents/*.txt -s data/stop-words/stop-words-es.txt -l data/corpus/corpus-es.json
```

---

## Opciones de ejecución

```bash
usage: main.py [-h] -d DOCUMENTS [DOCUMENTS ...] -s STOPWORDS -l LEMMATIZATION
```

* `-h` o `--help`: Muestra la ayuda del programa
* `-d DOCUMENTS` o `--documents DOCUMENTS`:
  Directorio o lista de ficheros `.txt` a analizar
  Ejemplo: `-d data/examples-documents/original-documents/*.txt`
* `-s STOPWORDS` o `--stopwords STOPWORDS`:
  Fichero con las palabras vacías (*stop words*) a eliminar
* `-l LEMMATIZATION` o `--lemmatization LEMMATIZATION`:
  Fichero con las reglas de lematización

---

## Breve descripción de los scripts

* `main.py`: Punto de entrada del sistema. Orquesta la lectura, preprocesamiento y cálculo de las métricas.
* `cli.py`: Define y parsea los argumentos de línea de comandos.
* `etl.py`: Encargado del pipeline ETL (Extract, Transform, Load) que limpia y lematiza los textos.
* `statistics_functions.py`: Contiene el cálculo de **TF**, **log(TF)**, **IDF**, **TF-IDF** y normalización de vectores.
* `output.py`: Genera tablas con `tabulate` para visualizar los resultados de cada documento.

---

## Ejemplo de salida

Para cada documento procesado, el sistema mostrará una tabla con las ponderaciones calculadas:

```fish
📄 document-01.txt
╒════════════════╤══════════╤══════════╤═════════════╤══════════╤══════════╕
│ WORD           │ TF       │ TF(log)  │ Normalized  │ IDF      │ TF-IDF   │
╞════════════════╪══════════╪══════════╪═════════════╪══════════╪══════════╡
│ cervantes      │ 0.0833   │ 0.3010   │ 0.2505      │ 1.2346   │ 0.1028   │
│ quijote        │ 0.1667   │ 0.4771   │ 0.3969      │ 1.0986   │ 0.1833   │
│ molino         │ 0.0833   │ 0.3010   │ 0.2505      │ 1.7918   │ 0.1572   │
╘════════════════╧══════════╧══════════╧═════════════╧══════════╧══════════╛
```

---

## Informe del proyecto

Dentro del directorio `docs/` se incluye el informe **“informe.pdf”**, que explica los fundamentos teóricos, el funcionamiento del modelo de filtrado basado en contenido y las conclusiones del análisis.
