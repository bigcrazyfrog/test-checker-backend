from ninja import Schema
from pydantic import Field


class UserUpdate(Schema):
    """Updation user schema."""
    first_name: str | None = None
    last_name: str | None = None


class UserOut(Schema):
    """Updation output schema."""
    username: str = Field(max_length=225)
    email: str = Field(max_length=225)
    first_name: str | None = Field(max_length=225)
    last_name: str | None = Field(max_length=225)
