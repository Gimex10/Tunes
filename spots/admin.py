from django.contrib import admin

# Register your models here.

from .models import Album, Musical

admin.site.register(Album)
admin.site.register(Musical)
