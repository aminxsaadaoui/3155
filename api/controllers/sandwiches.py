from sqlalchemy.orm import Session
from api.models import models, schemas

def create(db: Session, sandwich: schemas.SandwichCreate):
    db_sandwich = models.Sandwich(**sandwich.model_dump())
    db.add(db_sandwich)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

def read_all(db: Session):
    return db.query(models.Sandwich).all()

def read_one(db: Session, sandwich_id: int):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()

def update(db: Session, sandwich: schemas.SandwichUpdate, sandwich_id: int):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()
    if db_sandwich is None:
        return None
    for key, value in sandwich.model_dump().items():
        setattr(db_sandwich, key, value)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

def delete(db: Session, sandwich_id: int):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()
    if db_sandwich is None:
        return None
    db.delete(db_sandwich)
    db.commit()
    return db_sandwich
