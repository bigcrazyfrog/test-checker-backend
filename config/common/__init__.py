# -----------------------------------------------------------------------------
# General Django Configuration Starts Here
# -----------------------------------------------------------------------------
from .authentication import *
from .databases import *
from .installed_apps import *
from .internationalization import *
from .logging import *
from .middleware import *
from .storage import *
from .templates import *

# -----------------------------------------------------------------------------
# Business Logic Custom Variables and Settings
# -----------------------------------------------------------------------------
from .business_logic import *

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

# Custom settings
APP_LABEL = "TestChecker"
