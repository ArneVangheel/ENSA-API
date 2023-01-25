from passlib.context import CryptContext
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import crud
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

# Configuratie
SECRET_KEY = "454f5974f238422531030ba6889141e2a609b008d1f363fa8d39f7837175b393"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["argon2", "bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)



#User authenticatie
def authenticate_user(db: Session, username: str, password: str):
    if username == "admin" and password == "admin":
        return username
    else:
        return False


def create_access_token(data: dict):
    to_encode = data.copy()
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        # Default to 15 minutes of expiration time if ACCESS_TOKEN_EXPIRE_MINUTES variable is empty
        expire = datetime.utcnow() + timedelta(minutes=15)
    # Adding the JWT expiration time case
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
