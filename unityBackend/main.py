from typing import Union , Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LEDstatus(BaseModel):
    LED_id: str
    LED_index: str
    LED_status: str


@app.get("/")
async def getLEDstatus():
    return {"led":"on","ledIndex":"2"}

@app.post("/ledstatus/")
async def postLEDstatus( status : LEDstatus):
    print(status)
    return status 
