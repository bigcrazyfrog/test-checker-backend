from django.forms import ValidationError
from django.http import HttpRequest, HttpResponse

from ninja import NinjaAPI

from config.settings import DEBUG

from apps.attempts.api.routers import add_attempts_router
from apps.auth_jwt.api.routers import add_auth_router
from apps.auth_jwt.middlewares import HTTPJWTAuth
from apps.groups.api.routers import add_student_groups_router
from apps.quizzes.api.routers import add_quizzes_router
from apps.students.api.routers import add_students_router
from apps.users.api.routers import add_users_router


def get_api() -> NinjaAPI:
    """Assembly point of general API."""
    auth = [HTTPJWTAuth()]

    api = NinjaAPI(
        title="TEST.CHECKER.BACKEND",
        version="1.0.0",
        description="The best API",
        auth=auth,
    )

    add_auth_router(api=api)
    add_users_router(api=api)
    add_student_groups_router(api=api)
    add_students_router(api=api)
    add_quizzes_router(api=api)
    add_attempts_router(api=api)

    return api


# General NinjaAPI object using as REST API
ninja_api = get_api()


@ninja_api.exception_handler(ValidationError)
def validation_error_handler(request: HttpRequest, exc) -> HttpResponse:
    """Handler for unexpected `ValidationError`."""
    return ninja_api.create_response(
        request,
        {"message": str(exc) if DEBUG else "Data is not valid"},
        status=422,
    )


@ninja_api.exception_handler(Exception)
def exception_handler(request: HttpRequest, exc) -> HttpResponse:
    """Handler for unexpected error."""
    return ninja_api.create_response(
        request,
        {"message": str(exc) if DEBUG else "Unexpected error"},
        status=500,
    )
