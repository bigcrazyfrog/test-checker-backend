import factory

from apps.users.factories import UserFactory

from . import models


class StudentGroupFactory(factory.django.DjangoModelFactory):
    """Factory to generate test student group instance."""

    teacher = factory.SubFactory(UserFactory)
    name = factory.Faker("name")

    class Meta:
        model = models.StudentGroup
