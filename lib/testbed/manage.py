#!/usr/bin/env python

import os
import sys
from django.core.management import execute_manager


# use a default settings module if none was specified on the command line
DEFAULT_SETTINGS = 'testbed.local_settings'
settings_specified = any([arg.startswith('--settings=') for arg in sys.argv])
if not settings_specified and len(sys.argv) >= 2:
    print "NOTICE: using default settings module '%s'" % DEFAULT_SETTINGS
    sys.argv.append('--settings=%s' % DEFAULT_SETTINGS)


if __name__ == "__main__":
    # remove '.' from the path
    sys.path.pop(0)
    # add project directory to path
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    sys.path.insert(0, os.path.dirname(PROJECT_ROOT))
    
    try:
        import testbed.settings # Assumed to be in the same directory.
    except ImportError:
        import sys
        sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
        sys.exit(1)

    if __name__ == "__main__":
        execute_manager(testbed.settings)
