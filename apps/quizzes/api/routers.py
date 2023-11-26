from ninja import NinjaAPI, Router

import apps.quizzes.api.handlers as quiz_handlers
from apps.core.api.schemas import Message
from apps.quizzes.api.schemas import QuizOut


def get_quizzes_router() -> Router:
    """Get quizzes router."""
    router = Router(tags=["quizzes"])

    router.add_api_operation(
        "/",
        ["GET"],
        quiz_handlers.all,
        response={200: list[QuizOut], 400: Message},
    )

    router.add_api_operation(
        "/",
        ["POST"],
        quiz_handlers.add,
        response={201: QuizOut, 400: Message},
    )

    router.add_api_operation(
        "/{quiz_id}",
        ["GET"],
        quiz_handlers.get,
        response={200: QuizOut, 400: Message, 404: Message},
    )

    router.add_api_operation(
        "/{quiz_id}",
        ["PUT"],
        quiz_handlers.update,
        response={200: QuizOut, 400: Message, 404: Message},
    )

    router.add_api_operation(
        "/{quiz_id}",
        ["DELETE"],
        quiz_handlers.delete,
        response={200: Message, 400: Message, 404: Message},
    )

    return router


def add_quizzes_router(api: NinjaAPI) -> NinjaAPI:
    """Add quizzes router to REST API."""
    api.add_router("quizzes/", get_quizzes_router())
    return api
