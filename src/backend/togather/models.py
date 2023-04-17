from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


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
    # creator = models.ForeignKey(TogatherUser)
    # moderators = models.ManyToManyField(TogatherUser, blank=True)
    # participants = models.ManyToManyField(TogatherUser, blank=True)
    # interested = models.ManyToManyField(TogatherUser, blank=True)
    # participation_requests = models.ManyToManyField(TogatherUser)
    max_participants = models.PositiveIntegerField()

    # Location
    geo_lat = models.IntegerField()
    geo_long = models.IntegerField()
    address = models.CharField(max_length=150)

    # Time
    date = models.DateField()
    start_time = models.TimeField()

    # Status
    is_archived = models.BooleanField(default=False)


class Photo(models.Model):
    photo = models.ImageField()
    order = models.PositiveSmallIntegerField(unique=True)

    class Meta:
        abstract = True


class UserPhoto(Photo):
    pass


class EventPhoto(Photo):
    pass


class TogatherUser(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()
    bio = models.TextField()
    other_sites = models.JSONField()
    friends = models.ManyToManyField("self")
    creator_score = models.PositiveSmallIntegerField()
    participant_score = models.PositiveSmallIntegerField()
