# Generated by Django 4.2.7 on 2023-12-20 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_mobiledetails_stack_alter_mobiledetails_storage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mobiledetails',
            name='trending',
        ),
    ]
