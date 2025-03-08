import os

import spn_function
import requests
from PIL import Image

toponym_to_find = input()

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "8013b162-6b42-4997-9691-77b7074026e0",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)
if not response:
    exit(-1)


json_response = response.json()

toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
bounds = toponym['boundedBy']['Envelope']
delta = spn_function.count_spn(bounds)

toponym_coodrinates = toponym["Point"]["pos"]

toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
pt = 'pm2rdm'

map_params = {
    "ll": ",".join([toponym_longitude, toponym_lattitude]),
    "spn": ",".join(delta),
    "apikey": apikey,
    'pt': ",".join([toponym_longitude, toponym_lattitude]) + ',' + pt

}

map_api_server = "https://static-maps.yandex.ru/v1"
response = requests.get(map_api_server, params=map_params)
if not response:
    exit(-1)
with open('map.png', mode='wb') as output_file:
    output_file.write(response.content)
opened_image = Image.open('map.png')
opened_image.show()
os.remove('map.png')
