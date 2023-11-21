from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.core.validators import validate_email
from django.db.utils import IntegrityError
from django.http import HttpRequest

from apps.auth_jwt.api.schemas import TokenIn, TokenPair, UserIn, UserLogin
from apps.auth_jwt.models import RefreshToken
from apps.auth_jwt.services import generate_tokens, is_revoked_token
from apps.core.api.schemas import Message


def register_new_user(
    request: HttpRequest,
    user_data: UserIn,
) -> tuple[int, Message]:
    """Register new user in system."""
    try:
        validate_email(user_data.email)
    except exceptions.ValidationError:
        return 400, {"message": "Email not valid"}
    try:
        validate_password(user_data.password)
    except exceptions.ValidationError:
        return 400, {"message": "Password not valid"}

    try:
        user = get_user_model().objects.create(
            username=user_data.username,
            email=user_data.email,
        )
        user.set_password(user_data.password)
        user.save()
    except IntegrityError:
        return 422, {"message": "User is already exist"}

    return 201, {"message": "Successful registration"}


def login(
    request: HttpRequest,
    user_data: UserLogin,
) -> tuple[int, Message | TokenPair]:
    """Login user in system and give him token pair."""
    user = get_user_model().objects.filter(email=user_data.email).first()
    if user is None:
        return 404, {"message": "User with this email not found"}

    if not user.check_password(user_data.password):
        return 400, {"message": "Wrong password"}

    access_token, refresh_token = generate_tokens(user)
    return 200, {"access_token": access_token, "refresh_token": refresh_token}


def revoke_all_tokens(
    request: HttpRequest,
    token: TokenIn,
) -> tuple[int, Message | TokenPair]:
    """Revoke all exist tokens."""
    token_model = RefreshToken.objects.filter(jti=token.refresh_token).first()
    if token_model is None:
        return 400, {"message": "Token not exists"}

    RefreshToken.objects.filter(user=token_model.user).update(revoked=True)
    return 200, {"message": "Successful revoke"}


def logout(
    request: HttpRequest,
    token: TokenIn,
) -> tuple[int, Message | TokenPair]:
    """Logout user, revoke current token."""
    token_model = RefreshToken.objects.filter(jti=token.refresh_token).first()
    if token_model is None:
        return 400, {"message": "Token not exists"}

    token_model.revoked = True
    token_model.save()

    return 200, {"message": "Successful logout"}


def update_tokens(
    request: HttpRequest,
    token: TokenIn,
) -> tuple[int, Message | TokenPair]:
    """Update refresh tokens."""
    token_model = RefreshToken.objects.filter(jti=token.refresh_token).first()
    if token_model is None:
        return 400, {"message": "Token not exists"}

    if is_revoked_token(token_model):
        RefreshToken.objects.filter(user=token_model.user).update(revoked=True)
        return 400, {"message": "Token is revoked"}

    token_model.revoked = True
    token_model.save()

    access_token, refresh_token = generate_tokens(token_model.user)
    return 200, {"access_token": access_token, "refresh_token": refresh_token}
