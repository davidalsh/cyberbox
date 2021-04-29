from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        verbose_name='username',
        max_length=150,
        unique=True,
    )

    date_of_birth = models.DateField()

    programming_languages = models.ManyToManyField('ProgrammingLanguages')
    projects = models.ManyToManyField('Projects')
    owner_projects = models.ForeignKey('Projects', on_delete=models.CASCADE, null=True, blank=True)
    working_place = models.ForeignKey('WorkingPlace', on_delete=models.CASCADE, null=True, blank=True)

    avatar = models.ImageField(null=True, blank=True)
    about = models.TextField()
    github = models.URLField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=400, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


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




# Projects app
# class Projects(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     programming_languages_are_using = models.ManyToManyField(ProgrammingLanguages)
#     max_members = models.PositiveIntegerField()
#     full = models.BooleanField(default=False)
#     searching_for_working_place = models.ManyToManyField(WorkingPlace)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = "Project"
#         verbose_name_plural = "Projects"
#         ordering = ['-created_at']
