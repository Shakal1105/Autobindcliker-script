import keyboard,mouse,time,random,threading
from tkinter import *
from tkinter import messagebox



class Autoclick():
    def __init__(self):
        ################
        self.statusscript1 = "Off"
        self.statusscript2 = "Off"
        #######################
        self.stan = False
        self.stan2 = False
        self.checksecondwindow=0
        self.hotkey = " "
        self.key_1 = "H"
        self.timer = 1
        self.arr = []

        threading.Thread(target=self.scripttimer3, daemon=True, args=()).start()
        threading.Thread(target=self.script, daemon=True, args=()).start()
        threading.Thread(target=self.scriptsecondwindow, daemon=True, args=()).start()
        self.window()

    def window(self):
        window = Tk()
        window.title("config")
        window.resizable(False, False)
        window.wm_geometry("400x350")

        Button(window, text="New alt+tab script", command=lambda : threading.Thread(target=self.secondary_windows, args=()).start()).pack()

        Label(window, text="first window").pack()
        Label(window, text="Бінд на кнопку:").place(x=10, y=50)

        self.hotkey_entry = Entry(window, width=2, font="TimesNewRoman 18 bold")
        self.hotkey_entry.place(y=40, x= 120)

        Label(window, text="Що нажимати постійно \nодна кнопка:").place(x=10, y=100)

        self.bind_1 = Entry(window, width=2, font="TimesNewRoman 18 bold")
        self.bind_1.place(x=150, y=100)

        Label(window, text="Затримка між повторами:\nв секундах").place(x=10, y=170)

        self.timer_entry = Entry(window, width=4, font="TimesNewRoman 18 bold")
        self.timer_entry.place(x=160, y=160)

        Label(window, text="Enable/Disable unban check").place(x=10, y=220)

        self.unbanchecker = IntVar()
        Checkbutton(window, text='unBan Check', variable=self.unbanchecker).place(x=180, y= 230)

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

    def secondary_windows(self):
        self.checksecondwindow=1
        self.root=Tk()
        self.root.geometry("200x150")
        self.root.resizable(False,False)
        Label(self.root, text="1 окно / win+*").pack()
        self.win1 = Entry(self.root)
        self.win1.pack()
        Label(self.root, text="Кнопка").pack()
        self.batton = Entry(self.root)
        self.batton.pack()
        Label(self.root, text="2 окно").pack()
        self.win2 = Entry(self.root)
        self.win2.pack()
        Label(self.root, text="Время в секундах:").pack()
        self.timewin2 = Entry(self.root)
        self.timewin2.pack()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        if messagebox.askokcancel("я думаю да", "Зберегти дані?"):
            self.battonchik = self.batton.get()
            self.wind2 = self.win2.get()
            self.wind1 = self.win1.get()
            self.timerbatonchika = self.timewin2.get()
            self.checksecondwindow = 2
            self.root.destroy()

    def starter(self):
        self.hotkeysettings()

    def stoping(self):
        self.hotkey = " "
        self.start_btn["state"] = "normal"
        self.stop_btn["state"] = "disabled"
        self.stan = False
        self.stan2 = False
        self.stop = "stoping"

    def set_clicker(self):
        self.a = 0
        if self.checksecondwindow == 1 or self.checksecondwindow == 2:
            if self.stan:
                self.stan2 = False
                self.stan = False
            else:
                self.stan2 = True
                self.stan = True

        else:
            if self.stan:
                self.stan = False
            else:
                self.stan = True

    def hotkeysettings(self):
        if self.checksecondwindow == 1:
            self.battonchik = self.batton.get()
            self.wind2 = self.win2.get()
            self.wind1 = self.win1.get()
            self.timerbatonchika = self.timewin2.get()
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
        time.sleep(1)
        self.a=0
        while True:
            if self.stan:
                self.statusscript1 = "On"
                keyboard.send(self.key_1)
                if self.unbanchecker.get() == 1:
                    antiban = random.randint(0,5)/random.randint(10, 100)
                else:
                    antiban=0
                time.sleep(self.timer+antiban)

            else:
                time.sleep(1)
                self.statusscript1 = "Off"

    def scriptsecondwindow(self):
        time.sleep(1)
        while True:
            if self.stan2:
                self.statusscript2 = "On"
                try:
                    self.stan = False
                    keyboard.send(f"Win+{self.wind1}")
                    time.sleep(2)
                    keyboard.send(self.battonchik)
                    time.sleep(2)
                    keyboard.send(f"Win+{self.wind2}")
                    self.stan = True
                    time.sleep(int(self.timerbatonchika))
                except Exception as e:
                    self.error_text["text"] = e
            else:
                self.statusscript2 = "Off"
                time.sleep(5)

    def scripttimer3(self):
        time.sleep(2)
        while True:
            self.error_text["text"] = f"Status windows\nWindow 1 script: {self.statusscript1}\nBaffer Alt+Tab script: {self.statusscript2}"
            time.sleep(3)

if __name__ == "__main__":
    Autoclick()
