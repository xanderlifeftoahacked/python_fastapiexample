from typing import Optional

from pydantic import BaseModel, Field, validator


class STaskAdd(BaseModel):
    name: str = Field(..., max_length=30, min_length=1)
    description: Optional[str] = Field(None, max_length=300)
    phone_number: Optional[str] = Field(None,
                                        pattern=r'\+[\d]+', max_length=30, min_length=1)


class STask(STaskAdd):
    id: int


class SUserAdd(BaseModel):
    login: str = Field(..., pattern=r'[a-zA-Z0-9-]+',
                       max_length=30, min_length=1)
    password: str = Field(...,
                          pattern=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,}$', max_length=30, min_length=1)

    phone_number: Optional[str] = Field(None,
                                        pattern=r'\+[\d]+', max_length=30, min_length=1)


class SUser(BaseModel):
    id: int
    login: str
    phone_number: Optional[str] = None
