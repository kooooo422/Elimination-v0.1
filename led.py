from typing import Optional
from fastapi import FastAPI
from typing import Union
app = FastAPI() # 建立一個 Fast API application
from pydantic import BaseModel
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from mfrc522 import SimpleMFRC522
from time import sleep
import RPi.GPIO as GPIO
import time
import eventlet
eventlet.monkey_patch()

# 使用 BCM 編號
GPIO.setmode(GPIO.BCM)

# 操作 GPIO 4（Pin 7）
pin = 17

# 設定為 GPIO 為輸入模式
GPIO.setup(pin, GPIO.OUT)

reader = SimpleMFRC522()
@app.get("/") # 指定 api 路徑 (get方法)
def read_root():
    return {"Hello": "World"}


@app.get("/users/{user_id}") # 指定 api 路徑 (get方法)
def read_user(user_id: int, q: Optional[str] = None):
    return {"user_id": user_id, "q": q}

@app.get("/led/{set}")
async def setLed( set : str ):
    if(set == "on"):
        GPIO.output(pin, GPIO.HIGH)
    if(set == "off"):
        GPIO.output(pin, GPIO.LOW)
    return {"Led": set }
@app.get("/nfctag")
async def nfcDetect():
    try:
        with eventlet.Timeout(1,False):
            print("scan!")
            id, text = reader.read()
            print(id)
    finally:
        GPIO.cleanup()
    GPIO.cleanup()
    return {"nfcTagID": id }

import cv2
cap = cv2.VideoCapture(0)
flag = 1 #設定一個標誌，用來輸出視訊資訊
@app.get("/pic/{id}")
async def takeApic( id : int ):
    ret_flag, Vshow = cap.read() #返回兩個引數，第一個是bool是否正常開啟，第二個是照片陣列，如果只設定一個則變成一個tumple包含bool和圖片 #視窗顯示，顯示名為 Capture_Test
    cv2.imwrite(f"picData/testAPI{id}.jpg", Vshow)
    cap.release() #釋放攝像頭
    cv2.destroyAllWindows()#刪除建立的全部視窗
    return { "pic" : "success" }
@app.get("/led")
async def led( ledStatus : str ):
    GPIO.cleanup()
    if(ledStatus == "on"):
        GPIO.output(pin, GPIO.HIGH)

    if(ledStatus == "off"):
        GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()
    return { "ledStatus" : ledStatus }
servo0Pin=24
servo1Pin=27
servo0 = Servo(servo0Pin)
servo1 = Servo(servo1Pin)
servo0.value = 0
servo1.value = 0
def sg90(sg90id):
    if(sg90id == 0):
        servo = servo0
    elif(sg90id == 1):
        servo = servo1
    servo.value = 1
    sleep(1)
    servo.value = 0
    print("open")
    sleep(1)
@app.get("/sg90/{id}")
async def sg90_run( id : int ):
    sg90(id)
    text = f'sg90 {id} on'
    return {"sg90":text}
