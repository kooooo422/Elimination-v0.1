from sqlalchemy.orm import Session
from sqlalchemy import update

import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def create_leds(db: Session, Led: schemas.LedCreate):
    update_data = db.query(models.Leds).filter(models.Leds.Led_id == Led.Led_id).first()
    db_Led = models.Leds(Led_id = Led.Led_id , Led_index = Led.Led_index, Led_status = Led.Led_status)
    if update_data is None:
        db.add(db_Led)
        db.commit()
        db.refresh(db_Led)
    else:
        db.delete(update_data)
        db.commit()
        db.add(db_Led)
        db.commit()
        db.refresh(db_Led)
    return db_Led

def get_leds(db: Session):
    return db.query(models.Leds).all()

def get_ledstatus(db: Session , Led_id: int):
    return db.query(models.Leds).filter(models.Leds.Led_id == Led_id).first()

def update_leds(db: Session , Led_id: int, Led: schemas.LedCreate):
    update_data = db.query(models.Leds).filter(models.Leds.Led_id == Led_id).first()
    update_data = Led.dict(exclude_unset=True)
    # for key, value in update_data.items():
    #     setattr(update_data, key, value)
    # db.add(update_data)
    # db.commit()
    # db.refresh(update_data)
    print(update_data)
    return update_data