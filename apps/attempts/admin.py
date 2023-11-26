from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.core.admin import ReadOnlyAdmin

from .models import Attempt


@admin.register(Attempt)
class AttemptAdmin(ReadOnlyAdmin):
    """UI for `Attempt` model."""

    ordering = (
        "quiz",
    )
    list_display = (
        "quiz",
        "student",
        "quiz",
        "student",
    )
    search_fields = (
        "result",
        "answers",
    )
    readonly_fields = (
        "id",
        "quiz",
        "student",
        "result",
        "answers",
    )
    fieldsets = (
        (
            None, {
                "fields": (
                    "id",
                    "quiz",
                    "student",
                ),
            },
        ),
        (
            _("Results"), {
                "fields": (
                    "result",
                    "answers",
                ),
            },
        ),
    )
