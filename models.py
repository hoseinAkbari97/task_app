from pydantic import BaseModel, field_validator
from enum import Enum

class MyBaseModel(BaseModel):
    """my base model for validation"""
    id: int

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
    name: str
    surname: str
    email: str

class StatusType(str, Enum):
    """Enum for task status."""
    DONE = "done"
    PENDING = "pending"

class Category(MyBaseModel):
    id: int
    name: str
    
class Task(MyBaseModel):
    id: int
    name: str
    description: str
    status: StatusType
    user: User
    category: Category

    @field_validator('name')
    def id_name_alphanumeric(cls, v):
        assert v.replace(" ", "").isalnum(), 'Name must be alphanumeric'
        return v
