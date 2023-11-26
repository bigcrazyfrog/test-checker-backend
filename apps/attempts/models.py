import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel


class Attempt(BaseModel):
    """Default model for test attempts."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    quiz = models.ForeignKey(
        to="quizzes.Quiz",
        related_name="attempts",
        verbose_name=_("Attempt"),
        on_delete=models.CASCADE,
    )
    student = models.ForeignKey(
        to="students.Student",
        related_name="attempts",
        verbose_name=_("Student"),
        on_delete=models.CASCADE,
    )
    result = models.IntegerField(
        verbose_name=_("Result"),
        blank=True,
        null=True,
        default=None,
    )
    answers = models.CharField(
        verbose_name=_("Answers"),
        max_length=30,
        blank=True,
    )

    class Meta:
        verbose_name = _("Attempt")
        verbose_name_plural = _("Attempts")

    def __repr__(self) -> str:
        return f"Attempt<{self.id}>"

    def __str__(self) -> str:
        return self.name
