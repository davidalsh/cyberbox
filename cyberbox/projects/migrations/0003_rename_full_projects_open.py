# Generated by Django 3.2 on 2021-05-06 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210504_2341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='full',
            new_name='open',
        ),
    ]
