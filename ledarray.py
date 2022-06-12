import board
import neopixel
import numpy as p
from time import sleep
 
colors = p.random.randint(0, 255,(80, 3)) 
np = neopixel.NeoPixel(board.D18, 60)
np.brightness = 0.5
    
 
        
def color1():
     for i in range (60):  
         color = colors[i-19]
         np[i]=(color)
         np.show()
      
def color2():     
     for i in range(59,0,-1):
         color = colors[i-20]    
         np[i]=(color)
         np.show()
        
def color3():        
    for i in range (60):  
         color = colors[i-20]
         np[i]=(color)
         np.show()
      
def  color4():      
     for i in range(59,0,-1):
         np[i]=(0,0,255)

def color5():        
    for i in range (60):  
         color = colors[i-35]
         np[i]=(255,0,0)
         np.show()
         sleep(0.1)
         np[i]=(0,0,0)
         sleep(0.1)
         np [i]=(color)

def color6():
    for i in range (60):
        np[i]=(0,0,0)
while True:
    color1()
    color2()
    color3()
    color4()
    color5()
