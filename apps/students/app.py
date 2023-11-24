from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StudentsAppConfig(AppConfig):
    """Default configuration for Students app."""

    name = "apps.students"
    verbose_name = _("Students")

    def ready(self):
        # pylint: disable=unused-import
        import apps.students.api.schemas  # noqa
