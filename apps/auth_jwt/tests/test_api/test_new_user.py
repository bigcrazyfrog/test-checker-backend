import json

from django.test import Client, TestCase

from faker import Faker

fake = Faker()


class TestNewUser(TestCase):
    """Test user module."""

    def setUp(self) -> None:
        self.client = Client()

    def get_data(self) -> dict[str, str]:
        return {
            "username": fake.first_name(),
            "email": fake.email(),
            "password": fake.password(),
        }

    def test_without_auth(self) -> None:
        """Test request without auth."""
        response = self.client.post(
            "/api/v1/auth/register",
            json.dumps(self.get_data()),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)

    def test_unique_email(self) -> None:
        """Test request without auth."""
        data = self.get_data()
        other_data = self.get_data().update(email=data["email"])

        response = self.client.post(
            "/api/v1/auth/register",
            json.dumps(data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)

        response = self.client.post(
            "/api/v1/auth/register",
            json.dumps(other_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 422)
