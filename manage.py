#!/usr/bin/env python
import os
import sys
sys.path.append('/private/var/mobile/Containers/Shared/AppGroup/B8CAB6C6-1790-4404-B2BA-762A372C1D98/Pythonista3/Documents/djcode/mysite/')

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

