from bs4 import BeautifulSoup as bs
import requests as req
import json

site = req.get('https://www.paginasamarillas.com.co')
soup = bs(site.text, 'html.parser')

htmlDict = soup.find(id='__NEXT_DATA__').get_text()
servicios = json.loads(htmlDict)
categoriasData = servicios['runtimeConfig']['SEARCH_CATEGORIES'][2]['categories']

categorias = []

print('\nCATEGORÍAS\n====================')
for item in categoriasData:
    nombre = item['name']
    categorias.append(nombre)
    #print(nombre)