import requests
from bs4 import BeautifulSoup #para analizar los documentos html
import pandas as pd #para manejar los Datos en el dataFrames

def fetch_page(url):
    #obtenemos el contenido de una pagina
    response= requests.get(url)
    print(response)
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

base_url = "https://webscraper.io/test-sites/e-commerce/allinone"

    


