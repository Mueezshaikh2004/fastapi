from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from models.company import company
from sqlalchemy.orm import declarative_base

base = declarative_base()

class job(base):
    __tablename__ = "job"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    salary = Column(Integer, nullable=False)
    company_id = Column(Integer, ForeignKey("company.id"))