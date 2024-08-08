import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Extraction.settings')
import django
django.setup()

print("BASE_DIR:", settings.BASE_DIR)
print("STATIC_URL:", settings.STATIC_URL)
print("STATIC_ROOT:", settings.STATIC_ROOT)
for directory in settings.STATICFILES_DIRS:
    print("STATICFILES_DIR:", directory)

