from django.db import models
from django.contrib.auth.models import User

# Create your models here.


from django.db import models

# Create your models here.


class Status(models.Model):
    #  creating columns in our model's data structure. Status is a subclass of Model.
    text = models.Charfield(max_length=141)
    posted_at = models.DateTime()
    user = models.ForeignKey(User)  # points to other tables to get data, using IDs.
                                    #  Id is implied for Status.)
        
