# Generated by Django 5.0 on 2023-12-21 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='investment',
            new_name='inventory',
        ),
    ]
