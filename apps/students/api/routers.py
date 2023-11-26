from ninja import NinjaAPI, Router

import apps.students.api.handlers as student_handlers
from apps.core.api.schemas import Message
from apps.students.api.schemas import StudentOut


def get_students_router() -> Router:
    """Get students router."""
    router = Router(tags=["students"])

    router.add_api_operation(
        "/",
        ["GET"],
        student_handlers.all,
        response={200: list[StudentOut], 400: Message},
    )

    router.add_api_operation(
        "/",
        ["POST"],
        student_handlers.add,
        response={201: StudentOut, 400: Message},
    )

    router.add_api_operation(
        "/{student_id}",
        ["GET"],
        student_handlers.get,
        response={200: StudentOut, 400: Message, 404: Message},
    )

    router.add_api_operation(
        "/{student_id}",
        ["PUT"],
        student_handlers.update,
        response={200: StudentOut, 400: Message, 404: Message},
    )

    router.add_api_operation(
        "/{student_id}",
        ["DELETE"],
        student_handlers.delete,
        response={200: Message, 400: Message, 404: Message},
    )

    return router


def add_students_router(api: NinjaAPI) -> NinjaAPI:
    """Add students router to REST API."""
    api.add_router("groups/{group_id}/students/", get_students_router())
    return api
