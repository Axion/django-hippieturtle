# -*- coding: utf-8 -*-

import random
import time
import string
import MySQLdb
import cProfile

def test():
    conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "DrDn0809", db = "tester")
    cursor = conn.cursor ()
    d = None
    for pk in xrange(1,50000):
        cursor.execute ("SELECT `tests_user`.`id`, `tests_user`.`name`, `tests_user`.`email`, `tests_user`.`age`, `tests_user`.`power_level`, `tests_user`.`info` FROM `tests_user` WHERE `tests_user`.`id` = %(pk)s", {'pk' : pk})
        row = cursor.fetchone()
        d = row[4]
        d = 0
        cursor.execute ("UPDATE `tests_user` SET `name` = %s, `email` = %s, `age` = %s, `power_level` = %s, `info` = %s WHERE `tests_user`.`id` = %s", (row[1], row[2], row[3], d, row[5], pk ))
        
    d = None
        
    cursor.close ()
    conn.close ()
    
time.sleep(5)
print "test start"
t1 = time.time()
#cProfile.runctx('test()', globals(), locals(), '../debugging_profiles/select_raw.profile') 
test()
print time.time() - t1
print "test end"
time.sleep(5)    

