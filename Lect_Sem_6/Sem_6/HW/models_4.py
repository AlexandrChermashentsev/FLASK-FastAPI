from pydantic import BaseModel, Field


class Task(BaseModel):
    task_id: int
    title: str = Field(..., title="Title", max_length=32)
    description: str = Field(default=None, title="Description", max_length=1000)
    status: bool = Field(default=False)

class TaskIn(BaseModel):
    title: str = Field(..., title="Title", max_length=32)
    description: str = Field(default=None, title="Description", max_length=1000)
    status: bool = Field(default=False)
