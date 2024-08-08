import os
from pathlib import Path

# Path to the settings file
settings_path = '/home/dwp/cras/Extraction/settings.py'

# Read the settings file
with open(settings_path, 'r') as file:
    content = file.read()

# Print the content of the settings file
print(content)

# Extract paths from the settings
BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

print("BASE_DIR:", BASE_DIR)
print("MEDIA_ROOT:", MEDIA_ROOT)
print("STATIC_ROOT:", STATIC_ROOT)
for path in STATICFILES_DIRS:
    print("STATICFILES_DIR:", path)

