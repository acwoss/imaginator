import requests
import tempfile

from PIL import Image
from pathlib import Path


def fetch(url):
    response = requests.get(url)
    if response.ok:
        return response.content


def download(url, destination, name):
    temp = tempfile.TemporaryFile()
    response = fetch(url)
    temp.write(response)
    image = Image.open(temp)
    image.save(f'{destination}/{name}')


def zipdir(path, ziph):
    for file in Path(path).glob('**/*.png'):
        ziph.write(file, file.name)
