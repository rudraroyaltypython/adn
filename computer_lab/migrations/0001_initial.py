# Generated by Django 5.1.2 on 2024-11-15 09:21

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerLab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(max_length=50)),
                ('sub_title', models.CharField(max_length=150)),
                ('text_content', tinymce.models.HTMLField()),
                ('image1', models.ImageField(blank=True, null=True, upload_to='ComputerLab/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='ComputerLab/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='ComputerLab/')),
            ],
        ),
    ]