# Generated by Django 2.1.1 on 2018-11-22 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_admin_project_duedate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='group_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='notes',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.AddField(
            model_name='user',
            name='submission',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
