from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class quizzesAppConfig(AppConfig):
    """Default configuration for Tasks app."""

    name = "apps.quizzes"
    verbose_name = _("quizzes")

    def ready(self):
        # pylint: disable=unused-import
        import apps.quizzes.api.schemas  # noqa
