from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersAppConfig(AppConfig):
    """Default configuration for Groups app."""

    name = "apps.groups"
    verbose_name = _("Groups")

    def ready(self):
        # pylint: disable=unused-import
        import apps.groups.api.schemas  # noqa
