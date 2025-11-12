import tkinter as tk

def led_on():
    #print("LED 켜짐")
    lbl_display.config(text="LED 켜짐")  #밑이 아니라 버튼창에 뜨도록 함
def led_off():
    #print("LED 켜짐")
    lbl_display.config(text="LED 꺼짐")

win = tk.Tk()  #윈도우 객체 생성
win.title("GUI")
win.geometry("400x200")
win.resizable(False,False)

btn_on = tk.Button(win, text="LED ON", command=led_on) #버튼 객체 생성
btn_off = tk.Button(win, text="LED OFF", command=led_off)
lbl_display = tk.Label(win, text="LED DISPLAY") #라벨 객체 생성

lbl_display.pack()
btn_on.pack(fill='x')
btn_off.pack(fill='x') 

win.mainloop()



#import tkinter as tk

#win = tk.Tk()
#win.title("GUI")
#win.geometry("400x200")
#win.resizable(False,False)

#btn_test = tk.Button(win, text="IoT GUI 실습중...")
#btn_test.pack()

#win.mainloop()