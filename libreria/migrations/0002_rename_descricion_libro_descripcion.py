# Generated by Django 4.2.4 on 2024-09-02 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='descricion',
            new_name='descripcion',
        ),
    ]
