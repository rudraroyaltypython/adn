# Generated by Django 5.1.2 on 2024-11-15 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admission_form', '0004_admissionform_title_alter_admissionform_pdf'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admissionform',
            old_name='title',
            new_name='default_message_when_form_is_not_available',
        ),
    ]