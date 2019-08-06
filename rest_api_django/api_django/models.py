from django.db import models

# We create models for this model we want to create ReST_API (1st)
class UserApis(models.Model):
    name = models.CharField(max_length= 100)
    email = models.EmailField(unique = True)
    create= models.DateTimeField(auto_now_add = True)
    view = models.DateTimeField(auto_now = True)
