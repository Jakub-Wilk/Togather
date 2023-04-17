from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from togather.models import TogatherUser


class TogatherUserInline(admin.StackedInline):
    model = TogatherUser
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [TogatherUserInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
