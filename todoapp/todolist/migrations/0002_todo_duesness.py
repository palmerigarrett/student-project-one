# Generated by Django 3.0.8 on 2020-07-24 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='duesness',
            field=models.IntegerField(default=0),
        ),
    ]
