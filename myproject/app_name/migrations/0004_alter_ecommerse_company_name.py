# Generated by Django 5.1.4 on 2025-01-08 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_name', '0003_alter_ecommerse_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecommerse',
            name='company_name',
            field=models.CharField(max_length=100),
        ),
    ]