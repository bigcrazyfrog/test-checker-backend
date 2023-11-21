from django.test import Client, TestCase


class TestUserPermissions(TestCase):
    """Test user permissions."""

    def setUp(self) -> None:
        self.client = Client()

    def test_without_auth(self) -> None:
        """Test request without auth."""
        response = self.client.get("/api/v1/profile/me")
        self.assertEqual(response.status_code, 401)

        response = self.client.put("/api/v1/profile/settings")
        self.assertEqual(response.status_code, 401)
