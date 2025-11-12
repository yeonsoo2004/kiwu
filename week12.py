import RPi.GPIO as GPIO
import time

LED_PIN = 18    #BOARD 11
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)  # set output(출력핀 설정)


pwm =GPIO.PWM(LED_PIN, 1000)
pwm.start(0)

try:
    while True:
        for dc in range(0,101,5):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.05) #0.05sec
        for dc in range(100,-1,-5):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.05) #0.05sec
            
except KeyboardInterrupt:
    print("Exit program")
finally:
    pwm.stop()
    GPIO.cleanup()  #initialize GPIO setting
    
