from ninja import ModelSchema

from ..models import StudentGroup


class GroupAdd(ModelSchema):
    """Schema for new group."""

    class Meta:
        model = StudentGroup
        fields = ["name"]


class GroupOut(ModelSchema):
    """Schema for output group."""

    class Meta:
        model = StudentGroup
        fields = ["id", "name"]


class GroupRemove(ModelSchema):
    """Schema for group removing contains only `id` field."""

    class Meta:
        model = StudentGroup
        fields = ["id"]
