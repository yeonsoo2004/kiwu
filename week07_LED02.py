import RPi.GPIO as GPIO
import time

LED_PIN = 18    #BOARD 11
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)  # set output(출력핀 설정)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)   #HIGH: 전압 공급
        time.sleep(2)   #delay by 2 sec
        GPIO.output(LED_PIN, GPIO.LOW)   #HIGH: 전압 0으로 
        time.sleep(2)   #delay by 2 sec
except KeyboardInterrupt:
    print("Exit program")
finally:
    GPIO.cleanup()  #initialize GPIO setting
    