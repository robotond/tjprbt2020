from machine import Pin
led=Pin(2,Pin.OUT) #onboard LED
pwr=Pin(27,Pin.OUT) #PWR_ON pin
M1A=Pin(32,Pin.OUT) #Motor conrtoller pins as appear on the motor controller board
M1B=Pin(33,Pin.OUT)
M2A=Pin(25,Pin.OUT)
M2B=Pin(26,Pin.OUT)

pwr.value(True)
led.value(True)

M1A.value(True)
M2A.value(True)
M1B.value(True)
M2B.value(True)
