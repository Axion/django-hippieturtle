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

from django.db.models import Q

from tests.models import User
from optparse import make_option

from sleepconfig import *

@transaction.commit_manually
def test():
    for x in xrange(SELECTS_ITERATIONS):
        users = User.objects.filter(Q(power_level__gt=0))[:SUB_SELECT_ITERATIONS+x]
        ct = bool(users)

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--get_sql', action='store_true', dest='get_sql', default=False),
        make_option('--profile', action='store_true', dest='profile', default=False)
    )

    def handle(self, *args, **options):

        if options['get_sql']:
            settings.DEBUG = True
            users = User.objects.filter(Q(power_level__gt = 0))[:SELECT_ITERATIONS]
            print users.query
            sys.exit(0)

        start()
        if options['profile']:
            import cProfile
            cProfile.runctx('test()', globals(), locals(), './debugging_profiles/select_simple_orm.profile')
        else:
            test()
        stop()