from pydantic import BaseModel, field_validator, ValidationError
from enum import Enum

class StatusType(str, Enum):
    """Enum for task status."""
    DONE = "done"
    PENDING = "pending"
    
class Task(BaseModel):
    id: int
    name: str
    description: str
    status: StatusType
    
    @field_validator('id')
    def greater_than_zero(cls, v):
        if v <= 0:
            raise ValueError('ID must be greater than zero')
        return v
