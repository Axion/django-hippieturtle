# -*- coding: utf-8 -*-

from benchrun import Benchmark, clock

from django.conf import settings
from django.core.management.base import BaseCommand
import os
import random
import time
import string

#from tests.models import *
import sys

from django.db import models

class U(models.Model):
    #pass
    """
    name = models.TextField(max_length = 255, blank = False)
    name2 = models.TextField(max_length = 255, blank = False)
    name3 = models.TextField(max_length = 255, blank = False)
  
    name4 = models.TextField(max_length = 255, blank = False)
    
    name5 = models.TextField(max_length = 255, blank = False)
    name6 = models.TextField(max_length = 255, blank = False)
    name7 = models.TextField(max_length = 255, blank = False)
    name8 = models.TextField(max_length = 255, blank = False)
    name9 = models.TextField(max_length = 255, blank = False)                
    name10 = models.TextField(max_length = 255, blank = False)       
    
    n1ame = models.TextField(max_length = 255, blank = False)
    n1ame2 = models.TextField(max_length = 255, blank = False)
    n1ame3 = models.TextField(max_length = 255, blank = False)
    n1ame4 = models.TextField(max_length = 255, blank = False)
    n1ame5 = models.TextField(max_length = 255, blank = False)
    n1ame6 = models.TextField(max_length = 255, blank = False)
    n1ame7 = models.TextField(max_length = 255, blank = False)
    n1ame8 = models.TextField(max_length = 255, blank = False)
    n1ame9 = models.TextField(max_length = 255, blank = False)                
    n1ame10 = models.TextField(max_length = 255, blank = False)  
    
    n2ame = models.TextField(max_length = 255, blank = False)
    n2ame2 = models.TextField(max_length = 255, blank = False)
    n2ame3 = models.TextField(max_length = 255, blank = False)
    n2ame4 = models.TextField(max_length = 255, blank = False)
    n2ame5 = models.TextField(max_length = 255, blank = False)
    n2ame6 = models.TextField(max_length = 255, blank = False)
    n2ame7 = models.TextField(max_length = 255, blank = False)
    n2ame8 = models.TextField(max_length = 255, blank = False)
    n2ame9 = models.TextField(max_length = 255, blank = False)                
    n2ame10 = models.TextField(max_length = 255, blank = False)       
    
    n12ame = models.TextField(max_length = 255, blank = False)
    n12ame2 = models.TextField(max_length = 255, blank = False)
    n12ame3 = models.TextField(max_length = 255, blank = False)
    n12ame4 = models.TextField(max_length = 255, blank = False)
    n12ame5 = models.TextField(max_length = 255, blank = False)
    n12ame6 = models.TextField(max_length = 255, blank = False)
    n12ame7 = models.TextField(max_length = 255, blank = False)
    n12ame8 = models.TextField(max_length = 255, blank = False)
    n12ame9 = models.TextField(max_length = 255, blank = False)                
    n12ame10 = models.TextField(max_length = 255, blank = False)           
    
    n22ame = models.TextField(max_length = 255, blank = False)
    n22ame2 = models.TextField(max_length = 255, blank = False)
    n22ame3 = models.TextField(max_length = 255, blank = False)
    n22ame4 = models.TextField(max_length = 255, blank = False)
    n22ame5 = models.TextField(max_length = 255, blank = False)
    n22ame6 = models.TextField(max_length = 255, blank = False)
    n22ame7 = models.TextField(max_length = 255, blank = False)
    n22ame8 = models.TextField(max_length = 255, blank = False)
    n22ame9 = models.TextField(max_length = 255, blank = False)                
    n22ame10 = models.TextField(max_length = 255, blank = False)       
    
    n122ame = models.TextField(max_length = 255, blank = False)
    n122ame2 = models.TextField(max_length = 255, blank = False)
    n122ame3 = models.TextField(max_length = 255, blank = False)
    n122ame4 = models.TextField(max_length = 255, blank = False)
    n122ame5 = models.TextField(max_length = 255, blank = False)
    n122ame6 = models.TextField(max_length = 255, blank = False)
    n122ame7 = models.TextField(max_length = 255, blank = False)
    """
    n122ame8 = models.TextField(max_length = 255, blank = False)
    n122ame9 = models.TextField(max_length = 255, blank = False)                
    n122ame10 = models.TextField(max_length = 255, blank = False)                 
    

#class U2()

class Command(BaseCommand):
                          
    def handle(self, *args, **options):
    
        time.sleep(1)
        print "start"    
    
        t1 = clock()

        data = [U() for x in xrange(100)]
        
        print "finished in", clock() - t1
    
        print "sleeping"
        time.sleep(2)
        print "stop"    
