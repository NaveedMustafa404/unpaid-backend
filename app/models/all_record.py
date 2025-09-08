from sqlalchemy import Column, Integer, String,Float
from app.db.database import Base

class AllRecord(Base):
    __tablename__ = "AllRecord"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    gender = Column(String(10), nullable=False)
    total_hour = Column(Float, nullable=False)
    total_points = Column(Float, nullable=False)
    cooking = Column(Float, default=0.0)
    grocery = Column(Float, default=0.0)
    cleaning = Column(Float, default=0.0)
    laundry = Column(Float, default=0.0)
    child_care = Column(Float, default=0.0)
    elder_care = Column(Float, default=0.0)
    other_care_work = Column(Float, default=0.0)
    trnportation = Column(Float, default=0.0)
    child_education = Column(Float, default=0.0)
    running_household = Column(Float, default=0.0)
    home_maintenance = Column(Float, default=0.0)
    other_activities = Column(Float, default=0.0)
