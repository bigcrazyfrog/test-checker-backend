from django.http import HttpRequest

from apps.attempts.api.schemas import AttemptAdd, AttemptOut
from apps.core.api.schemas import Message
from apps.quizzes.models import Quiz
from apps.students.models import Student

from ..models import Attempt


def all(
    request: HttpRequest,
    student: str | None = None,
    group: str | None = None,
    quiz: str | None = None,
) -> tuple[int, Message | AttemptOut]:
    """Get a list of all existing attempt."""
    filters = {
        "quiz__author": request.user,
        "student__group__teacher": request.user,
    }
    if student:
        filters["student"] = student
    if group:
        filters["group"] = group
    if quiz:
        filters["quiz"] = quiz

    attempts = Attempt.objects.select_related(
        "student",
        "student__group",
        "quiz",
    ).filter(**filters)

    return 200, list(attempts)


def add(
    request: HttpRequest,
    attemps_data: AttemptAdd,
) -> tuple[int, Message | AttemptOut]:
    """Add new attempt to database."""
    student = Student.objects.filter(id=attemps_data.student).first()
    if student is None:
        return 404, {"message": "Student not found"}

    quiz = Quiz.objects.filter(id=attemps_data.quiz).first()
    if quiz is None:
        return 404, {"message": "Quiz not found"}

    attempt = Attempt.objects.create(
        student=student,
        quiz=quiz,
        result=attemps_data.result,
        answers=attemps_data.answers,
    )
    return 201, attempt


def get(
    request: HttpRequest,
    attempt_id: str,
) -> tuple[int, Message | AttemptOut]:
    """Get existing attempt."""
    attempt = Attempt.objects.filter(
        id=attempt_id,
        quiz__author=request.user,
        student__group__teacher=request.user,
    ).first()
    if attempt is None:
        return 404, {"message": "Attempt not found"}

    return 200, attempt
