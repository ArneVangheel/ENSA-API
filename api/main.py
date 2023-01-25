from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
import secrets
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import os
import crud
import models
import schemas
from database import SessionLocal, engine

print("We are in the main.......")
if not os.path.exists('.\sqlitedb'):
    print("Making folder.......")
    os.makedirs('.\sqlitedb')

print("Creating tables.......")
models.Base.metadata.create_all(bind=engine)
print("Tables created.......")

app = FastAPI()
security = HTTPBasic()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/code", response_model=schemas.Codes)
def create_code(code: schemas.CodesCreate, db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(security)):
    db_code = crud.get_code_by_code(db, code=code.code)
    if db_code:
        raise HTTPException(status_code=400, detail="Code already registered")
    return crud.create_code(db=db, code=code)


@app.get("/code", response_model=list[schemas.Codes])
def read_codes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(security)):
    codes = crud.get_codes(db, skip=skip, limit=limit)
    return codes

@app.get("/check_code/{code}")
def check_codes(code: str, db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(security)):
    db_code = crud.get_code_by_code(db, code=code)
    if db_code:
        return(True)
    else:
        return(False)

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    if not (credentials.username == "admin") or not (credentials.password == "admin"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
@app.get("/users/me")
def read_current_user(username: str = Depends(get_current_username)):
    return {"username": username}