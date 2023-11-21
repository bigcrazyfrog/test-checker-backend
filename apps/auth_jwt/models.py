from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class RefreshToken(models.Model):
    """Refresh token model."""

    jti = models.CharField(
        verbose_name=_("JTI"),
        max_length=255,
        primary_key=True,
    )
    user = models.ForeignKey(
        to=get_user_model(),
        verbose_name=_("User"),
        related_name="refresh_token",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        verbose_name=_("Creation date"),
        auto_now_add=True,
    )
    revoked = models.BooleanField(
        verbose_name=_("Is revoked"),
        default=False,
    )

    class Meta:
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    def __str__(self) -> str:
        return f"{self.user}"
