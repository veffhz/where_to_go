# Generated by Django 3.1.2 on 2020-10-27 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0014_auto_20201027_1743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='place_image',
            new_name='file',
        ),
    ]
