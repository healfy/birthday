from django.core.files.storage import FileSystemStorage
from django.db import models
from django.urls import reverse


from birthday.settings import MEDIA_ROOT

storage = FileSystemStorage(location=MEDIA_ROOT)


class Post(models.Model):
    author = models.CharField(max_length=100, verbose_name='Автор')
    message = models.TextField(verbose_name='Текст поздравления')
    photo = models.ImageField(upload_to='photos/', verbose_name='Картинка', storage=storage)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
