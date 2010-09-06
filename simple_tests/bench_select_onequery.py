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

def test():
    cursor = dbconfig.cursor()
    d = None
    cursor.execute ("SELECT `tests_user`.`id`, `tests_user`.`name`, `tests_user`.`email`, `tests_user`.`age`, `tests_user`.`power_level`, `tests_user`.`info` FROM `tests_user` LIMIT %s", SELECT_ITERATIONS)
    result_set = cursor.fetchall ()
    for row in result_set:
        d = row[4]
    d = None
    cursor = dbconfig.cursor_close()

start()
if args.profile:
    import cProfile
    cProfile.runctx('test()', globals(), locals(), './debugging_profiles/select_onefield_sql.profile')
else:
    test()
stop()

