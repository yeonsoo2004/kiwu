from gpiozero import LED
from time import sleep

red_led = LED(17)   #GPIO PIN으로 동작
green_led = LED(27)

try:
    while True:
        red_led.on()
        green_led.off()
        sleep(2)
#         GPIO.output(LED_PIN, GPIO.LOW)   #HIGH: 전압 0으로 
        red_led.off()
        green_led.on()
        sleep(2)
except KeyboardInterrupt:
    print("Exit program")
finally:
    red_led.close()
    green_led.close()
