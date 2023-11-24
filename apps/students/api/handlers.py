from django.http import HttpRequest

from apps.core.api.schemas import Message
from apps.groups.models import StudentGroup
from apps.students.api.schemas import StudentAdd, StudentOut

from ..models import Student


def all(
    request: HttpRequest,
    group_id: str,
) -> tuple[int, Message | StudentOut]:
    """Get a list of all existing students."""
    students = Student.objects.filter(group__id=group_id)
    return 200, list(students)


def add(
    request: HttpRequest,
    group_id: str,
    student_data: StudentAdd,
) -> tuple[int, Message | list[StudentOut]]:
    """Add new student to database."""
    group = StudentGroup.objects.filter(
        id=group_id,
        teacher=request.user,
    ).first()
    if group is None:
        return 404, {"message": "Group not found"}

    student = Student.objects.create(
        first_name=student_data.first_name,
        last_name=student_data.last_name,
        father_name=student_data.father_name,
        group=group,
    )
    return 200, student


def get(
    request: HttpRequest,
    group_id: str,
    student_id: str,
) -> tuple[int, Message | StudentOut]:
    """Get existing student."""
    student = Student.objects.filter(
        id=student_id,
        group__id=group_id,
        group__teacher=request.user,
    ).select_related("group").first()
    if student is None:
        return 404, {"message": "Student not found"}

    return 200, student


def update(
    request: HttpRequest,
    group_id: str,
    student_id: str,
    student_data: StudentAdd,
) -> tuple[int, Message | StudentOut]:
    """Update existing student fields."""
    student = Student.objects.filter(
        id=student_id,
        group__id=group_id,
        group__teacher=request.user,
    ).select_related("group").first()
    if student is None:
        return 404, {"message": "Student not found"}

    student.first_name = student_data.first_name
    student.last_name = student_data.last_name
    student.father_name = student_data.father_name
    student.save()

    return 200, student


def delete(
    request: HttpRequest,
    group_id: str,
    student_id: str,
) -> tuple[int, Message | StudentOut]:
    """Delete student from database."""
    student = Student.objects.filter(
        id=student_id,
        group__id=group_id,
        group__teacher=request.user,
    ).select_related("group").first()
    if student is None:
        return 404, {"message": "Student not found"}

    student.delete()
    return 200, {"message": "Successful delete"}
