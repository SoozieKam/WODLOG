# Generated by Django 3.2.18 on 2023-09-04 08:22

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wods', '0005_auto_20230829_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wod',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, max_length=1000, null=True),
        ),
    ]
