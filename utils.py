import pycha.bar
import cairo
import commands
from dbconfig import *

def db_prep():
    #return
    if DATABASE_ENGINE == 'mysql':
        status, output = commands.getstatusoutput('service mysql restart')
        print output
    return
    print "warming db by performing 10 000 select requests"
    status, output = commands.getstatusoutput('python warmup.py')
    print output


def graph(lines, output, type, command):

    info = { "mem" : "Memory (mb)", "time" : "Time (sec)"}
    colors = { "mem" : "blue", "time" : "red"}

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 550, 300)

    dataSet = (
        ('lines', [(i, l[1]) for i, l in enumerate(lines)]),
        )

    options = {
        'axis': {
            'x': {
                'ticks': [dict(v=i, label=l[0]) for i, l in enumerate(lines)],
                'label': 'Tests',
                'rotate': 0,
            },
            'y': {
                'tickCount': 10,
                'rotate': 35,
                'label': info[type]
            }
        },
        'background': {
            'chartColor': '#ffeeff',
            'baseColor': '#ffffff',
            'lineColor': '#444444'
        },
        'colorScheme': {
            'name': 'gradient',
            'args': {
                'initialColor': colors[type],
            },
        },
        'legend': {
            'hide': True,
        },
        'padding': {
            'left': 130,
            'bottom': 75,
        },
        'title': '%s ORM vs SQL' % command
    }
    chart = pycha.bar.HorizontalBarChart(surface, options)

    chart.addDataset(dataSet)
    chart.render()

    surface.write_to_png(output)