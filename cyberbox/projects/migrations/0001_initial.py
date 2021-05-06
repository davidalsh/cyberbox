# Generated by Django 3.2 on 2021-05-04 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0003_alter_userprofile_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('max_members', models.PositiveIntegerField()),
                ('full', models.BooleanField(default=False)),
                ('programming_languages_are_using', models.ManyToManyField(to='main.ProgrammingLanguages')),
                ('searching_for_working_place', models.ManyToManyField(to='main.WorkingPlace')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'ordering': ['-created_at'],
            },
        ),
    ]