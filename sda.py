from pynput import mouse
import keyboard
from tkinter import *
from tkinter import messagebox
import threading

a=0

def on_move(x, y):
    pass

def on_click(x, y, button, pressed):
    if button == button.x1:
        global a
        if a == 0:
            a=1
            keyboard.send("1")
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

ss = threading.Thread(target=prog, args=())
ss.start()

window = Tk()
Label(window, text="use mouse for play, bind on mouse button X1 on side mouse\nUse txt for test\By Shakal").pack()

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        quit()

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()

