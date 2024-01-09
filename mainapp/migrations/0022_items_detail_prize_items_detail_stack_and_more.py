# Generated by Django 4.2.7 on 2023-12-29 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_add_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='items_detail',
            name='prize',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='items_detail',
            name='stack',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='add_cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.items_detail'),
        ),
        migrations.DeleteModel(
            name='mobiledetails',
        ),
    ]