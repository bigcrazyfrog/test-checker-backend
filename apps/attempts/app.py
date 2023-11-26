from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AttemptAppConfig(AppConfig):
    """Default configuration for attempts app."""

    name = "apps.attempts"
    verbose_name = _("Attempts")

    def ready(self):
        # pylint: disable=unused-import
        import apps.attempts.api.schemas  # noqa
