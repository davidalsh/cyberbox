from django.contrib.auth.models import User
from django.db import models
from main.models import WorkingPlace, ProgrammingLanguages


class Projects(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    programming_languages_are_using = models.ManyToManyField(ProgrammingLanguages)
    searching_for_working_place = models.ManyToManyField(WorkingPlace)

    users = models.ManyToManyField(User)
    project_owner = models.ForeignKey(User, related_name='owner_p', on_delete=models.CASCADE, null=True,
                                      blank=True)
    open = models.BooleanField(default=False)
    max_members = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['-created_at']


