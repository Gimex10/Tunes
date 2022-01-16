from django.db import models

from spots.helpers import get_audio_length
from spots.validators import validate_is_audio

# Create your models here.


class Album(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name



class Musical(models.Model):
    title = models.CharField(max_length=100, null=True)
    artist = models.CharField(max_length=100, null=True)
    album = models.ForeignKey(Album, null=True, blank=True, on_delete=models.SET_NULL)
    time_length = models.DecimalField(
        null=True, blank=True, max_digits=20, decimal_places=2)
    audio_file = models.FileField(upload_to="spots", null=True, validators=[validate_is_audio])
    cover_image = models.ImageField(
        upload_to="spots_image", null=True, blank=True)

    def save(self, *args, **kwargs):

        if not self.time_length:

            audio_length = get_audio_length(self.audio_file)
            self.time_length = audio_length

        return super().save(*args, **kwargs)
