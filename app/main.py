from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import Base, engine
from app.api.route_all_records import router as all_record_router

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Unpaid Work API", version="1.0.0")

# Allow CORS (important for Flutter Web)
origins = [
    "http://localhost:50942",   # Flutter web local
    "http://127.0.0.1:50942",   # alternative local
    "http://localhost:8000",    # optional if API accessed directly
    "http://127.0.0.1:8000",    # optional if API accessed directly
    "*"                         # <-- dev only (all origins)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] for dev
    allow_credentials=True,
    allow_methods=["*"],    # allow POST, GET, OPTIONS etc.
    allow_headers=["*"],
)

# Routers
app.include_router(all_record_router)

@app.get("/")
def root():
    return {"message": "FastAPI + MySQL CRUD ready!"}
