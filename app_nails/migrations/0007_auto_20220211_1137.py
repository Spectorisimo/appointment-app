# Generated by Django 3.2.11 on 2022-02-11 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_nails', '0006_auto_20220211_1134'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'Запись', 'verbose_name_plural': 'Записи'},
        ),
        migrations.AlterModelOptions(
            name='pickdate',
            options={'verbose_name': 'Доступная дата', 'verbose_name_plural': 'Доступные даты'},
        ),
    ]
