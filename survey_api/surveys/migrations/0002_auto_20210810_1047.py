# Generated by Django 2.2.10 on 2021-08-10 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Response',
            new_name='SurveyResponse',
        ),
    ]