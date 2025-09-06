from pydantic import BaseModel, Field ,field_validator
from enum import Enum
from typing import Optional

class MyBaseModel(BaseModel):
    """my base model for validation"""
    id: int = Field(ge=1, le=100)

    @field_validator('id')
    def greater_than_zero(cls, v):
        if v <= 0:
            raise ValueError('must be greater than zero')
        return v
    
    @field_validator('id')
    def less_than_a_thousand(cls, v):
        if v > 1000:
            raise ValueError('must be less than a thousand')
        return v

class User(MyBaseModel):
    id: int
    name: str = Field(min_length=3)
    surname: str
    email: str

class StatusType(str, Enum):
    """Enum for task status."""
    READY = "ready"
    PENDING = "pending"

class Category(MyBaseModel):
    id: int
    name: str
    
class Task(MyBaseModel):
    id: int
    name: str
    description: Optional [str] = Field(None, min_length=3)
    status: StatusType
    user: User
    category: Category

    @field_validator('name')
    def id_name_alphanumeric(cls, v):
        assert v.replace(" ", "").isalnum(), 'Name must be alphanumeric'
        return v
