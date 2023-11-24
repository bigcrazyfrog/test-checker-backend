from ninja import ModelSchema

from ..models import Quiz


class QuizAdd(ModelSchema):
    """Schema for new quiz."""

    class Meta:
        model = Quiz
        fields = ["title", "description", "content"]


class QuizOut(ModelSchema):
    """Schema for output quiz."""

    class Meta:
        model = Quiz
        fields = ["id", "title", "description", "content"]
