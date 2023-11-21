from ninja import Schema
from pydantic import Field


class UserIn(Schema):
    """Incoming user schema."""
    username: str = Field(max_length=225)
    email: str = Field(max_length=225)
    password: str = Field(max_length=225)


class UserLogin(Schema):
    """Login user schema."""
    email: str = Field(max_length=225)
    password: str = Field(max_length=225)


class TokenPair(Schema):
    """Incoming user schema."""
    access_token: str = Field(max_length=225)
    refresh_token: str = Field(max_length=225)


class TokenIn(Schema):
    """Incoming refresh token schema."""
    refresh_token: str = Field(max_length=225)
