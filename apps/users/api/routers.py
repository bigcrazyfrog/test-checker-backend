from ninja import NinjaAPI, Router

import apps.users.api.handlers as user_handlers
from apps.core.api.schemas import Message
from apps.users.api.schemas import UserOut


def get_users_router() -> Router:
    """Get auth user router."""
    router = Router(tags=["users"])

    router.add_api_operation(
        "/",
        ["GET"],
        user_handlers.me,
        response={200: UserOut, 400: Message},
    )

    router.add_api_operation(
        "/",
        ["PUT"],
        user_handlers.update,
        response={200: UserOut, 400: Message},
    )

    return router


def add_users_router(api: NinjaAPI) -> NinjaAPI:
    """Add auth user router to REST API."""
    api.add_router("profile/", get_users_router())
    return api
