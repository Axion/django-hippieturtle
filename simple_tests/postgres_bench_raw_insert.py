# -*- coding: utf-8 -*-

import random
import time
import string
import psycopg2
import cProfile

def save(userdata):
    conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "DrDn0809", db = "tester")
    conn = psycopg2.connect(host = "localhost", user = "postgresql", passwd = "DrDn0809", db = "tester")
    cursor = conn.cursor ()
    for entry in userdata:
        cursor.execute ("INSERT INTO `tests_user` (`name`, `email`, `age`, `power_level`, `info`) VALUES (%(name)s, %(email)s, %(age)s, %(power_level)s, %(info)s)", entry)


def r(len):
    return ''.join(random.choice(string.ascii_letters) for x in range(len))

time.sleep(2)
print "connection"

"""
conn = MySQLdb.connect (host = "localhost", user = "root", passwd = "DrDn0809", db = "tester")
cursor = conn.cursor ()
"""
time.sleep(2)
print "cache start"

userdata = []
for i in range(10000):
    userdata.append({'name':r(20), 'email':r(20), 'age':random.randint(10,80), 'power_level':random.randint(-100,100), 'info':r(400)})

time.sleep(2)
print "insert start"
cProfile.runctx('save(userdata)', globals(), locals(), 'insert_raw.profile')


"""
i = 0
t1 = time.time()
for entry in userdata:
    i = i + 1
    cursor.execute ("INSERT INTO `tests_user` (`name`, `email`, `age`, `power_level`, `info`) VALUES (%(name)s, %(email)s, %(age)s, %(power_level)s, %(info)s)", entry)
    #if i % 5000 == 0:
    #    print i
print "time=", time.time()  - t1
print "end"    
"""    
time.sleep(2)    
"""    
cursor.close ()
conn.close ()
"""
