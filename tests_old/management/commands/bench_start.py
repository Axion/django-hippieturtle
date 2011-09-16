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

class Command(BaseCommand):
                          
    def handle(self, *args, **options):    
        time.sleep(5)
        print "start"    
        print "sleeping"
        time.sleep(10)
        print "stop"    
