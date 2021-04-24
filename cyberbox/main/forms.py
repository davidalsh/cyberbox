from django import forms
from django.contrib.auth.models import User

from main.models import *


class LoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        print(self.cleaned_data)
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'That was an invalid username or password.')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError('That was an invalid username or password.')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password']
