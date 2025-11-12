import tkinter as tk

led = False

def led_on_off():
    global led
    #print("LED 켜짐")
    if led:
        lbl_display.config(text="LED 꺼짐")  #config : 밑이 아니라 버튼창에 뜨도록 함
        led = False
    else:
        lbl_display.config(text="LED 켜짐")
        led = True
        
win = tk.Tk()  #윈도우 객체 생성
win.title("GUI")
win.geometry("400x200")
win.resizable(False,False)

btn_on_off = tk.Button(win, text="LED ON/OFF", command=led_on_off) #버튼 객체 생성
lbl_display = tk.Label(win, text="LED DISPLAY") #라벨 객체 생성

lbl_display.pack()
btn_on_off.pack(fill='x')

win.mainloop()