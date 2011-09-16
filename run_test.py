import sys
import commands

file_param = sys.argv[1]
method_param = sys.argv[2]
klass_param = sys.argv[3]

module = __import__(file_param, fromlist=[klass_param])
klass = getattr(module, klass_param)

instance = klass()
method = getattr(instance, method_param)


#from django.conf import settings
#from django.db import transaction
#from django.db import connection

#method = transaction.commit_manually(method)

"""
if "orm" in method_param:
    from django.db import transaction
    method = transaction.commit_manually(method)
"""

method()