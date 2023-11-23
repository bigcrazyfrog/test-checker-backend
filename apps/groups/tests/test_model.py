from django.db.utils import DataError
from django.test import TestCase

from faker import Faker

from apps.groups.models import StudentGroup
from apps.users.factories import UserFactory

fake = Faker()


class TestStudentGroupModel(TestCase):
    """Test user model."""

    def setUp(self) -> None:
        self.user = UserFactory()

    def test_valid_name_max_length(self) -> None:
        """Test unique email."""
        with self.assertRaises(DataError):
            StudentGroup.objects.create(
                name="a" * 31,
                teacher=self.user,
            )
