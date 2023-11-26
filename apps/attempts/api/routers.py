from ninja import NinjaAPI, Router

import apps.attempts.api.handlers as attempt_handlers
from apps.attempts.api.schemas import AttemptOut
from apps.core.api.schemas import Message


def get_attempts_router() -> Router:
    """Get student attempts router."""
    router = Router(tags=["attempts"])

    router.add_api_operation(
        "/",
        ["GET"],
        attempt_handlers.all,
        response={200: list[AttemptOut], 400: Message},
    )

    router.add_api_operation(
        "/",
        ["POST"],
        attempt_handlers.add,
        response={200: AttemptOut, 400: Message, 404: Message},
    )

    router.add_api_operation(
        "/{attempt_id}",
        ["GET"],
        attempt_handlers.get,
        response={200: AttemptOut, 400: Message, 404: Message},
    )

    return router


def add_attempts_router(api: NinjaAPI) -> NinjaAPI:
    """Add attempts router to REST API."""
    api.add_router("attempts/", get_attempts_router())
    return api
