from django import forms
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.files.images import get_image_dimensions
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from main.models import UserProfile

import re


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get("username")

        try:
            User.objects.get(username=username.lower())
        except ObjectDoesNotExist:
            pass
        else:
            self.add_error("username", "This username exists. Please, choose another one")

        return cleaned_data


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'working_place',
            'avatar',
            'about',
            'programming_languages',
            'github',
            'linkedin',
        ]

    def clean(self):
        cleaned_data = super().clean()

        prog_languages = cleaned_data.get("programming_languages")
        github = cleaned_data.get("github")
        linkedin = cleaned_data.get("linkedin")

        if prog_languages and len(prog_languages) > 7:
            self.add_error('programming_languages', 'You can choose maximum 7 skills.')
        if github is not None:
            links = [r'https://github.com/', r'https://www.github.com/', r'http://github.com/', r'http://www.github.com/']
            if not len(list(filter(None, map(lambda link: re.search(link, github), links)))):
                self.add_error('github', 'GitHub link is invalid.')

        if linkedin is not None:
            links = [r'https://linkedin.com/', r'https://www.linkedin.com/', r'http://linkedin.com/', r'http://www.linkedin.com/']
            if not len(list(filter(None, map(lambda link: re.search(link, linkedin), links)))):
                self.add_error('linkedin', 'LinkedIn link is invalid.')

        return cleaned_data
