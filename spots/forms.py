from django.db import models
from django import forms
from .models import Musical


class AddMusicForm(forms.ModelForm):

    album = forms.CharField(max_length=100, required=False)

    class Meta:

        model = Musical
        fields = ["title", "artist", "audio_file", "cover_image"]
