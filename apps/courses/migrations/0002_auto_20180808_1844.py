# Generated by Django 2.0.8 on 2018-08-08 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='learn_time',
            new_name='learn_times',
        ),
    ]
