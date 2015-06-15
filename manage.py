#!/usr/bin/env python
import os
import sys

sys.path.append('/usr/lib/python2.6/site-packages')
sys.path.append('/usr/lib/python2.6/site-packages/django/db/backends/sqlite3')

print sys.path

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djproject.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
