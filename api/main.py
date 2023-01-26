from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
import os
import crud
import models
import schemas
import auth
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
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

origins = [
    "http://localhost/",
    "http://localhost:8080/",
    "http://localhost:63342",
    "https://localhost.tiangolo.com/",
    "http://127.0.0.1:5500/",
    "http://127.0.0.1:8080",
    "https://api-eindproject.netlify.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/code", response_model=schemas.Codes)
def create_code(code: schemas.CodesCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_code = crud.get_code_by_code(db, code=code.code)
    if db_code:
        raise HTTPException(status_code=400, detail="Code already registered")
    return crud.create_code(db=db, code=code)


@app.get("/code", response_model=list[schemas.Codes])
def read_codes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    codes = crud.get_codes(db, skip=skip, limit=limit)
    return codes

@app.get("/check_code/{code}")
def check_codes(code: str, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_code = crud.get_code_by_code(db, code=code)
    if db_code:
        return db_code
    else:
        return(False)

@app.delete("/code/{code}")
def delete_order(code: str, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    #Controleer of er een code op dit id staat
    db_code = crud.get_code_by_code(db, code=code)
    if not db_code:
        raise HTTPException(status_code=400, detail="There is no Code registered")
    #Zoja, verwijder de code
    code = crud.delete_code(db, code=code)
    return code

@app.put("/code/{code}", response_model=schemas.Codes)
def edit_code(code: str, item: schemas.CodesEdit, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_code = crud.get_code_by_code(db, code=code)
    if not db_code:
        raise HTTPException(status_code=400, detail="There is no code registered")
    db_item = crud.edit_code(db, item, code=code)
    return db_item


@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(
        data={"sub": user}
    )
    return {"access_token": access_token, "token_type": "bearer"}
