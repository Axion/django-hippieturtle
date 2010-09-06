# -*- coding: utf-8 -*-

import random
import time
import string
import sys
import os
import MySQLdb
import argparse

sys.path.insert(0, os.getcwd())
from sleepconfig import *
import dbconfig

parser = argparse.ArgumentParser(prog='HippieTurtle', description='Django ORM testing')
parser.add_argument('-p', '--profile', help='profile', action="store_true", default=False, dest="profile")
args = parser.parse_args()

def save(userdata):
    cursor = dbconfig.cursor()
    for entry in userdata:
        cursor.execute ("INSERT INTO `tests_user` (`name`, `email`, `age`, `power_level`, `info`) VALUES (%(name)s, %(email)s, %(age)s, %(power_level)s, %(info)s)", entry)


def r(len):
    return ''.join(random.choice(string.ascii_letters) for x in range(len))

time.sleep(PRETEST_SLEEP)

userdata = []
for i in range(INSERT_ITERATIONS):
    userdata.append({'name':r(20), 'email':r(20), 'age':random.randint(10,80), 'power_level':random.randint(-100,100), 'info':r(400)})

start()

if args.profile:
    import cProfile
    cProfile.runctx('save(userdata)', globals(), locals(), './debugging_profiles/insert_raw.profile')
else:
    save(userdata)

stop()
