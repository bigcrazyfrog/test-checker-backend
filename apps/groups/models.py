import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class StudentGroup(BaseModel):
    """Default model for school class."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=30,
    )
    teacher = models.ForeignKey(
        to="users.User",
        related_name="classes",
        verbose_name=_("Teacher"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
    )

    class Meta:
        verbose_name = _("Student Group")
        verbose_name_plural = _("Student Groups")

    def __repr__(self) -> str:
        return f"Group<{self.name}>"

    def __str__(self) -> str:
        return self.name
