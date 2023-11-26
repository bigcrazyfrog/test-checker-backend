from django.test import TestCase

from apps.fixtures import AuthClient


class TestAttemptMethods(TestCase):
    """Test API methods from attempt app."""

    def setUp(self) -> None:
        self.client = AuthClient()

    def test_get_all_group_with_error(self) -> None:
        """Test get all groups."""
        response = self.client.get("/api/v1/attempts/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])
