from pydantic import BaseModel, EmailStr
from datetime import date


class ClientCreate(BaseModel):
client_name: str
company_name: str
city: str | None = None
contact_person: str | None = None
phone: str
email: EmailStr


class CaseCreate(BaseModel):
client_id: int
invoice_number: str
invoice_amount: float
invoice_date: date
due_date: date


class CaseUpdate(BaseModel):
status: str | None = None
last_follow_up_notes: str | None = None