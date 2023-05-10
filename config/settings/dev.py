from .base import *

DJANGO_APPS.extend(
    [
        "django_extensions",
    ]
)

INSTALLED_APPS = DJANGO_APPS + THIRD_APPS + LOCAL_APPS
