#!/usr/bin/python
# -*- coding: utf-8 -*-

import commands
import argparse
import os
import time
from utils import *

import operator

from dbconfig import *

DELTAY_INT = 0

print "Welcome to HippieTurtle - Django ORM testing suite, please note that this script will run only under Ubuntu with mysql, postgres and sqlight installed. Please run it as root, if you want to restart your db before each test."

testcases = {
    "insert" : ("Create new db rows by either model.save() or sql insert", ['insert'], ['insert']),
    "select_one_field" : ("Select all fields from db rows, access one field", ['select_simple','select_defer','select_only', 'select_values'], ['select_all','select_onefield', 'select_onefield_pk']),
    "select_one_query" : ("Select all fields from db in one query, access one field", ['select_onequery','select_onequery_noiterator'], ['select_onequery']),
    "delete" : ("Select all fields from db in one query, access one field", ['delete',], ['delete',]),
    "cache_bug" : ("Select all fields from db in one query, access one field", ['select_with_filter','select_with_filter2'], ['select_with_filter','select_with_filter2']),

    "select_with_filter" : ("Select all fields from db in one query, access one field", ['select_with_filter','select_with_filter3','select_with_filter_Q'], ['select_with_filter','select_with_filter3']),
}

print "Select testcase to execute"

i = 0
for k, v in testcases.items():
    print "%s %s" % (k,v[0])
    i = i + 1

#inp = raw_input()

command = "cache_bug"


print "You selected %s" % (command)

save_sql = False
save_profile = False


#if check_base:
#    status, output = commands.getstatusoutput('./runner.sh "%s" 1 > reports/%s_orm.txt' % ("python ./manage.py bench_%s" % cmd, cmd))


status, output = commands.getstatusoutput('rm turtle_test_pipe')
status, output = commands.getstatusoutput('mkfifo turtle_test_pipe')

if save_sql:

    for cmd in testcases[command][1]:
        print "saving SQL for ORM test"
        status, output = commands.getstatusoutput('python ./manage.py bench_%s --get_sql > sql/%s_%s.sql' % (cmd, DATABASE_ENGINE, cmd))
        print output

if save_profile:
    for cmd in testcases[command][1]:
        print "generating debug profile for ORM test"
        print 'python ./manage.py bench_%s --profile' % cmd
        status, output = commands.getstatusoutput('python ./manage.py bench_%s_%s --profile' % (DATABASE_ENGINE, cmd))
        #print output

    for cmd in testcases[command][2]:
        print "generating debug profile for SQL test"
        status, output = commands.getstatusoutput('python ./simple_tests/bench_%s_%s.py --profile' % (DATABASE_ENGINE, cmd))
        #print output

run_times = {}
mem_usage = {}
mem_usage_relative = {}

for cmd in testcases[command][1]:
    db_prep()
    print "checking speed and memory consuption of ORM test"
    status, output = commands.getstatusoutput('(./runner.sh "%s" 0.2  > turtle_test_pipe &);(sleep 0.5);(cat < turtle_test_pipe > reports/%s_%s_orm.txt)' % ("python ./manage.py bench_%s" % cmd, DATABASE_ENGINE, cmd))
    print output

    max_mem = 0
    run_time = 0

    mem = 0
    base_mem = 0

    for line in open("reports/%s_orm.txt" % cmd,'r'):
        (pcmd, val) = line.split(":")
        if pcmd == "mem":
            mem = round(float(val.strip())) / 1024.0
            max_mem = max(max_mem, mem)
        elif pcmd == "time":
            run_time = round(float(val.strip()),1)
        elif pcmd == "msg" and val.strip() == "testing":
            base_mem = mem
            print "BM", base_mem

    run_times["ORM_%s" % cmd] = run_time
    mem_usage["ORM_%s" % cmd] = max_mem
    mem_usage_relative["ORM_%s" % cmd] = max_mem-base_mem

    print "sleeping"
    time.sleep(DELTAY_INT)

for cmd in testcases[command][2]:
    db_prep()

    print "checking speed and memory consuption of SQL test"
    status, output = commands.getstatusoutput('(./runner.sh "%s" 0.2  > turtle_test_pipe &);(sleep 0.5);(cat < turtle_test_pipe > reports/%s_%s_sql.txt)' % ("python ./simple_tests/bench_%s.py" % cmd, DATABASE_ENGINE, cmd))
    #print output

    max_mem = 0
    run_time = 0

    base_mem = 0
    mem = 0

    for line in open("reports/%s_sql.txt" % cmd,'r'):
        (pcmd, val) = line.split(":")

        #print pcmd, val
        if pcmd == "mem":
            mem = round(float(val.strip())) / 1024.0
            max_mem = max(max_mem, mem)
        elif pcmd == "time":
            run_time = round(float(val.strip()),1)
        elif pcmd == "msg" and val.strip() == "testing":
            base_mem = mem
            print "BM", base_mem


    run_times["SQL_%s" % cmd] = run_time
    mem_usage["SQL_%s" % cmd] = max_mem
    mem_usage_relative["SQL_%s" % cmd] = max_mem-base_mem

    print "sleeping"
    time.sleep(DELTAY_INT)


points = [(name, val) for name, val in run_times.items()]
sorted_points = sorted(points, key=lambda k: k[1])
print points
graph(sorted_points ,"charts/%s_%s_time.png" % (DATABASE_ENGINE, command), "time", command)

points = [(name, val) for name, val in mem_usage.items()]
sorted_points = sorted(points, key=lambda k: k[1])
print points
graph(sorted_points,"charts/%s_%s_mem.png" % (DATABASE_ENGINE, command), "mem", command)

points = [(name, val) for name, val in mem_usage_relative.items()]
sorted_points = sorted(points, key=lambda k: k[1])
print points
graph(sorted_points,"charts/%s_%s_mem_relative.png" % (DATABASE_ENGINE, command), "mem", command)

dirList=os.listdir("./debugging_profiles/")
for fname in dirList:
    print fname
    status, output = commands.getstatusoutput('./tools/gprof2dot.py -f pstats ./debugging_profiles/%s | dot -Tpng -o ./report_images/%s.png' % (fname, fname))