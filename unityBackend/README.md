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
＃新增
def create_leds(db: Session, Led: schemas.LedCreate):
    db_Led = models.Leds(Led_id = Led.Led_id , Led_index = Led.Led_index, Led_status = Led.Led_status)
    db.add(db_Led)
    db.commit()
    db.refresh(db_Led)
    return db_Led
＃新增或更新
def createORupdateleds(db: Session, Led: schemas.LedCreate):
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
＃取全部
def get_leds(db: Session):
    return db.query(models.Leds).all()
＃取部分（Led_id）
def get_ledstatus(db: Session , Led_id: int):
    return db.query(models.Leds).filter(models.Leds.Led_id == Led_id).first()
```
## main part
```py
＃新增或更新
@app.post("/leds/", response_model=schemas.LedCreate)
def createORupdateleds(led: schemas.LedCreate, db: Session = Depends(get_db)):
    return crud.createORupdateleds(db=db, Led=led)
＃取全部
@app.get("/getleds/", response_model=list[schemas.LedCreate])
def read_leds(db: Session = Depends(get_db)):
    leds = crud.get_leds(db)
    return leds
＃取狀態
@app.get("/ledstatus/{led_id}", response_model=schemas.LedCreate)
def read_ledstatus(led_id: str, db: Session = Depends(get_db)):
    db_leds = crud.get_ledstatus(db, Led_id=led_id)
    if db_leds is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_leds
```