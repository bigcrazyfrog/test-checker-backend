from datetime import datetime

import jwt

from config.settings import (
    JWT_ACCESS_SECRET,
    JWT_ACCESS_TOKEN_LIFETIME,
    JWT_REFRESH_SECRET,
    JWT_REFRESH_TOKEN_LIFETIME,
)

from apps.users.models import User

from .models import RefreshToken


def is_revoked_token(token: RefreshToken) -> bool:
    """Check if token is revoked."""
    if token.revoked:
        return True

    try:
        payload = jwt.decode(
            token.jti,
            JWT_REFRESH_SECRET,
            algorithms=["HS256"],
        )
    except (
        jwt.exceptions.ExpiredSignatureError,
        jwt.exceptions.DecodeError,
    ):
        return True

    date = datetime.strptime(payload["date"], "%Y-%m-%d %H:%M:%S.%f")
    print(date < datetime.now())


def get_user_id_from_token(token: str) -> str | None:
    """Valid access token."""
    try:
        payload = jwt.decode(token, JWT_ACCESS_SECRET, algorithms=["HS256"])
    except (
        jwt.exceptions.ExpiredSignatureError,
        jwt.exceptions.DecodeError,
    ):
        return None

    date = datetime.strptime(payload["date"], "%Y-%m-%d %H:%M:%S.%f")
    if date < datetime.now():
        return None

    return payload["id"]


def generate_tokens(user: User) -> tuple[str, str]:
    """Generate a pair of tokens for user."""
    access_token = _generate_access_token(user.id)
    refresh_token = _generate_refresh_token(user.id)

    RefreshToken.objects.create(jti=refresh_token, user=user)

    return access_token, refresh_token


def _generate_access_token(user_id: str) -> str:
    date = str(datetime.now() + JWT_ACCESS_TOKEN_LIFETIME)
    payload = {"id": str(user_id), "admin": False, "date": date}

    return jwt.encode(payload, JWT_ACCESS_SECRET, algorithm="HS256")


def _generate_refresh_token(user_id: str) -> str:
    date = str(datetime.now() + JWT_REFRESH_TOKEN_LIFETIME)
    payload = {"id": str(user_id), "date": date}

    return jwt.encode(payload, JWT_REFRESH_SECRET, algorithm="HS256")
