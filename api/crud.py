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

def delete_code(db: Session, code = str):
    db_item = db.query(models.Codes).filter(models.Codes.code == code).first()
    db.delete(db_item)
    db.commit()
    return {"detail": "The code has been deleted"}


def get_code(db: Session, code_id: int):
    return db.query(models.Codes).filter(models.Codes.id == code_id).first()


def edit_code(db: Session, item = schemas.CodesEdit, code = str):
    db_item = db.query(models.Codes).filter(models.Codes.code == code).first()
    db_item.uses = item.uses
    db.commit()
    db.refresh(db_item)
    return db_item
