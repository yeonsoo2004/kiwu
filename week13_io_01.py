import RPi.GPIO as GPIO
import time

LED_PIN = 18    #BOARD 11
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)  # set output(출력핀 설정)

def led_on():
    GPIO.output(LED_PIN,GPIO.HIGH)
    print("LED ON")
def led_off():
    GPIO.output(LED_PIN,GPIO.LOW)
    print("LED OFF")
def main():
    try:
        while True:
            user_input = input("Led_led gpio pin 18번\n#1) led on 2) led off 0)quit: ")
            if menu == '1':
                led_on()
            elif menu == '2':
                led_off()
            elif menu == '0':
                print("종료")
                break
            else:
                print("잘못된 입력입니다. 1,2,0중 하나를 입력하세요.")
    except KeyboardInterrupt:
        print("\n프로그램 강제 종료")
    finally:
        GPIO.cleanup()  #initialize GPIO setting
    
