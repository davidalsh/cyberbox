# Generated by Django 3.2 on 2021-05-04 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210504_2326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='owner_projects',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='projects',
        ),
    ]
