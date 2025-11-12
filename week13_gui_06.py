from tkinter import *
from gpiozero import LED

red_led = LED(23) 
green_led = LED(18) 

win = Tk()
win.title("LED 제어 GUI")
win.geometry("300x300")

red_led_on = False
green_led_on = False

red_label = Label(win, text="Red OFF", bg="gray", fg="white", font=("Arial", 14), width=12, height=2)
red_label.pack(pady=10)

green_label = Label(win, text="Green OFF", bg="gray", fg="white", font=("Arial", 14), width=12, height=2)
green_label.pack(pady=10)

def toggle_red_led():
    global red_led_on
    if red_led_on:
        red_led.off()
        red_label.config(text="Red OFF", bg="gray")
        red_led_button.config(text="Red ON")
        red_led_on = False
    else:
        red_led.on()
        red_label.config(text="Red ON", bg="red")
        red_led_button.config(text="Red OFF")
        red_led_on = True

def toggle_green_led():
    global green_led_on
    if green_led_on:
        green_led.off()
        green_label.config(text="Green OFF", bg="gray")
        green_led_button.config(text="Green ON")
        green_led_on = False
    else:
        green_led.on()
        green_label.config(text="Green ON", bg="green")
        green_led_button.config(text="Green OFF")
        green_led_on = True

def on_exit():
    red_led.off()
    green_led.off()
    win.destroy()

# 버튼 생성
red_led_button = Button(win, text="Red ON", command=toggle_red_led, height=2, width=10)
red_led_button.pack(pady=5)

green_led_button = Button(win, text="Green ON", command=toggle_green_led, height=2, width=10)
green_led_button.pack(pady=5)

exit_button = Button(win, text="Exit", command=on_exit, height=2, width=10)
exit_button.pack(pady=10)

win.mainloop()
