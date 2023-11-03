from pydantic import BaseModel, Field


class Form(BaseModel):
    age: int = Field(..., gt=0, lt=115)
    name: str = Field(default="", max_length=20)
