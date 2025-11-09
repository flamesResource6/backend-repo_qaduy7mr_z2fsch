from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Contact(BaseModel):
    name: str = Field(..., description="Sender name")
    email: EmailStr = Field(..., description="Sender email")
    message: str = Field(..., min_length=1, max_length=2000, description="Message body")

# Example existing schemas remain available in schema_examples.py
