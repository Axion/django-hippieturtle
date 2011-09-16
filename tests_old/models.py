# -*- coding: utf-8 -*-

from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 255, blank = False)
    email = models.CharField(max_length = 255, blank = False)
    age = models.SmallIntegerField(blank = False)
    power_level = models.IntegerField(blank = False)
    info = models.TextField(blank = False)
    
    
class User_empty(models.Model):
    pass

class User_tn(models.Model):
    name = models.CharField(max_length = 255, blank = False)
    name2 = models.CharField(max_length = 255, blank = False)    
    name3 = models.CharField(max_length = 255, blank = False)                
    n1ame = models.CharField(max_length = 255, blank = False)
    n1ame2 = models.CharField(max_length = 255, blank = False)    
    n1ame3 = models.CharField(max_length = 255, blank = False)                
    n2ame = models.CharField(max_length = 255, blank = False)
    n2ame2 = models.CharField(max_length = 255, blank = False)    
    n2ame3 = models.CharField(max_length = 255, blank = False)                
    n3ame = models.CharField(max_length = 255, blank = False)
    n3ame2 = models.CharField(max_length = 255, blank = False)    
    n3ame3 = models.CharField(max_length = 255, blank = False)                

      
