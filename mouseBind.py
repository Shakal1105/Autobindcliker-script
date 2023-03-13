from pynput import mouse
import keyboard
from tkinter import *
from tkinter import messagebox
import threading

a=0

button_list = "x1"
bind_num = "1"

def on_move(x, y):
    pass

def on_click(x, y, button, pressed):
    buttons = f"{button}"
    if buttons == f"Button.{button_list}":
        print(11)
        global a
        if a == 0:
            a=1
            keyboard.send(bind_num)
        else:
            a=0

def on_scroll(x, y, dx, dy):
    pass


def prog():
    with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
            listener.join()

ss = threading.Thread(target=prog, args=(), daemon=True)
ss.start()

window = Tk()
Label(window, text="use mouse for play, bind on mouse button X1 on side mouse\nUse txt for test\By Shakal").pack()

Label(window, text="кнопка мишки, наприклад: left, right, middle, x1, x2...").pack(side="left")
num_mouse = Entry(window)
num_mouse.pack(side="right")
Label(window).pack()
Label(window).pack()
Label(window).pack()
Label(window, text="какую кнопку нажимать в игре пример: F1, 1, H...").pack(side="left")
key_num =  Entry(window)
key_num.pack(side="right")
def settings():
    global button_list, bind_num
    button_list = num_mouse.get()
    bind_num = key_num.get()

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
        quit()
Label(window).pack()
Label(window).pack()
Label(window).pack()
Button(window, text="Create", command=settings).pack()

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()

