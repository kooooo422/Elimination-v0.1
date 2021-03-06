from turtle import up
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
async def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
async def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@app.post("/leds/", response_model=schemas.LedCreate)
async def createORupdateleds(led: schemas.LedCreate, db: Session = Depends(get_db)):
    return crud.createORupdateleds(db=db, Led=led)

@app.get("/getleds/", response_model=list[schemas.LedCreate])
async def read_leds(db: Session = Depends(get_db)):
    leds = crud.get_leds(db)
    return leds

@app.get("/ledstatus/{led_id}", response_model=schemas.LedCreate)
async def read_ledstatus(led_id: str, db: Session = Depends(get_db)):
    db_leds = crud.get_ledstatus(db, Led_id=led_id)
    if db_leds is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_leds
@app.patch("/ledsupdate/{led_id}", response_model=schemas.LedCreate)
async def update_led(led_id: int,led: schemas.LedCreate, db: Session = Depends(get_db)):
    update_data = crud.update_leds(db=db, Led_id=led_id,Led=led)
    return update_data



class LEDstatus(BaseModel):
    LED_id: str
    LED_index: str
    LED_status: str


@app.get("/")
async def getLEDstatus():
    return {"led":"on","ledIndex":"2"}

# @app.post("/ledstatus/")
# async def postLEDstatus( status : LEDstatus):
#     print(status)
#     return status 
