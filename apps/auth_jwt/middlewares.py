from django.contrib.auth import get_user_model
from django.http import HttpRequest

from ninja.security import HttpBearer

from apps.auth_jwt.services import get_user_id_from_token


class HTTPJWTAuth(HttpBearer):
    """Authentication middleware for REST API."""

    def __init__(self):
        super().__init__()

    def authenticate(self, request: HttpRequest, token: str) -> str | None:
        """Add User to request."""
        user_id = get_user_id_from_token(token)
        if user_id is None:
            return None

        user = get_user_model().objects.filter(id=user_id).first()
        if user is None:
            return None

        request.user = user
        return token
