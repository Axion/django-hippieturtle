# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.db import transaction

import os
import sys
import random
import time
import string
import cProfile

from tests.models import User

def test():
    d = None
    for pk in xrange(1,50000):
        user = User.objects.get(pk = pk)  
        user.power_level = 0
        user.save()
        
        #from django.db import connection
        #print connection.queries
        #die 

class Command(BaseCommand):
                          
    def handle(self, *args, **options):
        time.sleep(3)
        print "testing"

        t1 = time.time()
        #cProfile.runctx('test()', globals(), locals(), 'debugging_profiles/update.profile')
        test()
        print "time=", time.time() - t1
       
        print "sleeping"
        time.sleep(2)
        print "stop"    
