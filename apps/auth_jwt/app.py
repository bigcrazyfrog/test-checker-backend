from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AuthAppConfig(AppConfig):
    """Default configuration for Users app."""

    name = "apps.auth_jwt"
    verbose_name = _("Auth")

    def ready(self):
        # pylint: disable=unused-import
        import apps.auth_jwt.api.schemas  # noqa