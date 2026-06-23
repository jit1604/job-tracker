from pydantic import BaseModel
from typing import Optional

class JobApplication(BaseModel):
    company: str
    role: str
    status: str
    deadline: str
    priority: str
    notes: Optional[str] = None