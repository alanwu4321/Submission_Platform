# Generated by Django 2.1.1 on 2018-11-22 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20181121_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='Project_DueDate',
        ),
    ]