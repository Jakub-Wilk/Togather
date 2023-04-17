from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

from django.db.models.signals import pre_delete
from django.dispatch import receiver


class TogatherUser(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="togather_user")
    phone_number = PhoneNumberField(blank=True)  # TODO change before release to disallow blank
    bio = models.TextField(blank=True)
    other_sites = models.JSONField(blank=True, null=True, default=list)
    friends = models.ManyToManyField("self", blank=True)
    creator_score = models.PositiveSmallIntegerField(blank=True, null=True)
    participant_score = models.PositiveSmallIntegerField(blank=True, null=True)


class Event(models.Model):
    # General
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200)
    tags = models.JSONField()
    description = models.CharField(max_length=2000, blank=True)
    price = models.PositiveIntegerField(default=0)

    class AccessTypes(models.IntegerChoices):
        OPEN = 1, "OPEN"
        WHITELIST = 2, "WHITELIST"
        PREMIUM = 3, "PREMIUM"
        FRIENDS = 4, "FRIENDS"
        INVITE = 5, "INVITE ONLY"

    access_type = models.PositiveSmallIntegerField(choices=AccessTypes.choices)

    # Users
    creator = models.ForeignKey(TogatherUser, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="created_events")
    moderators = models.ManyToManyField(TogatherUser, blank=True, related_name="moderated_events")
    participants = models.ManyToManyField(TogatherUser, blank=True, related_name="participating_events")
    interested = models.ManyToManyField(TogatherUser, blank=True, related_name="interested_events")
    participation_requests = models.ManyToManyField(TogatherUser, blank=True, related_name="requested_events")
    max_participants = models.PositiveIntegerField(blank=True, null=True)

    # Location
    geo_lat = models.IntegerField()
    geo_long = models.IntegerField()
    address = models.CharField(max_length=150)

    # Time
    date = models.DateField()
    start_time = models.TimeField()

    # Status
    is_archived = models.BooleanField(default=False)


# If the event is archived, it doesn't get deleted when the creator deletes their profile
@receiver(pre_delete, sender=TogatherUser, dispatch_uid="togatheruser_delete_signal")
def delete_if_not_archived(sender, instance, using, **kwargs):
    instance.created_events.filter(is_archived=True).update(creator=None)
    instance.created_events.filter(is_archived=False).delete()


class Photo(models.Model):
    photo = models.ImageField()
    order = models.PositiveSmallIntegerField(unique=True)

    class Meta:
        abstract = True


class UserPhoto(Photo):
    user = models.ForeignKey(TogatherUser, on_delete=models.CASCADE, related_name="photos")


class EventPhoto(Photo):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="photos")
