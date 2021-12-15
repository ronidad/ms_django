from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'


    def save(self):
        super().save()

        img=Image.open(self.image.path)

        if img.height>100 or img.width>100:
            output_size=(100,100)
            img.thumbnail(output_size)
            img.save(self.image.path)

