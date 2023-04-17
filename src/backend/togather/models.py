from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class TogatherUser(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()
    bio = models.TextField()
    other_sites = models.JSONField()
    friends = models.ManyToManyField("self")
    creator_score = models.PositiveSmallIntegerField()
    participant_score = models.PositiveSmallIntegerField()
