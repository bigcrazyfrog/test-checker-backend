from ninja import ModelSchema

from ..models import Attempt


class AttemptAdd(ModelSchema):
    """Schema for new attempt."""

    class Meta:
        model = Attempt
        fields = ["quiz", "student", "result", "answers"]


class AttemptOut(ModelSchema):
    """Schema for output attempt."""

    class Meta:
        model = Attempt
        fields = ["id", "quiz", "student", "result", "answers"]
