# Generated by Django 2.2.10 on 2021-08-09 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0009_auto_20210806_1346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='session_id',
            new_name='user_id',
        ),
    ]
