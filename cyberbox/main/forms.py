from django import forms
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from main.models import UserProfile


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


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

    # def clean(self):
    #     cleaned_data = super().clean()
    #     img = cleaned_data.get("avatar")
    #     print(img)
    #     print(self.img)
    #     prog_languages = cleaned_data.get("programming_languages")
    #     github = cleaned_data.get("github")
    #     linkedin = cleaned_data.get("linkedin")
    #
    #     # from PIL import Image, ImageOps
    #     # mask = Image.open('static/assets/mask.png').convert('L')
    #     # im = Image.open(self.img.path)
    #     #
    #     # output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
    #     # output.putalpha(mask)
    #     # output.save(self.img.path)
    #     print(prog_languages)
    #     # if len(prog_languages) > 7:
    #     #     raise ValidationError("You can choose maximum 7 skills.")
    #     print(github)
    #     print(linkedin)
