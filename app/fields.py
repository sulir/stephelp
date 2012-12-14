from HTMLParser import HTMLParser
from django.forms import CharField, RegexField, Textarea
from django.core.validators import ValidationError
from models import User

"""A unique user name to be used later for authorization purposes."""
class UsernameField(RegexField):
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
class HtmlField(CharField):
    widget = Textarea(attrs={'class': 'html-editor'})
    
    def validate(self, value):
        super(HtmlField, self).validate(value)
        AntiXssHtmlParser().feed(value)