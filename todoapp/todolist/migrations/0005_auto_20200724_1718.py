# Generated by Django 3.0.8 on 2020-07-24 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_auto_20200724_1715'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]