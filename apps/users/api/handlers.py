from django.http import HttpRequest

from apps.core.api.schemas import Message
from apps.users.api.schemas import UserOut, UserUpdate


def me(request: HttpRequest) -> tuple[int, Message | UserOut]:
    """Get general user info."""
    response = {
        "username": request.user.username,
        "email": request.user.email,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
    }

    return 200, response


def settings(
    request: HttpRequest,
    user_data: UserUpdate,
) -> tuple[int, Message]:
    """Update user fields."""
    if user_data.first_name is not None:
        request.user.first_name = user_data.first_name
    if user_data.last_name is not None:
        request.user.last_name = user_data.last_name

    request.user.save()
    return 200, {"message": "Succesfull update"}
