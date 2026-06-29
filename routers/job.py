from fastapi import APIRouter,HTTPException,Depends,status
from schemas.job import JobCreate, JobUpdate,JobResponse
from models import job
from sqlalchemy.orm import Session
from database import get_db,sessionlocal

router = APIRouter(prefix="/job", tags=["job"])


@router.post("/",status_code=status.HTTP_201_CREATED,response_model=JobResponse)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    db_job = job.Job(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

@router.get("/",status_code=status.HTTP_200_OK,response_model=list[JobResponse])
def get_all_job(db: Session = Depends(get_db)):
    return db.query(job.Job).all()

@router.get("/{job_id}",status_code=status.HTTP_200_OK,response_model=JobResponse)
def get_job(job_id: int, db: Session = Depends(get_db)):
    db_job = db.query(job.Job).filter(job.Job.id == job_id).first()
    if not db_job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with id {job_id} not found")
    return db_job

@router.put("/{job_id}",status_code=status.HTTP_200_OK,response_model=JobResponse)
def update_job(job_id: int, job: JobUpdate, db: Session = Depends(get_db)):
    db_job = db.query(job.Job).filter(job.Job.id == job_id).first()
    if not db_job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with id {job_id} not found")
    for key, value in job.__dict__.items():
        setattr(db_job, key, value)
    db.commit()
    db.refresh(db_job)
    return db_job

@router.delete("/{job_id}",status_code=status.HTTP_204_NO_CONTENT,response_model=None)
def delete_job(job_id: int, db: Session = Depends(get_db)):
    db_job = db.query(job.Job).filter(job.Job.id == job_id).first()
    if not db_job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with id {job_id} not found")
    db.delete(db_job)
    db.commit()
    return {"message": f"Job with id {job_id} has been deleted successfully."}

# @router.get("/")
# def read_job():
#     return {"job": "Job root"}

# @router.get("/{job_id}")
# def read_job(job_id: int):
#     return {"job_id": job_id}