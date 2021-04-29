from django.db import models


'''
Models:


User
-------------------
username
email
password
avatar
about
github
linkedin

programming_languages = ManyToMany(ProgrammingLanguages)

projects = ManyToMany(Project)

working_place = ForeignKey()
===================


WorkingPlace
-------------------


===================

#projects app
Project
-------------------
title
description
languages
image
date

full = Booleanfield(default=True)


working_place in projects = ManyToMany(User)
users = ManyToMany(User)

===================
'''


class ProgrammingLanguages(models.Model):
    title = models.CharField(max_length=80)
    desc = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "ProgrammingLanguage"
        verbose_name_plural = "ProgrammingLanguages"
        ordering = ['-title']




