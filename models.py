from pydantic import BaseModel
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
