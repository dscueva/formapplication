from pydantic import BaseModel, EmailStr, Field

class FormData(BaseModel):
    name: str = Field(..., example="John Doe")
    email: EmailStr = Field(..., example="johndoe@example.com")
    message: str = Field(..., example="This is a demo message.")
