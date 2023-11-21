from django.db.utils import IntegrityError
from django.test import TestCase

from faker import Faker

from apps.users.factories import UserFactory
from apps.users.models import User

fake = Faker()


class TestUserModel(TestCase):
    """Test user model."""

    def setUp(self) -> None:
        self.user = UserFactory()

    def test_unique_email(self) -> None:
        """Test unique email."""
        with self.assertRaises(IntegrityError):
            User.objects.create(
                username=fake.first_name(),
                email=self.user.email,
                password=fake.password(),
            )
