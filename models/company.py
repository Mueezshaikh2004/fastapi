from sqlalchemy import Column, Integer, String,Enum
from database import Base,engine,sessionlocal
from sqlalchemy.orm import relationship

class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    jobs = relationship("Job", back_populates="company")
    
   