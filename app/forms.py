from django import forms
from django.forms.widgets import TextInput
from models import Project, Task, User
from fields import UsernameField, HtmlField

"""A user registration (and possibly editing) form."""
class UserForm(forms.Form):
    username = UsernameField(
        max_length=30,
        help_text="Max. 30 characters. Letters, digits and .@+-_"
    )
    password = forms.CharField(
        min_length=5,
        widget=forms.PasswordInput(render_value=True, attrs={'autocomplete': 'off'}),
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

"""A form used to create or edit a project."""
class ProjectForm(forms.ModelForm):
    description = HtmlField()
    
    class Meta:
        model = Project
        exclude = ('owner',)
    
    def save(self, owner):
        project = super(ProjectForm, self).save(commit=False)
        project.owner = owner
        project.save()
        return project

"""A task creation form."""
class TaskForm(forms.ModelForm):
    class Meta:
        CLASSES = 'input-block-level init-clear'
        model = Task
        widgets = {
            'project': forms.HiddenInput,
            'description': forms.TextInput(attrs={'class': CLASSES, 'placeholder': 'Description'}),
            'assigned_to': forms.TextInput(attrs={'class': CLASSES, 'placeholder': 'Assignee', 'maxlength': 30}),
            'status': forms.Select(attrs={'class': CLASSES})
        }
    
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['assigned_to'].error_messages = {
            'invalid_choice': "Please enter an existing username or leave blank."
        }
