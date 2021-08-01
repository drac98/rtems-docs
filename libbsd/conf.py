import sys, os
sys.path.insert(0, os.path.abspath('../common/'))

from conf import *

project = "RTEMS LibBSD User Manual"

latex_documents = [
    ('index',
     'libbsd.tex',
     u'RTEMS LibBSD User Manual',
     u'RTEMS Documentation Project',
     'manual'),
]
