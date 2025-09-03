from pydantic import BaseModel, field_validator, ValidationError
from enum import Enum

class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str

class StatusType(str, Enum):
    """Enum for task status."""
    DONE = "done"
    PENDING = "pending"

class Category(BaseModel):
    id: int
    name: str
    
class Task(BaseModel):
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
    
    @field_validator('id')
    def greater_than_zero(cls, v):
        if v <= 0:
            raise ValueError('ID must be greater than zero')
        return v

    @field_validator('id')
    def id_less_than_a_thousand(cls, v):
        if v >= 1000:
            raise ValueError('ID must be less than 1000')
        return v
