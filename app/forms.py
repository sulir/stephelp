from HTMLParser import HTMLParser
from django import forms
from django.core.validators import ValidationError
from django.contrib.auth.models import User
from models import Project

"""A unique user name to be used later for authorization purposes."""
class UsernameField(forms.RegexField):
    def __init__(self, *args, **kwargs):
        super(UsernameField, self).__init__(r'^[\w.@+-]+$', *args, **kwargs)
    
    def validate(self, value):
        super(UsernameField, self).validate(value)
        if User.objects.filter(username=value).count():
            raise ValidationError("Username already exists.")

"""A whitelist-based HTML parser used to validate untrusted user input."""
class AntiXssHtmlParser(HTMLParser):
    allowed_tags = 'h1 h2 h3 b i u ul ol li br p div span blockquote a img'.split()
    allowed_attrs = ('href', 'target', 'rel', 'src', 'alt')
    
    def handle_starttag(self, tag, attrs):
        if tag not in self.allowed_tags:
            raise ValidationError("Tag '%s' is not allowed." % tag)
        for attr in attrs:
            name, value = attr
            if name not in self.allowed_attrs:
                raise ValidationError("Attribute '%s' is not allowed." % name)
            if name in ('href', 'src') and value.strip().startswith('javascript:'):
                raise ValidationError("JavaScript URLs are forbidden.")
    
    def handle_comment(self, data):
        raise ValidationError("HTMl comments are not allowed.")

"""A text field which is rendered as a WYSIWYG HTML editor."""
class HtmlField(forms.CharField):
    widget = forms.Textarea(attrs={'class': 'html-editor'})
    
    def validate(self, value):
        super(HtmlField, self).validate(value)
        AntiXssHtmlParser().feed(value)

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
