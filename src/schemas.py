from typing import Optional
import re

from pydantic import BaseModel, validator


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None
    phone_number: Optional[str] = None

    @validator("phone_number")
    def validate_phone(cls, value):
        if value is None:
            return value
        if len(value) > 30:
            raise ValueError("Too long number!")
        if not re.fullmatch(r'\+[\d]+', value):
            raise ValueError(
                "Wrong phone number")
        return value

    @validator("name")
    def validate_name(cls, value):
        if value is None or not value:
            raise ValueError("Empty name!")
        if len(value) > 30:
            raise ValueError("Too long name!")
        return value

    @validator("description")
    def validate_desc(cls, value):
        if value is None or not value:
            raise ValueError("Empty description!")
        if len(value) > 200:
            raise ValueError("Too long description!")
        return value


class STask(STaskAdd):
    id: int
