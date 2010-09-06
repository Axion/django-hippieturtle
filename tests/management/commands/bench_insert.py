# -*- coding: utf-8 -*-

import os
import random
import time
import string
import sys

from django.conf import settings
from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction
from django.db import connection

from tests.models import User
from optparse import make_option

from sleepconfig import *

def r(len):
    return ''.join(random.choice(string.ascii_letters) for x in range(len))


@transaction.commit_manually
def save(userdata):
    for entry in userdata:
        User(**entry).save()
    transaction.commit()

class Command(BaseCommand):
    
    option_list = BaseCommand.option_list + (
        make_option('--get_sql', action='store_true', dest='get_sql', default=False),
        make_option('--profile', action='store_true', dest='profile', default=False)
    )
                          
    def handle(self, *args, **options):
    
        if options['get_sql']:
            settings.DEBUG = True
            entry = {'name':r(20), 'email':r(20), 'age':random.randint(10,80), 'power_level':random.randint(-100,100), 'info':r(400)}
            User(**entry).save()
            print connection.queries[0]["sql"]
            sys.exit(0)
    
        time.sleep(PRETEST_SLEEP)

        userdata = []
        for i in range(INSERT_ITERATIONS):
            userdata.append({'name':r(20), 'email':r(20), 'age':random.randint(10,80), 'power_level':random.randint(-100,100), 'info':r(400)})
        
        start()
        if options['profile']:
            import cProfile
            cProfile.runctx('save(userdata)', globals(), locals(), './debugging_profiles/insert_orm.profile')
        else:
            save(userdata)
        stop()