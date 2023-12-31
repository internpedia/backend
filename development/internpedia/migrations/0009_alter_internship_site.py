# Generated by Django 4.2.6 on 2023-10-12 05:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "internpedia",
            "0008_company_website_internship_location_internship_paid_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="internship",
            name="site",
            field=models.TextField(
                choices=[
                    ("On-Site", "On Site"),
                    ("Remote", "Remote"),
                    ("Hybrid", "Hybrid"),
                ]
            ),
        ),
    ]
