from gpiozero import LED
# import time
from time import sleep

led = LED(17)   #GPIO PIN으로 동작 

try:
    while True:
        led.on()
#         time.sleep(2)   #delay by 2 sec
        sleep(2)
#         GPIO.output(LED_PIN, GPIO.LOW)   #HIGH: 전압 0으로 
        led.off()
#         time.sleep(2)   #delay by 2 sec
        sleep(2)
except KeyboardInterrupt:
    print("Exit program")
finally:
#     GPIO.cleanup()  #initialize GPIO setting
    led.close()