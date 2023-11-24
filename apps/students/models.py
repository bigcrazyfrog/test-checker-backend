import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class Student(BaseModel):
    """Default model for student."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    first_name = models.CharField(
        verbose_name=_("Firstname"),
        max_length=30,
    )
    last_name = models.CharField(
        verbose_name=_("Lastname"),
        max_length=30,
    )
    father_name = models.CharField(
        verbose_name=_("Fathername"),
        max_length=30,
        blank=True,
    )
    group = models.ForeignKey(
        to="groups.StudentGroup",
        related_name="students",
        verbose_name=_("Group"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
    )

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")

    def __repr__(self) -> str:
        return f"Student<{self.first_name} {self.last_name}>"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
