import factory

from apps.users.factories import UserFactory

from . import models


class QuizFactory(factory.django.DjangoModelFactory):
    """Factory to generate test quiz instance."""

    author = factory.SubFactory(UserFactory)
    title = factory.Faker("name")
    description = factory.Faker("text")
    content = {"some_content": "text"}

    class Meta:
        model = models.Quiz
