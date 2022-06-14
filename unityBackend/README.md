## models part
```py
class Leds(Base):
    __tablename__ = "led"

    Led_id = Column(String, primary_key=True, index=True)
    Led_index = Column(String, index=True)
    Led_status = Column(String, index=True)
```
## schemas part
```py
class LedCreate(BaseModel):
    Led_id :str
    Led_index :str
    Led_status :str
    class Config:
        orm_mode = True
```
## crud part
```py
def create_leds(db: Session, Led: schemas.LedCreate):
    db_Led = models.Leds(Led_id = Led.Led_id , Led_index = Led.Led_index, Led_status = Led.Led_status)
    db.add(db_Led)
    db.commit()
    db.refresh(db_Led)
    return db_Led
```
## main part
```py
@app.post("/leds/", response_model=schemas.LedCreate)
def create_leds(led: schemas.LedCreate, db: Session = Depends(get_db)):
    return crud.create_leds(db=db, Led=led)
```