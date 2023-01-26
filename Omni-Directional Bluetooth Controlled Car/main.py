from machine import UART, Pin, PWM
from time import sleep

m11 = Pin(2,Pin.OUT)
m12 = Pin(3,Pin.OUT)
m21 = Pin(4,Pin.OUT)
m22 = Pin(5,Pin.OUT)
m31 = Pin(6,Pin.OUT)
m32 = Pin(7,Pin.OUT)
m41 = Pin(8,Pin.OUT)
m42 = Pin(9,Pin.OUT)

# led1 = Pin(10.Pin.OUT)
# led2 = Pin(11.Pin.OUT)
# led3 = Pin(12.Pin.OUT)
# led4 = Pin(13.Pin.OUT)

uart = UART(0, 9600)


def forward():   #move forward
    print("forward")
#     led1.on()
#     led2.on()
#     led3.off()
#     led4.off()
    m11.off()
    m12.on()
    m21.off()
    m22.on()
    m31.off()
    m32.on()
    m41.on()
    m42.off()
    
def backward():   #move backward
    print("backward")
#     led1.off()
#     led2.off()
#     led3.on()
#     led4.on()
    m11.on()
    m12.off()
    m21.on()
    m22.off()
    m31.on()
    m32.off()
    m41.off()
    m42.on()
    
def left():       #move left
    print("left")
    m11.off()
    m12.on()
    m21.on()
    m22.off()
    m31.on()
    m32.off()
    m41.on()
    m42.off()
    
def right():      #move right
    print("right")
    m11.on()
    m12.off()
    m21.off()
    m22.on()
    m31.off()
    m32.on()
    m41.off()
    m42.on()
    
def forwardleft():   #move forward left
    print("forwardleft")
#     led1.on()
#     led2.off()
#     led3.off()
#     led4.off()
    m11.off()
    m12.on()
    m21.off()
    m22.off()
    m31.off()
    m32.off()
    m41.on()
    m42.off()
    
def forwardright():   #move forward right
    print("forwardright")
#     led1.off()
#     led2.on()
#     led3.off()
#     led4.off()
    m11.off()
    m12.off()
    m21.off()
    m22.on()
    m31.off()
    m32.on()
    m41.off()
    m42.off()

def backwardright():   #move backward right
    print("backwardright")
#     led1.off()
#     led2.off()
#     led3.off()
#     led4.on()
    m11.on()
    m12.off()
    m21.off()
    m22.off()
    m31.off()
    m32.off()
    m41.off()
    m42.on()
    
def backwardleft():   #move backward left
    print("backwardleft")
#     led1.off()
#     led2.off()
#     led3.on()
#     led4.off()
    m11.off()
    m12.off()
    m21.on()
    m22.off()
    m31.on()
    m32.off()
    m41.off()
    m42.off()
    
def rotateleft():   #rotate left
    print("rotateleft")
#     led1.on()
#     led2.off()
#     led3.on()
#     led4.off()
    m11.on()
    m12.off()
    m21.on()
    m22.off()
    m31.off()
    m32.on()
    m41.on()
    m42.off()
    
def rotateright():   #rotate right
    print("rotateright")
#     led1.off()
#     led2.on()
#     led3.off()
#     led4.on()
    m11.off()
    m12.on()
    m21.off()
    m22.on()
    m31.on()
    m32.off()
    m41.off()
    m42.on()

def stop():
    print("stop")
    m11.off()
    m12.off()
    m21.off()
    m22.off()
    m31.off()
    m32.off()
    m41.off()
    m42.off()
    
while True:
    if uart.any():
        value = uart.readline()
        print(value)
        
        if value == b'A':
            forwardleft()
        elif value == b'B':
            forward()
        elif value == b'C':
            forwardright()xsac
        elif value == b'D':
            left()
        elif value == b'E':
            right()
        elif value == b'F':
            backwardleft()
        elif value == b'G':
            backward()
        elif value == b'H':
            backwardright()
        elif value == b'I':
            rotateleft()
        elif value == b'J':
            rotateright()
        elif value == b'S':
            stop() 

