from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WebUser(User):

    class Meta:
        proxy = True
        # custom ordering, etc

    # custom methods

# TODO is a profile necessary
# class WebProfile(models.Model):
#     pass
