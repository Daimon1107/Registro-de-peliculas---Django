# Generated by Django 4.1 on 2022-08-27 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='plot',
            field=models.TextField(max_length=65),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to='posters_movie'),
        ),
    ]