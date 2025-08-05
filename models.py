from enum import Enum

class StatusType(str, Enum):
    """Enum for task status."""
    DONE = "done"
    PENDING = "pending"
