import tkinter
import threading
import datetime
import time

app = tkinter.Tk()
app.overrideredirect(True)
app.attributes('-alpha', 0.9)
app.attributes('-topmost', 1)
app.geometry('210x125+800+200')

labelDateTime = tkinter.Label(app)
labelDateTime.pack(fill=tkinter.BOTH,expand=tkinter.YES)
labelDateTime.configure(bg = 'purple')

X = tkinter.IntVar(value=0)
Y = tkinter.IntVar(value=0)

canMove = tkinter.IntVar(value=0)
still = tkinter.IntVar(value=1)

def onLeftButtonDown(event):
    app.attributes('-alpha', 0.4)
    X.set(event.x)
    Y.set(event.y)

    canMove.set(1)

labelDateTime.bind('<Button-1>',onLeftButtonDown)

def onLeftButtonUp(event):
    app.attributes('-alpha', 0.9)

    canMove.set(0)

labelDateTime.bind('<ButtonRelease-1>',onLeftButtonUp)

def onLeftButtonMove(event):
    if canMove.get() == 0:
        return
    newX = app.winfo_x()+(event.x-X.get())
    newY = app.winfo_y()+(event.y-Y.get())

    g = '210x125+'+str(newX)+'+'+str(newY)
    app.geometry(g)

labelDateTime.bind('<B1-Motion>',onLeftButtonMove)

def onRightButtonDown(event):
    still.set(0)
    t.join(0.2)

    app.destroy()

labelDateTime.bind('<Button-3>',onRightButtonDown)


def nowDateTime():
    while still.get() == 1:
        now = datetime.datetime.now()
        s = str(now.year) + '-' + str(now.month) + '-' + str(now.day) + ' '
        s = s + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)

        labelDateTime['text'] = s

        time.sleep(0.5)

t = threading.Thread(target=nowDateTime)
t.daemon = True
t.start()



app.mainloop()
