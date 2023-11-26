from django.test import Client

from faker import Faker

from apps.auth_jwt.services import generate_tokens
from apps.users.factories import UserFactory
from apps.users.models import User

fake = Faker()


class AuthClient(Client):
    """Auth client for testing purposes."""

    def __init__(
        self,
        user: User | None = None,
        enforce_csrf_checks=False,
        raise_request_exception=True,
        *,
        headers=None,
        **defaults,
    ):
        self.user = user or UserFactory()
        self.tokens = generate_tokens(self.user)

        headers = {"Authorization": f"Bearer {self.tokens[0]}"}
        super().__init__(headers=headers, **defaults)
