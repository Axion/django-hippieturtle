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

from optparse import make_option

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--code', dest='code'),
    )

    def handle(self, *args, **options):
        eval()
