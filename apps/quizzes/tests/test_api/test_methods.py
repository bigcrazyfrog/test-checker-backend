import json

from django.test import TestCase

from apps.fixtures import AuthClient
from apps.quizzes.api.schemas import QuizOut
from apps.quizzes.factories import QuizFactory


class TestQuiz(TestCase):
    """Test quiz profile."""

    def setUp(self) -> None:
        self.client = AuthClient()
        self.quiz = QuizFactory(author=self.client.user)

    def test_get_all_quizzes(self) -> None:
        """Test get all quizzes."""
        response = self.client.get("/api/v1/quizzes/")

        json_data = response.json()[0]
        json_data.pop("id")
        correct_data = QuizOut.from_orm(self.quiz).dict()
        correct_data.pop("id")

        self.assertEqual(json_data, correct_data)

    def test_add_new_quiz(self) -> None:
        """Test add new qiuz."""
        data = {
            "title": "title",
            "description": "description",
            "content": {"content": "content"},
        }

        response = self.client.post(
            "/api/v1/quizzes/",
            json.dumps(data),
            content_type="application/json",
        )

        json_data = response.json()
        self.assertEqual(response.status_code, 201)
        for key, value in data.items():
            self.assertEqual(json_data[key], value)
