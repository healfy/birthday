from io import BytesIO
from PIL import Image

from django.forms import ModelForm
from django.conf import settings
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    def clean_photo(self):

        image_field = self.cleaned_data['photo']
        photo_new = BytesIO(image_field.read())

        image = Image.open(photo_new)

        # ImageOps compatible mode
        if image.mode not in ("L", "RGB"):
            image = image.convert("RGB")

        image.thumbnail((settings.WIDTH, settings.HEIGHT), Image.ANTIALIAS)

        image_file = BytesIO()
        image.save(image_file, 'jpeg')

        image_field.file = image_file
        return image_field
