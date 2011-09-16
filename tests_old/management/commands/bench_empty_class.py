# -*- coding: utf-8 -*-

from benchrun import Benchmark, clock

from django.conf import settings
from django.core.management.base import BaseCommand
import os
import random
import time
import string

from tests.models import User
import sys

def r(len):
    return ''.join(random.choice(string.ascii_letters) for x in range(len))

class T():
    pass

class Command(BaseCommand):
                          
    def handle(self, *args, **options):
    
        time.sleep(5)
        print "start"    
    
        t1 = clock()

        data = [T() for x in xrange(100000)]
        
        print "finished in", clock() - t1
    
        print "sleeping"
        time.sleep(10)
        print "stop"    
