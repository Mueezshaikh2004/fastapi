from sqlalchemy import Column, Integer, String,Enum, relationship
from database import base,engine,sessionlocal

class company(base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    jobs = relationship("job", back_populates="company")
    
   