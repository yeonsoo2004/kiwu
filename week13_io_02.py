from gpiozero import LED

led = LED(18)

while True:
    try:
        cmd = input("1) led on 2) led off 0)quit: ")
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
        break
    except