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

@transaction.commit_manually
def test():
    d = None
    for pk in xrange(1, SELECT_ITERATIONS):
        user = User.objects.get(pk = pk).delete()
        d = user.power_level

    d = None

class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option('--get_sql', action='store_true', dest='get_sql', default=False),
        make_option('--profile', action='store_true', dest='profile', default=False)
    )

    def handle(self, *args, **options):

        if options['get_sql']:
            settings.DEBUG = True
            #User.objects.get(pk = 1).delete()
            User.objects.filter(pk = 2).delete()
            #print connection.queries[0]["sql"]
            print connection.queries
            sys.exit(0)

        start()
        if options['profile']:
            import cProfile
            cProfile.runctx('test()', globals(), locals(), './debugging_profiles/select_simple_orm.profile')
        else:
            test()
        stop()

