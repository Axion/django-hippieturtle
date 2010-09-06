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

from django.db import transaction

import cProfile

def test():
    d = None
    users = User.objects.only("power_level")[:500000]
    for user in users.iterator():
        d = user.power_level
    d = None
    #users = User.objects.all("power_level")[:500000]
    
class Command(BaseCommand):
                          
    def handle(self, *args, **options):
        #time.sleep(3)
        #print "testing"

        t1 = time.time()
        #cProfile.runctx('test()', globals(), locals(), 'select_by_pk_orm.profile')
        test()
        print "time=", time.time() - t1
       
        #print "sleeping"
        #time.sleep(2)
        #print "stop"    
