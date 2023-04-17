from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from togather.models import TogatherUser, Event


class CreatedEventsInline(admin.TabularInline):
    model = Event
    show_change_link = True
    fields = ["name"]
    verbose_name_plural = "Created Events"
    extra = 0


class ModeratedEventsInline(admin.TabularInline):
    model = Event.moderators.through
    verbose_name_plural = "Moderated Events"
    extra = 0


class ParticipatedEventsInline(admin.TabularInline):
    model = Event.participants.through
    verbose_name_plural = "Participated-in Events"
    extra = 0


class InterestedEventsInline(admin.TabularInline):
    model = Event.interested.through
    verbose_name_plural = "Interested-in Events"
    extra = 0


class RequestedEventsInline(admin.TabularInline):
    model = Event.participation_requests.through
    verbose_name_plural = "Requested-access-to Events"
    extra = 0


class TogatherUserAdmin(admin.ModelAdmin):
    model = TogatherUser
    inlines = [CreatedEventsInline, ModeratedEventsInline, ParticipatedEventsInline, InterestedEventsInline, RequestedEventsInline]


admin.site.register(TogatherUser, TogatherUserAdmin)


class TogatherUserInline(admin.StackedInline):
    model = TogatherUser
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [TogatherUserInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Event)
