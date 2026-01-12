from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey, DECIMAL, Text
from database import Base


class Client(Base):
__tablename__ = "clients"
id = Column(Integer, primary_key=True, index=True)
client_name = Column(String(100), nullable=False)
company_name = Column(String(150), nullable=False)
city = Column(String(100))
contact_person = Column(String(100))
phone = Column(String(20), nullable=False)
email = Column(String(150), unique=True, nullable=False)


class Case(Base):
__tablename__ = "cases"
id = Column(Integer, primary_key=True, index=True)
client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
invoice_number = Column(String(50), nullable=False)
invoice_amount = Column(DECIMAL(10,2), nullable=False)
invoice_date = Column(Date, nullable=False)
due_date = Column(Date, nullable=False)
status = Column(Enum('New','In Follow-up','Partially Paid','Closed'), default='New')
last_follow_up_notes = Column(Text)