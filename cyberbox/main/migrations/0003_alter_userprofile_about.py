# Generated by Django 3.2 on 2021-04-29 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210429_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='about',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
