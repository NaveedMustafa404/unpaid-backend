from sqlalchemy.orm import Session
from app.models.all_record import AllRecord
from app.schemas.all_record import AllRecordCreate, AllRecordUpdate
###
from sqlalchemy import func

def get_records(db: Session):
    return db.query(AllRecord).all()

def get_record(db: Session, record_id: int):
    return db.query(AllRecord).filter(AllRecord.id == record_id).first()
###
def get_total_hours_of_man(db: Session):

    return db.query(func.sum(AllRecord.total_hour))\
        .filter(AllRecord.gender == "Man")\
             .scalar()

def get_avg_hours_of_man(db: Session):

    avg_value= db.query(func.avg(AllRecord.total_hour))\
        .filter(AllRecord.gender == "Man")\
             .scalar()
    return avg_value or 0

def get_total_hours_of_woman(db: Session):
    return db.query(func.sum(AllRecord.total_hour))\
             .filter(AllRecord.gender == "Woman")\
             .scalar()


def get_avg_hours_of_woman(db: Session):
    avg_value = db.query(func.avg(AllRecord.total_hour)) \
        .filter(AllRecord.gender == "Woman") \
        .scalar()
    return avg_value or 0

def create_record(db: Session, record: AllRecordCreate):
    db_record = AllRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def update_record(db: Session, record_id: int, record: AllRecordUpdate):
    db_record = get_record(db, record_id)
    if db_record:
        for key, value in record.dict().items():
            setattr(db_record, key, value)
        db.commit()
        db.refresh(db_record)
    return db_record

def delete_record(db: Session, record_id: int):
    db_record = get_record(db, record_id)
    if db_record:
        db.delete(db_record)
        db.commit()
    return db_record
