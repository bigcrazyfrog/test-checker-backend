from django.http import HttpRequest

from apps.core.api.schemas import Message
from apps.groups.api.schemas import GroupAdd, GroupOut

from ..models import StudentGroup


def all(
    request: HttpRequest,
) -> tuple[int, Message | GroupOut]:
    """Get a list of all existing group."""
    group = StudentGroup.objects.filter(teacher=request.user)
    return 200, list(group)


def add(
    request: HttpRequest,
    group_data: GroupAdd,
) -> tuple[int, Message | list[GroupOut]]:
    """Add new group to database."""
    groups = StudentGroup.objects.create(
        name=group_data.name,
        teacher=request.user,
    )
    return 201, groups


def get(
    request: HttpRequest,
    group_id: str,
) -> tuple[int, Message | GroupOut]:
    """Get existing group."""
    group = StudentGroup.objects.filter(
        teacher=request.user,
        id=group_id,
    ).first()
    if group is None:
        return 404, {"message": "Group not found"}

    return 200, group


def update(
    request: HttpRequest,
    group_id: str,
    group_data: GroupAdd,
) -> tuple[int, Message | GroupOut]:
    """Update group fields."""
    group = StudentGroup.objects.filter(
        teacher=request.user,
        id=group_id,
    ).first()

    if group is None:
        return 404, {"message": "Group not found"}

    group.name = group_data.name
    group.save()
    return 200, group


def delete(
    request: HttpRequest,
    group_id: str,
) -> tuple[int, Message | GroupOut]:
    """Remove group from database."""
    group = StudentGroup.objects.filter(
        teacher=request.user,
        id=group_id,
    ).first()

    if group is None:
        return 404, {"message": "Group not found"}

    group.delete()
    return 200, {"message": "Group was removed"}
