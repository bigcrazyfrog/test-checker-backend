from django.contrib import admin

from apps.core.admin import BaseAdmin

from .models import StudentGroup


@admin.register(StudentGroup)
class StudentGroupAdmin(BaseAdmin):
    """UI for `StudentClass` model."""

    ordering = (
        "name",
    )
    list_display = (
        "name",
        "teacher",
    )
    search_fields = (
        "name",
    )
    readonly_fields = (
        "id",
    )
    fieldsets = (
        (
            None, {
                "fields": (
                    "id",
                    "name",
                    "teacher",
                ),
            },
        ),
    )
