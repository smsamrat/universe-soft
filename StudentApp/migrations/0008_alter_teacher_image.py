# Generated by Django 4.1.6 on 2023-02-14 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentApp', '0007_remove_song_artist_remove_univstudent_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='teacher'),
        ),
    ]
