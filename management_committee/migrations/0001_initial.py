# Generated by Django 5.1.2 on 2024-11-07 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManagementCommittee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=50)),
                ('committee_members_upto_1994', models.CharField(max_length=100)),
            ],
        ),
    ]
