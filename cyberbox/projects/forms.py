from django import forms

from projects.models import Projects


class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = [
            'title',
            'description',
            'programming_languages_are_using',
            'searching_for_working_place',
            'open',
            'max_members',
        ]

    def clean(self):
        cleaned_data = super().clean()
        members = cleaned_data['max_members']

        if members < 2:
            self.add_error('max_members', 'Members must be more than 1')
        elif members > 1000:
            self.add_error('max_members', 'Members must be less than 1000')

        return cleaned_data

