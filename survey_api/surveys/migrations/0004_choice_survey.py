# Generated by Django 2.2.10 on 2021-08-05 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0003_auto_20210805_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='survey',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys.Survey'),
        ),
    ]
