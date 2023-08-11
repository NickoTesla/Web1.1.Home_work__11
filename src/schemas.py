from datetime import date
from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr

class ContactBase(BaseModel):
    first_name: str = Field(..., max_length=50, description="First name of the contact")
    last_name: str = Field(..., max_length=50, description="Last name of the contact")
    email: EmailStr = Field(..., description="Email address of the contact")
    phone_number: str = Field(..., max_length=20, description="Phone number of the contact")
    birth_date: Optional[date] = Field(None, description="Birth date of the contact (YYYY-MM-DD)")
    additional_data: Optional[str] = Field(None, description="Additional data about the contact")

class ContactCreate(ContactBase):
    pass

class ContactUpdate(ContactBase):
    pass

class ContactResponse(ContactBase):
    id: int

    class Config:
        orm_mode = True
