from sqlalchemy.orm import Session

import models
import schemas

def get_code_by_code(db: Session, code: str):
    return db.query(models.Codes).filter(models.Codes.code == code).first()

def get_codes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Codes).offset(skip).limit(limit).all()

def create_code(db: Session, code: schemas.CodesCreate):
    db_item = models.Codes(**code.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
