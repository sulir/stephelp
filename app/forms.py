from django import forms
from django.core.validators import ValidationError
from django.contrib.auth.models import User
from models import Project

class UsernameField(forms.RegexField):
    def __init__(self, *args, **kwargs):
        super(UsernameField, self).__init__(r'^[\w.@+-]+$', *args, **kwargs)
    
    def validate(self, value):
        super(UsernameField, self).validate(value)
        if User.objects.filter(username=value).count():
            raise ValidationError("Username already exists.")

class UserForm(forms.Form):
    username = UsernameField(
        max_length=30,
        help_text="Max. 30 characters. Letters, digits and .@+-_"
    )
    password = forms.CharField(
        min_length=5,
        widget=forms.PasswordInput(attrs={'autocomplete': 'off'}),
        help_text="At least 5 characters."
    )
    email = forms.EmailField(
        label="E-mail",
        help_text="Project support requests will be sent to this e-mail."
    )
    name = forms.CharField(
        max_length=100,
        help_text="Either your full name (John Doe) or organization (Acme)."
    )
    info = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 3}),
        label="Profile info",
        help_text="Optional. This will be displayed in your public profile."
    )

class ProjectForm(forms.ModelForm):
    def save(self, owner):
        project = super(ProjectForm, self).save(commit=False)
        project.owner = owner
        project.save()
        return project
    
    class Meta:
        model = Project
        exclude = ('owner',)
        widgets = {'description': forms.Textarea(attrs={'class': 'html-editor'})}
