from django.http import HttpRequest

from apps.core.api.schemas import Message
from apps.quizzes.api.schemas import QuizAdd, QuizOut
from apps.quizzes.models import Quiz


def all(
    request: HttpRequest,
) -> tuple[int, Message | QuizOut]:
    """Get a list of all existing quizzes."""
    quizzes = Quiz.objects.filter(author=request.user)
    return 200, list(quizzes)


def add(
    request: HttpRequest,
    quiz_data: QuizAdd,
) -> tuple[int, Message | list[QuizOut]]:
    """Add new quiz to database."""
    quiz = Quiz.objects.create(
        title=quiz_data.title,
        description=quiz_data.description,
        content=quiz_data.content,
        author=request.user,
    )
    return 200, quiz


def get(
    request: HttpRequest,
    quiz_id: str,
) -> tuple[int, Message | QuizOut]:
    """Get existing quiz."""
    quiz = Quiz.objects.filter(
        id=quiz_id,
        author=request.user,
    ).first()
    if quiz is None:
        return 404, {"message": "Quiz not found"}

    return 200, quiz


def update(
    request: HttpRequest,
    quiz_id: str,
    quiz_data: QuizAdd,
) -> tuple[int, Message | QuizOut]:
    """Update existing quiz fields."""
    quiz = Quiz.objects.filter(
        id=quiz_id,
        author=request.user,
    ).first()
    if quiz is None:
        return 404, {"message": "Quiz not found"}

    quiz.title = quiz_data.title
    quiz.description = quiz_data.description
    quiz.content = quiz_data.content
    quiz.save()

    return 200, quiz


def delete(
    request: HttpRequest,
    quiz_id: str,
) -> tuple[int, Message | QuizOut]:
    """Delete quiz from database."""
    quiz = Quiz.objects.filter(
        id=quiz_id,
        author=request.user,
    ).first()
    if quiz is None:
        return 404, {"message": "Quiz not found"}

    quiz.delete()
    return 200, {"message": "Successful delete"}
