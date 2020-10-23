import os
from io import BytesIO

from PIL import Image
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.files import File

from birthday.settings import MEDIA_ROOT

storage = FileSystemStorage(location=MEDIA_ROOT)


class Post(models.Model):
    author = models.CharField(max_length=100, verbose_name='Автор')
    message = models.TextField(verbose_name='Текст поздравления')
    photo = models.ImageField(upload_to='photos/', verbose_name='Картинка', storage=storage)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


class Photo(models.Model):
    message = models.TextField(verbose_name='Текс')
    photo = models.ImageField(upload_to='photos/', verbose_name='Картинка',
                              storage=storage)
    width = models.PositiveIntegerField(verbose_name='Ширина')
    height = models.PositiveIntegerField(verbose_name='Высота')

    @classmethod
    def create_all(cls):
        path = os.path.join(settings.STATIC_ROOT, 'files', 'tanya')
        obj = []
        files = os.listdir(path)
        for f in files:
            with Image.open(os.path.join(path, f)) as img:
                width, height = img.size
                image_file = BytesIO()
                img.save(image_file, img.format)
                obj.append(cls(
                    width=width,
                    height=height,
                    photo=File(image_file, name=f))
                )
        cls.objects.bulk_create(obj)

    @property
    def size(self):
        return f'{self.width}x{self.height}'
