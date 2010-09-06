# -*- coding: utf-8 -*-

from benchrun import Benchmark, clock

from django.conf import settings
from django.core.management.base import BaseCommand
import os
import random
import time
import string

from tests.models import *
import sys

def r(len):
    return ''.join(random.choice(string.ascii_letters) for x in range(len))

class Command(BaseCommand):
                          
    def handle(self, *args, **options):
        d = User_3()
        print "end"
        d = User_5()
        print "end"
