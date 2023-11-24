from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.core.admin import BaseAdmin

from .models import Quiz


@admin.register(Quiz)
class QuizAdmin(BaseAdmin):
    """UI for `Quiz` model."""

    ordering = (
        "title",
    )
    list_display = (
        "title",
        "author",
    )
    search_fields = (
        "title",
        "author",
    )
    readonly_fields = (
        "id",
    )
    fieldsets = (
        (
            None, {
                "fields": (
                    "id",
                    "title",
                    "description",
                ),
            },
        ),
        (
            _("Permission"),
            {
                "fields": (
                    "author",
                ),
            },
        ),
        (
            _("Content"),
            {
                "fields": (
                    "content",
                ),
            },
        ),
    )
