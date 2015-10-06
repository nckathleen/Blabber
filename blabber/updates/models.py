from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Status(models.Model):
    #  creating columns in our model's data structure. Status is a subclass of Model.
    text = models.CharField(max_length=141)
    posted_at = models.DateTimeField()
    user = models.ForeignKey(User)  # points to other tables to get data, using IDs.
                                    #  Id is implied for Status.)


class Favorite(models.Model):
    user = models.ForeignKey(User)
    Status = models.ForeignKey(Status)
