from django.db import models
class User(models.Model):
    name = models.CharField(max_length = 255, blank = False)
    email = models.CharField(max_length = 255, blank = False)
    age = models.SmallIntegerField()
    power_level = models.IntegerField()
    info = models.TextField()