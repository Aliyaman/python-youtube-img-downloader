import requests

def downloader(url, file_name):
    img_data = requests.get(url).content
    with open(f'{file_name}.jpg', 'wb') as handler:
        handler.write(img_data)