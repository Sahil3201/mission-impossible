"""
    data = [('<username>','<password>'),]
"""

data = [
    ['10000101', 'PV42723G'],
    ['10000102', 'MP16177E'],
    ['10000103', 'WL40274F'],
    ['10000104', 'MN57832L'],
    ['10000105', 'DQ86215X'],
    ['10000106', 'PW87779R'],
]

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','que.settings')

import django
django.setup()

from quiz.models import Student

def populate_login_data(data):
    for d in data:
        usrnm = d[0]
        psswrd = d[1]

        entry = Student(username=usrnm)
        entry.set_password(psswrd)
        entry.save()

populate_login_data(data)
print('Done')