import random
import inspect
import subprocess
import commands
import time

import pycha.bar
import cairo
import CairoPlot


class TurtleTest(object):

    def pipe_print(self, str):
        with open('turtle_test_pipe', 'r+') as f:
            f.write(str + "\n")

    def test(self):
        results = dict()
        for test in self.__tests():
            results[test['name']] = self.__run_tests(test)

        self.__generate_charts(results)

    def __warmup(self):
        pass

    def __restart_db(self):
        status, output = commands.getstatusoutput("service mysql restart")

    def __tests(self):
        return [
            #{'name': 'Insert', 'file': 'orm_tests.test', 'class': 'TestInsert'},
            #{'name': 'Select', 'file': 'orm_tests.test', 'class': 'TestSelect'},
            #{'name': 'Select one field', 'file': 'orm_tests.test', 'class': 'TestSelectOneField'},
            #{'name': 'Select one query', 'file': 'orm_tests.test', 'class': 'TestSelectOneQuery'},
            #{'name': 'Select with filter', 'file': 'orm_tests.test', 'class': 'TestCacheBug'},
            {'name': 'Select with filter', 'file': 'orm_tests.test', 'class': 'TestSelectWithFilter'},
            ]

    def __run_tests(self, test):
        module = __import__(test['file'], fromlist=[test['class'], ])
        klass = getattr(module, test['class'])

        results = dict()

        for method in inspect.getmembers(klass, predicate=inspect.ismethod):
            if method[0].startswith("test_orm_")\
            or method[0].startswith("test_sql_"):

                self.__restart_db()
                self.__warmup()

                results[method[0]] = self.__run_test(method[0], test['class'], test['file'])
        return results

    def __generate_charts(self, results):

        for test, test_data in results.items():
            mem_data = list()
            time_data = list()

            h_labels = list()

            for key, value in test_data.items():
                #print key, value
                time_data.append(value[0])
                mem_data.append(value[1])
                h_labels.append(key.replace("test_", "").replace("_", " ").capitalize())

            #data = [[3,4], [4,8], [5,3], [9,1]]
            #v_labels = ["line1", "line2", "line3", "line4", "line5", "line6"]
            #h_labels = ["group1", "group2", "group3", "group4"]

            CairoPlot.bar_plot('charts/time_%s.png' % key, time_data, 900, 300, border=20, \
                grid=True, h_labels=h_labels)
            CairoPlot.bar_plot('charts/mem_%s.png' % key, mem_data, 900, 300, border=20, \
                grid=True, h_labels=h_labels)

    def __run_test(self, method, klass, file):
        from django.core.management import call_command
        call_command('syncdb', interactive=True)

        print "running"
        #subprocess.Popen(['./runner.sh', ''])
        #subprocess.Popen(['python', 'run_django.py', file, method, klass])

        status, output = commands.getstatusoutput('rm turtle_test_pipe')
        status, output = commands.getstatusoutput('mkfifo turtle_test_pipe')

        cmd = "python run_test.py %s %s %s" % (file, method, klass)
        print cmd
        runner = '(./runner.sh "%s" 0.2 > turtle_test_pipe &);(sleep 0.5);' \
                 '(cat < turtle_test_pipe > out.txt)' % cmd
        status, output = commands.getstatusoutput(runner)

        max_mem = 0
        base_mem = 0
        exec_time = 0

        with open('out.txt', 'r') as f:

            while 1:
                line = f.readline()
                if not line:
                    break

                line = line.strip()

                if line == "Starting test":
                    base_mem = int(f.readline().replace("mem:", "").strip())
                    max_mem = base_mem

                elif line.startswith("time:"):
                    exec_time = float(line.replace("time:", ""))

                elif line.startswith("mem:") and base_mem:
                    max_mem = max(int(line.replace("mem:", "")), max_mem)

        print "time", exec_time
        print "mem", base_mem, max_mem

        return exec_time, max_mem - base_mem

    def _mark_start(self):
        self.pipe_print("Starting test")
        time.sleep(5)
        self.__start_time = time.time()

    def _mark_end(self):
        self.pipe_print("Finishing test")
        total_time = time.time() - self.__start_time
        self.pipe_print("time:%s" % total_time)

    def _get_cursor(self):
        import MySQLdb
        from test_settings import DATABASES

        conn = MySQLdb.connect(
            host="localhost",
            user=DATABASES['default']['USER'],
            passwd=DATABASES['default']['PASSWORD'],
            db=DATABASES['default']['NAME']
        )
        
        return conn.cursor()


def r(len):
    import string
    return ''.join(random.choice(string.ascii_letters) for x in range(len))








