from bs4 import BeautifulSoup as bs
from categorias import categorias
import requests as req
import json

while True:
    j = 0
    for i in categorias:
        print(f'{j}. {i}')
        j+=1
    print(f'{j}. Salir')
    seleccion = int(input('Digite el número de categoría que desea consultar: '))

    if seleccion == j:
        print('Saliendo...')
        break

    site = req.get(f'https://www.paginasamarillas.com.co/bogota/servicios/{categorias[seleccion]}')#cambiar por categoria seleccionada
    soup = bs(site.text, 'html.parser')

    htmlDict = soup.find(id='__NEXT_DATA__').get_text()
    servicios = json.loads(htmlDict)
    data = servicios['props']['pageProps']['results']

    print(f'\nSERVICIO DE {categorias[seleccion].upper()}\n======================')
    for item in data:
        nombre = item['name']
        ubi = item['mainAddress']['streetName']
        info = item['infoLine']
        acerca = item['infoEmpresa']
        tel = item['mainAddress']['allPhones'][0]['phoneToShow']
        print(f'- {nombre}\nDirección: {ubi}\nTeléfono: {tel}\nSobre la empresa: {info}\n{acerca}\n')
    print('======================')