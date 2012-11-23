from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from models import *

for model in [Category, Project, ProjectPart]:
    admin.site.register(model)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class UserAdmin(DjangoUserAdmin):
    list_display = ('username', 'email')
    inlines = (UserProfileInline,)
    fieldsets = (
        (None, {'fields': ('username', 'password', 'email')}),
        ("Permissions", {'fields': ('is_active', 'is_staff', 'is_superuser')})
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)