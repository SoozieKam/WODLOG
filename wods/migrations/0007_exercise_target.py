# Generated by Django 3.2.18 on 2023-09-05 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wods', '0006_alter_wod_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='target',
            field=models.CharField(default='target', max_length=100),
        ),
    ]