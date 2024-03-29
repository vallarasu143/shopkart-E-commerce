# Generated by Django 4.2.7 on 2023-11-29 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_product_items_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_qty', models.IntegerField(null=True)),
                ('product_amount', models.IntegerField(null=True)),
                ('shipping_address', models.TextField()),
                ('payment_option', models.TextField()),
                ('product_items_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product_items')),
            ],
            options={
                'db_table': 'product_order',
            },
        ),
    ]
