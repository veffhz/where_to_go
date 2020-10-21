# Generated by Django 3.1.2 on 2020-10-21 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20201021_1205'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-position'], 'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'Место', 'verbose_name_plural': 'Места'},
        ),
        migrations.AddField(
            model_name='image',
            name='position',
            field=models.PositiveIntegerField(default=0, verbose_name='Позиция'),
        ),
    ]