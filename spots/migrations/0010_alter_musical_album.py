# Generated by Django 4.0.1 on 2022-01-09 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spots', '0009_musical_audio_file_musical_cover_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musical',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='spots.album'),
        ),
    ]
