# -*- coding: utf-8 -*-

import random
import time
import string
import MySQLdb
import cProfile

import dbconfig

def test():
    cursor = dbconfig.cursor()
    for pk in xrange(1,10000):
        cursor.execute ("SELECT `tests_user`.`id`, `tests_user`.`name`, `tests_user`.`email`, `tests_user`.`age`, `tests_user`.`power_level`, `tests_user`.`info` FROM `tests_user` WHERE `tests_user`.`id` = %(pk)s", {'pk' : pk})
        row = cursor.fetchone()
    dbconfig.cursor_close()

    
print "warming up"
test()
print "db ready"
