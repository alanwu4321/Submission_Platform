# Generated by Django 2.1.1 on 2018-11-26 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfile',
            name='User',
        ),
        migrations.AddField(
            model_name='userfile',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='app.User'),
            preserve_default=False,
        ),
    ]
