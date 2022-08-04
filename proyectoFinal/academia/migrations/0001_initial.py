# Generated by Django 4.0.5 on 2022-08-03 02:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=100)),
                ('contenido', ckeditor.fields.RichTextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='articulos')),
                ('duracion', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='profesores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('especialidad', models.CharField(max_length=40)),
                ('mail', models.EmailField(max_length=100)),
                ('educacion', models.CharField(max_length=40)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='articulos')),
            ],
        ),
    ]
