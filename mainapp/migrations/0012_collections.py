# Generated by Django 4.2.7 on 2023-12-15 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_remove_product_order_product_items_class_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='collections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categeory', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
