# Generated by Django 4.2.6 on 2023-11-29 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internpedia', '0013_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.CharField(default='review', max_length=200),
            preserve_default=False,
        ),
    ]