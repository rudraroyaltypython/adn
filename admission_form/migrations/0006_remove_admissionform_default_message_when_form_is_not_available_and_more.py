# Generated by Django 5.1.2 on 2024-11-15 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission_form', '0005_rename_title_admissionform_default_message_when_form_is_not_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admissionform',
            name='default_message_when_form_is_not_available',
        ),
        migrations.AlterField(
            model_name='admissionform',
            name='pdf',
            field=models.FileField(default=3, upload_to='AdmissionForm/'),
            preserve_default=False,
        ),
    ]
