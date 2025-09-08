from pydantic import BaseModel

class AllRecordBase(BaseModel):
    name: str
    gender: str
    total_hour: float
    total_points: float
    cooking: float = 0.0
    grocery: float = 0.0
    cleaning: float = 0.0
    laundry: float = 0.0
    child_care: float = 0.0
    elder_care: float = 0.0
    other_care_work: float = 0.0
    trnportation: float = 0.0
    child_education: float = 0.0
    running_household: float = 0.0
    home_maintenance: float = 0.0
    other_activities: float = 0.0

class AllRecordCreate(AllRecordBase):
    pass

class AllRecordUpdate(AllRecordBase):
    pass

class AllRecordResponse(AllRecordBase):
    id: int

    class Config:
        orm_mode = True
