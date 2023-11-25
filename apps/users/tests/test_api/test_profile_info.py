import json

from django.test import TestCase

from faker import Faker

from apps.fixtures import AuthClient
from apps.users.api.schemas import UserOut
from apps.users.models import User

fake = Faker()


class TestUserProfile(TestCase):
    """Test user profile."""

    def setUp(self) -> None:
        self.auth_client = AuthClient()

    def test_get_user_info(self) -> None:
        """Test request without auth."""
        response = self.auth_client.get("/api/v1/profile/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            UserOut.from_orm(self.auth_client.user).dict(),
        )

    def test_update_user_info(self) -> None:
        """Test request without auth."""
        data = {"first_name": fake.first_name()}
        response = self.auth_client.put(
            "/api/v1/profile/",
            json.dumps(data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            User.objects.filter(
                id=self.auth_client.user.id,
            ).values("username", "email", "first_name", "last_name").first(),
        )
