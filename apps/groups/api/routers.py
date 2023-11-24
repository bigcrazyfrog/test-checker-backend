from ninja import NinjaAPI, Router

import apps.groups.api.handlers as group_handlers
from apps.core.api.schemas import Message
from apps.groups.api.schemas import GroupOut


def get_student_groups_router() -> Router:
    """Get student groups router."""
    router = Router(tags=["student groups"])

    router.add_api_operation(
        "/",
        ["GET"],
        group_handlers.all,
        response={200: list[GroupOut], 400: Message},
    )

    router.add_api_operation(
        "/",
        ["POST"],
        group_handlers.add,
        response={200: GroupOut, 400: Message},
    )

    router.add_api_operation(
        "/{id}",
        ["GET"],
        group_handlers.get,
        response={200: GroupOut, 400: Message, 404: Message},
    )

    router.add_api_operation(
        "/{id}",
        ["PUT"],
        group_handlers.update,
        response={200: GroupOut, 400: Message, 404: Message},
    )

    router.add_api_operation(
        "/{id}",
        ["DELETE"],
        group_handlers.remove,
        response={200: Message, 400: Message, 404: Message},
    )

    return router


def add_student_groups_router(api: NinjaAPI) -> NinjaAPI:
    """Add students router to REST API."""
    api.add_router("groups/", get_student_groups_router())
    return api
