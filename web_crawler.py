import requests
from bs4 import BeautifulSoup
from PIL import Image
import os

def download_images(url, folder):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    img_tags = soup.find_all('img')
    urls = [img['src'] for img in img_tags]
    print('hi')
    count = 0
    for i, url in enumerate(urls, start=26542):
        try:
            response = requests.get(url)
            if response.status_code == 200 and response.headers['content-type']== 'image/jpeg':
                count+=1
                with open(os.path.join(folder, f'{i}.jpg'), 'wb') as f:
                    img = Image.open(response.content)
                    img.save(f, optimize=True, quality=85)
        except:
            pass

    print(count)

url = "https://unsplash.com/s/photos/old-person-face"
folder = '/Users/adityagupta/Desktop/old_temp'
download_images(url, folder)