from ninja import NinjaAPI, Router

import apps.auth_jwt.api.handlers as auth_handlers
from apps.auth_jwt.api.schemas import TokenPair
from apps.core.api.schemas import Message


def get_auth_router() -> Router:
    """Get auth user router."""
    router = Router(tags=["auth"])

    router.add_api_operation(
        "/register",
        ["POST"],
        auth_handlers.register_new_user,
        response={201: Message, 400: Message, 422: Message},
        auth=None,
    )

    router.add_api_operation(
        "/login",
        ["POST"],
        auth_handlers.login,
        response={200: TokenPair, 400: Message, 404: Message},
        auth=None,
    )

    router.add_api_operation(
        "/logout",
        ["DELETE"],
        auth_handlers.logout,
        response={200: Message, 400: Message},
        auth=None,
    )

    router.add_api_operation(
        "/update_tokens",
        ["PUT"],
        auth_handlers.update_tokens,
        response={200: TokenPair, 400: Message},
        auth=None,
    )

    router.add_api_operation(
        "/revoke_all_tokens",
        ["DELETE"],
        auth_handlers.revoke_all_tokens,
        response={200: Message, 400: Message},
        auth=None,
    )

    return router


def add_auth_router(api: NinjaAPI) -> NinjaAPI:
    """Add auth user router to REST API."""
    api.add_router("auth/", get_auth_router())
    return api
