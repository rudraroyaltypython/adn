# Generated by Django 5.1.2 on 2024-11-11 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_notice', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schoolnotice',
            old_name='sub_title',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='schoolnotice',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='schoolnotice',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='schoolnotice',
            name='image3',
        ),
    ]