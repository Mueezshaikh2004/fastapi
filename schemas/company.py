from pydantic import BaseModel

class Company(BaseModel):
    name: str
    location: str
    
class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None