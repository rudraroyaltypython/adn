# Generated by Django 5.1.2 on 2024-11-06 11:02

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Secretary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secretary_img', models.FileField(default=None, max_length=300, null=True, upload_to='secretary_img/')),
                ('Secretary_msg', tinymce.models.HTMLField()),
            ],
        ),
    ]
