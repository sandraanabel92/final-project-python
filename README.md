# Scraping Web de Productos.

Este proyecto realiza scraping de datos de productos de un sitio web, limpia y analiza los datos; los guarda en archivos CSV y en una base de datos SQLite.

## Requisitos.

- Python 3.7+
- pandas
- beautifulsoup4
- requests
- matplotlib
- time
- logging
- SQLite

## Instalacion.

Para instalar las dependencias creamos un archivo "txt" en el cual se guarda todas las dependecias para una rapida instalacion. Su metodo de uso es utilizando PIP y es con el comando siguiente.

````bash
pip install -r .\dep.txt
````

## Estructura de las carpetas.

````bash
final-project-python
|-- data/
|    |- database/
|    |    |__ products.db
|    |- raw/
|    |    |__ products.csv
|    |- processed/
|        |__ cleaned_products.csv    
|
|-- notebooks/
|    |__ exploration.ipynb
|
|-- src/
|    |- analysis/
|        |__ __init__.py
|        |__ analysis.py
|    |- decorators/
|        |__ __init__.py
|        |__ decorators.py
|    |- scraping/
|        |__ __init__.py
|        |__ scraper.py
|__ dep.txt
|__ README.md
|__ requirements.txt
````

## Ejecucion del Scraper.

Para ejecutar el scraper lo que hay que realizar lo siguiente:

````bash
python .\src\scraping\scraper.py
````

Esto nos va a generar  dos archivos dentro de la carpeta "DATA":

- Un CSV en la carpeta "RAW"  llamado "products.csv"
- Un DB en la carpeta "DATABASE" llamado "products.db"

## Ejecucion para el analisis de datos.

Para ejecutar el script para analisis de datos lo que hay que realizar es:

````bash
python .\src\analysys\analysys.py
````

Esto nos va a generar un CSV en la carpeta "PROCESSED" dentro de la carpeta "DATA" llamado "cleaned_products.csv"

#### Autora:

- Sandra Anabel Palacios Abad

- e-mail: sandraanabel21@gmail.com
