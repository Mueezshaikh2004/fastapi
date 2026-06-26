from fastapi import APIRouter
from schemas.company import Company, CompanyUpdate

router = APIRouter()

router = APIRouter(prefix="/company", tags=["company"])
company = []



@router.get("/")
def read_company(company: CompanyCreate):
    company.append(company)
    return company

# @router.get("/")
#def read_company():
#  return {"company": "Company root"}