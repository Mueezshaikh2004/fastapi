from fastapi import APIRouter,HTTPException,Depends,status
from schemas.company import CompanyCreate, CompanyUpdate, CompanyResponse
from models import company,job
from sqlalchemy.orm import Session
from database import get_db,sessionlocal


router = APIRouter(prefix="/company",tags=["company"])

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=CompanyResponse)
def create_company(company: CompanyCreate,db:Session=Depends(get_db)):
    pass


@router.get("/",status_code=status.HTTP_200_OK,response_model=list[CompanyResponse])
def get_all_company(db:Session=Depends(get_db)):
    pass

@router.get("/{company_id}",status_code=status.HTTP_200_OK,response_model=CompanyResponse)
def get_all_company(company_id: int,db:Session=Depends(get_db)):
    companies = db.query(company.Company).filter(company).all()
    return companies

@router.put("/{company_id}",status_code=status.HTTP_201_CREATED)
def update_company(company_id: int, company: CompanyUpdate,db:Session=Depends(get_db)):
    db_company = db.query(company.Company).filter(company.Company.id == company_id).first()
    if not db_company:   
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Company with id {company_id} not found")
    for key, value in company.__dict__.items():
        setattr(db_company, key, None)
    db.commit()
    db.refresh(db_company)
    return db_company

@router.delete("/{company_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_company(company_id: int,db:Session=Depends(get_db)):
    db_company = db.query(company.Company).filter(company.Company.id == company_id).first()
    if not db_company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Company with id {company_id} not found")
    db.delete(db_company)
    db.commit()
    return {"message": f"Company with id {company_id} has been deleted successfully."}
    
  
# @router.get("/")
# def read_company():
#     return {"company": "Company root"}

# @router.get("/{company_id}")
# def read_company(company_id: int):
#     return {"company_id": company_id}