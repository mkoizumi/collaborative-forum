from django.db import models
from django.contrib import auth # library for user authentication

# Create your models here.

# already have predefined username, email, password etc for forms
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "User: {}".format(self.username)
