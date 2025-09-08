from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app import crud, schemas
from app.schemas import all_record as all_record_schema
from app.crud import all_record as all_record_crud


router = APIRouter(prefix="/allrecords", tags=["AllRecord"])

@router.get("/", response_model=list[all_record_schema.AllRecordResponse])
def read_records(db: Session = Depends(get_db)):
    return all_record_crud.get_records(db)




@router.get("/dashboard-metrics", )
def read_male_total_hours(db: Session = Depends(get_db)):
    total_hours_man = all_record_crud.get_avg_hours_of_man(db)
    total_hours_women = all_record_crud.get_avg_hours_of_woman(db)
    return {"total_man_hours": total_hours_man or 0, "total_women_hours": total_hours_women or 0}

@router.get("/woman")
def read_male_total_hours(db: Session = Depends(get_db)):
    total_hours = all_record_crud.get_total_hours_of_woman(db)
    return {"total_woman_hours": total_hours or 0}

@router.get("/man")
def read_male_total_hours(db: Session = Depends(get_db)):
    total_hours = all_record_crud.get_total_hours_of_man(db)
    return {"total_man_hours": total_hours or 0}

@router.get("/{record_id}", response_model=all_record_schema.AllRecordResponse)
def read_record(record_id: int, db: Session = Depends(get_db)):
    db_record = all_record_crud.get_record(db, record_id)
    if not db_record:
        raise HTTPException(status_code=404, detail="Record not found")
    return db_record

@router.post("/", response_model=schemas.all_record.AllRecordResponse)
def create_record(record: schemas.all_record.AllRecordCreate, db: Session = Depends(get_db)):
    return crud.all_record.create_record(db, record)

@router.put("/{record_id}", response_model=schemas.all_record.AllRecordResponse)
def update_record(record_id: int, record: schemas.all_record.AllRecordUpdate, db: Session = Depends(get_db)):
    db_record = crud.all_record.update_record(db, record_id, record)
    if not db_record:
        raise HTTPException(status_code=404, detail="Record not found")
    return db_record

@router.delete("/{record_id}")
def delete_record(record_id: int, db: Session = Depends(get_db)):
    db_record = crud.all_record.delete_record(db, record_id)
    if not db_record:
        raise HTTPException(status_code=404, detail="Record not found")
    return {"detail": "Record deleted"}
