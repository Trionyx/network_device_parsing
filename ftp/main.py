import requests
import ftplib
from io import BytesIO

from PIL import Image
from dotenv import load_dotenv


def image_upload(img_urls: list) -> None:
    ftp = ftplib.FTP('ftp.example.com')
    ftp.login('username', 'password')

    ftp.cwd('/www/docrec.ru/itpict')

    for url in img_urls:
        response = requests.get(url)

        # catalogue item index as name
        filename = 'temp/temp_image.jpg'

        with open(filename, 'wb') as f:
            im = Image.open(BytesIO(response.content))
            im.save(f, 'JPEG')

        with open(filename, 'rb') as file:
            ftp.storbinary('STOR %s' % filename, file)

    ftp.quit()
    print('Image uploaded')


def save_images_to_ftp(image_urls: list) -> None:
    """
    Take image url and save it to FTP
    :param image_urls: list with image urls
    :return: None
    """
    response = requests.get(image_urls)

    with open('image.jpg', 'wb') as f:
        im = Image.open(BytesIO(response.content))
        im.save(f, 'JPEG')
