# Generated by Django 4.2.7 on 2023-11-29 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_items',
            name='product_name',
            field=models.TextField(),
        ),
    ]
