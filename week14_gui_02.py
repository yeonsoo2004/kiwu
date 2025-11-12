import tkinter as tk
from gpiozero import LED

def get_input_value():
    num = en_input.get()
    if num == "1":
        red_led.on()
        lbl_display.config("LED ON")
    elif num == "0":
        red_led.off()
        lbl_display.config("LED OFF")
    else:
        lbl_display.config("0또는 1 입력 ")
        
red_led = LED(16)

win = tk.Tk()  #윈도우 객체 생성
win.title("GUI")
win.geometry("400x200")

en_input = tk.Entry(win, width=15)
btn_click = tk.Button(win, text='Click',width=15, command= get_input_value)
lbl_display = tk.Label(win,text='Display', width=30)

#lbl_display.pack()
#en_input.pack()
#btn_click.pack()

lbl_display.grid(row=0, column=0, columnspan=2)
en_input.grid(row=1, column=0)
btn_click.grid(row=1, column=1)

win.mainloop()



