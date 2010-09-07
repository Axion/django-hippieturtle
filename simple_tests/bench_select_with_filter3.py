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
    for x in xrange(SELECTS_ITERATIONS):
        cursor.execute ("SELECT `tests_user`.`id`, `tests_user`.`name`, `tests_user`.`email`, `tests_user`.`age`, `tests_user`.`power_level`, `tests_user`.`info` FROM `tests_user` WHERE `tests_user`.`power_level` > 0  LIMIT %s", SUB_SELECT_ITERATIONS+x)
        results = cursor.fetchall()
        """
        for row in results:
            id = row[0]
            name = row[1]
            email = row[2]
            age = row[3]
            power_level = row[4]
            info = row[5]
        """
    cursor = dbconfig.cursor_close()

start()
if args.profile:
    import cProfile
    cProfile.runctx('test()', globals(), locals(), './debugging_profiles/select_all_sql.profile')
else:
    test()
stop()