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

class T(object):
    pass
    
class T3(object):
    p1 = T()   
    p2 = T()
    p3 = T()
    p4 = T()
    p5 = T()
    p6 = T()
    p7 = T()
    p8 = T()                            
    p9 = T()   
    p10 = T()
    p11 = T()
    p12 = T()
    p13 = T()
    p14 = T()
    p15 = T()
    p16 = T()                            


class Command(BaseCommand):
                          
    def handle(self, *args, **options):
    
        time.sleep(1)
        print "start"    
    
        t1 = clock()

        data = [T3() for x in xrange(100000)]
        
        print "finished in", clock() - t1
    
        print "sleeping"
        time.sleep(2)
        print "stop"    
