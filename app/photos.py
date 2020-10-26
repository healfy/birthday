import os
from PIL import Image
from django.conf import settings


path = os.path.join(settings.STATIC_ROOT, 'files', 'tanya')


class PhotoFactory:
    width = 0
    height = 0
    url = ''

    @classmethod
    def get_all(cls):
        photos = []
        files = os.listdir(path)
        for f in files:
            file_path = os.path.join(path, f)
            os.path.basename(file_path)
            with Image.open(os.path.join(path, f)) as img:
                width, height = img.size
                photos.append(cls(width, height, f'/static/files/tanya/{f}'))
        return photos

    def __init__(self, width, height, url):
        self.width = width
        self.height = height
        self.url = url

    @property
    def size(self):
        return f'{self.width}x{self.height}'
