from django.http import HttpRequest, HttpResponse

from ninja import NinjaAPI

from apps.auth_jwt.api.routers import add_auth_router
from apps.auth_jwt.middlewares import HTTPJWTAuth
from apps.groups.api.routers import add_student_groups_router
from apps.users.api.routers import add_users_router


def get_api() -> NinjaAPI:
    """Assembly point of general API."""
    auth = [HTTPJWTAuth()]

    api = NinjaAPI(
        title="TEST.CHECKER.BACKEND",
        version="1.0.0",
        auth=auth,
    )

    add_auth_router(api=api)
    add_users_router(api=api)
    add_student_groups_router(api=api)

    return api


# General NinjaAPI object using as REST API
ninja_api = get_api()


@ninja_api.exception_handler(Exception)
def exception_handler(request: HttpRequest, exc) -> HttpResponse:
    """Handler for unexpected error."""
    return ninja_api.create_response(
        request,
        {"message": str(exc)},
        status=400,
    )
