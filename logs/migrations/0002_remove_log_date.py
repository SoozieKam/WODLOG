# Generated by Django 3.2.18 on 2023-09-05 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='date',
        ),
    ]
