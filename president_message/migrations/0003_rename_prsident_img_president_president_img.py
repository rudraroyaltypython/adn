# Generated by Django 5.1.2 on 2024-11-06 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('president_message', '0002_president_prsident_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='president',
            old_name='prsident_img',
            new_name='president_img',
        ),
    ]