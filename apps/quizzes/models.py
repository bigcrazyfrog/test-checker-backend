import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class Quiz(BaseModel):
    """Default model for task."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=60,
    )
    description = models.TextField(
        verbose_name=_("Description"),
    )
    author = models.ForeignKey(
        to="users.User",
        related_name="quizzes",
        verbose_name=_("Author"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None,
    )
    content = models.JSONField(
        verbose_name=_("Content"),
    )

    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quiz")

    def __repr__(self) -> str:
        return f"Student<{self.title}>"

    def __str__(self) -> str:
        return f"{self.title}"
