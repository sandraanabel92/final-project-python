import requests
from bs4 import BeautifulSoup #para analizar los documentos html
import pandas as pd #para manejar los Datos en el dataFrames
import sqlite3 #Importacion de sqlite3 para importacion de DB

def fetch_page(url):
    #obtenemos el contenido de una pagina
    response= requests.get(url)
    
    if response.status_code == 200:
        return response.content  #si la solucitud es exitosa devuelve el contenido de la pagina
    else:
        raise Exception(f"Failed to fetch page: {url}") 
    
def parse_product(product):
    #Analizamos los detalles de un producto
    title= product.find("a",class_="title").text.strip()
    description = product.find("p",class_="description").text.strip()
    price = product.find("h4",class_="price").text.strip()
    return{  #retornamos un diccionario con el titulo,descripcion y precio del producto
        "title": title,
        "description": description,
        "price": price,
    }

def scrape(url):
    #Funcion principal del scraping
    page_content = fetch_page(url) #obtenemos el codigo base de la pagina
    soup = BeautifulSoup(page_content, "html.parser") #Analizamos el contenido de la pagina con Beautiful Soup
   
    products = soup.find_all("div",class_="thumbnail") #Encontramos todos los elementos div con la clase "thumbnail" que representa productos
    products_data = [] #Inicializamos una lista para almacenar los datos de los productos

    for product in products:
        product_info = parse_product(product) #Analizamos cada producto encontrado
        products_data.append(product_info) #Agregamos los datos del producto a la lista
    
    return pd.DataFrame(products_data)

def save_to_db(df, db_name = 'products.db'):
    """
    Guarda un DataFrame en una base de datos SQLite.
    
    Args:
        df (DataFrame): El DataFrame de pandas que se va a guardar.
        db_name (str): El nombre del archivo de la base de datos SQLite.
    """
    conn = sqlite3.connect(db_name) #Conecta a la base de datos SQLITE (se crea si no existe)
    df.to_sql('products', conn, if_exists = 'replace', index = False) #Guarda el DataFrame en la tabla 'products'
    conn.close() #Cierra la conexión a la base de datos


def view_data_from_db(db_name = 'products.db'):
    """
    Recupera y muestra los datos de la base de datos SQLite.
    
    Args:
        db_name (str): El nombre del archivo de la base de datos SQLite.
        
    Returns:
        DataFrame: Un DataFrame de pandas con los datos de la tabla 'products'.
    """
    conn = sqlite3.connect(db_name)
    query = "SELECT * FROM products" # Consulta SQL para seleccionar todos los datos de la tabla 'products'
    df = pd.read_sql(query, conn)  # Ejecuta la consulta y carga los datos en un DataFrame de pandas
    conn.close()
    return df # Retorna el DataFrame con los datos
    

base_url = "https://webscraper.io/test-sites/e-commerce/allinone"

df = scrape(base_url) # Realiza el scraping y obtiene los datos en un DataFrame

print(df)

df.to_csv('data/raw/products.csv', index=False)

# Guarda los datos en una base de datos SQLite
save_to_db(df)

# Visualiza los datos guardados en la base de datos
print("Visualizacion de informacion de datos")
viewed_df = view_data_from_db()
print(viewed_df)

print("Data saved to CSV and SQLITE database.")

    


