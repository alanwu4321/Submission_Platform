# Generated by Django 2.1.1 on 2018-11-21 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20181121_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='Due_date',
            field=models.DateField(default=''),
            preserve_default=False,
        ),
    ]