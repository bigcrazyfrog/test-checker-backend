import json

from django.test import TestCase

from faker import Faker

from apps.fixtures import AuthClient
from apps.groups.factories import StudentGroupFactory

fake = Faker()


class TestUserProfile(TestCase):
    """Test user profile."""

    def setUp(self) -> None:
        self.client = AuthClient()
        self.group = StudentGroupFactory()

    def test_add_new_group(self) -> None:
        """Test add new group."""
        name = fake.first_name()
        data = {"name": name}

        response = self.client.post(
            "/api/v1/groups/",
            json.dumps(data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], name)

    def test_get_group_info(self) -> None:
        """Test get group info."""
        client = AuthClient(self.group.teacher)
        response = client.get(f"/api/v1/groups/{str(self.group.id)}")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], self.group.name)

    def test_update_group(self) -> None:
        """Test update new group."""
        client = AuthClient(self.group.teacher)

        name = fake.first_name()
        data = {"name": name}

        response = client.put(
            f"/api/v1/groups/{str(self.group.id)}",
            json.dumps(data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], name)
