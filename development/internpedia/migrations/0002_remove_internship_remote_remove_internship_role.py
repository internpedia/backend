# Generated by Django 4.2.6 on 2023-10-05 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internpedia', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internship',
            name='remote',
        ),
        migrations.RemoveField(
            model_name='internship',
            name='role',
        ),
    ]
