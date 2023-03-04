import keyboard
import mouse
from tkinter import *
import time
import random
import threading

class Autoclick():
    def __init__(self):
        self.stan = False
        self.hotkey = " "
        self.key_1 = "H"
        self.timer = 1
        self.arr = []

        threading.Thread(target=self.script, daemon=True, args=()).start()
        self.window()

    def window(self):
        window = Tk()
        window.title("config")
        window.resizable(False, False)
        window.wm_geometry("400x300")

        Label(window, text="first window").pack()
        Label(window, text="Бінд на кнопку:").place(x=10, y=30)

        self.hotkey_entry = Entry(window, width=2, font="TimesNewRoman 18 bold")
        self.hotkey_entry.place(y=20, x= 120)

        Label(window, text="Що нажимати постійно \nодна кнопка:").place(x=10, y=80)

        self.bind_1 = Entry(window, width=2, font="TimesNewRoman 18 bold")
        self.bind_1.place(x=150, y=80)

        Label(window, text="Затримка між повторами:\nв секундах").place(x=10, y=150)

        self.timer_entry = Entry(window, width=4, font="TimesNewRoman 18 bold")
        self.timer_entry.place(x=160, y=140)

        ButtonFrame = Frame(window)
        ButtonFrame.pack(side="bottom", anchor="e")

        self.error_text = Label(ButtonFrame, text='', fg="red")
        self.error_text.pack(side="left")
        self.start_btn = Button(ButtonFrame, text="Start", width=10, state="normal", bg="green",
                                font="TimesNewRoman 10 bold", fg="yellow", command=self.starter)
        self.start_btn.pack(side="right", pady=10, padx=10)
        self.stop_btn = Button(ButtonFrame, text="Stop", width=10, state="disabled", bg="crimson",
                               font="TimesNewRoman 10 bold", fg="yellow", command=self.stoping)
        self.stop_btn.pack(side="right", pady=10, padx=10)
        window.mainloop()

    def starter(self):
        self.hotkeysettings()

    def stoping(self):
        self.hotkey = " "
        self.start_btn["state"] = "normal"
        self.stop_btn["state"] = "disabled"
        self.stan = False
        self.stop = "stoping"

    def set_clicker(self):
        if self.stan:
            self.stan = False
            print("off")
        else:
            self.stan = True
            print("on")

    def hotkeysettings(self):
        self.hotkey = self.hotkey_entry.get()
        self.hotkey_entry.delete(1, END)
        try:
            if self.hotkey[0] in self.arr:
                self.start_btn["state"] = "disabled"
                self.stop_btn["state"] = "normal"
            else:
                self.hotkey_entry["state"] = "disabled"
                self.arr.append(self.hotkey[0])
                keyboard.add_hotkey(self.hotkey[0], self.set_clicker)
                self.start_btn["state"]="disabled"
                self.stop_btn["state"]="normal"
            self.key_1 = self.bind_1.get()
            self.timer = int(self.timer_entry.get())
        except Exception as e:
            self.error_text["text"]=e

    def script(self):
        while True:
            if self.stan:
                keyboard.send(self.key_1)
                antiban = random.randint(0,5)/random.randint(10, 100)
                time.sleep(self.timer+antiban)

            else:
                time.sleep(5)

if __name__ == "__main__":
    Autoclick()