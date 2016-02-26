'''
Handles Django settings for timetracker project.

All actual settings should be set in either:
- settings_local (for settings that only apply to that particular installation
- settings_base (for all other settings)

This creates a SECRET_KEY if necessary, 
then imports settings from settings_local if it exists,
and settings_base otherwise.

If settings_local.py exists it should begin with:

from settings_base import *

and change whatever settings are necessary for that particular installation.
'''

import os

try:
    from .secret_key import SECRET_KEY
except ImportError:
    
    def generate_secret_key(keyfilepath):
        from django.utils.crypto import get_random_string

        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = get_random_string(50, chars)
        with open(keyfilepath, 'w') as keyfile:
            keyline = 'SECRET_KEY = "{0}"\n'.format(key)
            keyfile.write(keyline)
    
    SETTINGS_DIR=os.path.abspath(os.path.dirname(__file__))
    generate_secret_key(os.path.join(SETTINGS_DIR, 'secret_key.py'))
    from .secret_key import SECRET_KEY

try:
    from .settings_local import *
except ImportError:
    from .settings_base import *
