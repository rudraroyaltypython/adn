# Generated by Django 5.1.2 on 2024-11-15 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission_form', '0002_remove_document_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='AdmissionForm/')),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]