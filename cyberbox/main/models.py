from django.db import models
from django.contrib.auth.models import User

from django_resized import ResizedImageField


class WorkingPlace(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "WorkingPlace"
        verbose_name_plural = "WorkingPlaces"
        ordering = ['title']


class ProgrammingLanguages(models.Model):
    title = models.CharField(max_length=80)
    desc = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "ProgrammingLanguage"
        verbose_name_plural = "ProgrammingLanguages"
        ordering = ['-title']


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    programming_languages = models.ManyToManyField('ProgrammingLanguages', related_name='programming_languages',
                                                   blank=True)
    working_place = models.ForeignKey('WorkingPlace', related_name='work', on_delete=models.CASCADE,  null=True,
                                      blank=True)

    # avatar = models.ImageField(upload_to='profileavatar/%Y/%m/%d', null=True, blank=True)
    avatar = ResizedImageField(size=[230, 230], crop=['middle', 'center'], quality=99, upload_to='profileavatar/%Y/%m/%d', null=True, blank=True)

    about = models.CharField(max_length=300, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=400, null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.user.pk}'

