# Generated by Django 3.1.2 on 2020-10-27 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20201021_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]
