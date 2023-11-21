from ninja import Schema


class Message(Schema):
    """Message schema api response."""
    message: str
