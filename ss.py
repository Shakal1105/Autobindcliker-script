from pynput import mouse
import keyboard

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

# Collect events until released
with mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll) as listener:
    listener.join()
