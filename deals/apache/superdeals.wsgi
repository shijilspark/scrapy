import os
import sys
import djcelery
djcelery.setup_loader()

path = '/home/ubuntu'
if path not in sys.path:
 sys.path.insert(0, '/home/ubuntu/superdeals/deals')
os.environ['DJANGO_SETTINGS_MODULE'] = 'deals.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
