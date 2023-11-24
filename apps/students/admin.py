from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.core.admin import BaseAdmin

from .models import Student


@admin.register(Student)
class StudentAdmin(BaseAdmin):
    """UI for `Student` model."""

    ordering = (
        "last_name",
    )
    list_display = (
        "first_name",
        "last_name",
        "father_name",
        "group",
    )
    search_fields = (
        "last_name",
        "group",
    )
    readonly_fields = (
        "id",
    )
    fieldsets = (
        (
            None, {
                "fields": (
                    "id",
                    "group",
                ),
            },
        ),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "father_name",
                ),
            },
        ),
    )
