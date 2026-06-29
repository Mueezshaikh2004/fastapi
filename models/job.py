from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from models.company import Company
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship


class Job(Base):
    __tablename__ = "job"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    salary = Column(Integer)
    company_id = Column(Integer, ForeignKey("company.id"))
    company = relationship("Company", back_populates="jobs")   