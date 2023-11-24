from ninja import ModelSchema

from ..models import Student


class StudentAdd(ModelSchema):
    """Schema for new Student."""

    class Meta:
        model = Student
        fields = ["first_name", "last_name", "father_name"]


class StudentOut(ModelSchema):
    """Schema for output Student."""

    class Meta:
        model = Student
        fields = ["id", "first_name", "last_name", "father_name"]
