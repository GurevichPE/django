# Generated by Django 3.1.7 on 2021-05-18 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students_life', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='cource',
            new_name='course',
        ),
    ]
