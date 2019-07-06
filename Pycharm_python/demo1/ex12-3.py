import os
import tkinter
import tkinter.simpledialog
import tkinter.colorchooser
import tkinter.filedialog

from PIL import ImageGrab

root = tkinter.Tk()
root.title('My paint----by Lao Wang')
root['width'] = 800
root['height'] = 600

canDraw = tkinter.IntVar(value=0)
what = tkinter.IntVar(value=1)

X = tkinter.IntVar(value=0)
Y = tkinter.IntVar(value=0)

foreColor = '#000000'
backColor = '#FFFFFF'

image = tkinter.PhotoImage()
canvas = tkinter.Canvas(root, bg='white', width=800, height=600)
canvas.create_image(800,600,image=image)

def onLeftButtonDown(event):
    canDraw.set(1)
    X.set(event.x)
    Y.set(event.y)
    if what.get()==4:
        canvas.create_text(event.x,event.y,text=text)

canvas.bind('<Button-1>',onLeftButtonDown)

lastDraw = 0

def onLeftButtonMove(event):
    global lastDraw
    if canDraw.get() == 0:
        return

    if what.get()==1:
        canvas.create_line(X.get(),Y.get(),event.x,event.y,fill=foreColor)
        X.set(event.x)
        Y.set(event.y)
    elif what.get()==2:
        try:
            canvas.delete(lastDraw)
        except Exception as e:
            pass
        lastDraw = canvas.create_line(X.get(),Y.get(),event.x,event.y,fill=foreColor)
    elif what.get()==3:
        try:
            canvas.delete(lastDraw)
        except Exception as e:
            pass
        lastDraw = canvas.create_rectangle(X.get(),Y.get(),event.x,event.y,fill=foreColor,outline=foreColor)
    elif what.get()==5:
        canvas.create_rectangle(event.x-5, event.y-5, event.x+5, event.y+5, fill=backColor, outline=backColor)

canvas.bind('<B1-Motion>', onLeftButtonMove)

def onLeftButtonUp(event):
    if what.get()==2:
        canvas.create_line(X.get(),Y.get(),event.x,event.y,fill=foreColor)
    elif what.get()==3:
        canvas.create_rectangle(X.get(), Y.get(), event.x, event.y, fill=foreColor, outline=foreColor)
    canDraw.set(0)
    global lastDraw
    lastDraw = 0

canvas.bind('<ButtonRelease-1>', onLeftButtonUp)


#--------------------------------------------------------------------
menu = tkinter.Menu(root,tearoff=0)
def Open():
    filename = tkinter.filedialog.askopenfilename(title='Open Image',filetypes=[('image','*jpg *.png *.gif')])
    if filename:
        global  image
        image = tkinter.PhotoImage(file=filename)
        canvas.create_image(80,80,image=image)

menu.add_command(label='Open',command=Open)


def Save():
    left = int(root.winfo_rootx())
    top = int(root.winfo_rooty())
    width = root.winfo_width()
    height = root.winfo_height()
    im = ImageGrab((left,top,left+width,top+height))

    filename = tkinter.filedialog.asksaveasfilename(title='保存图片',filename=[('图片文件','*.png')])
    if not filename:
        return
    if not filename.endswith('.png'):
        filename = filename+'.png'
    im.save(filename)

menu.add_command(label = 'Save', command = Save)

def Clear():
    for item in canvas.find_all():
        canvas.delete(item)

menu.add_command(label='Cear',command=Clear)

#-----------------------------------
menu.add_separator()

menuType = tkinter.Menu(menu,tearoff=0)

def drawCurve():
    what.set(1)
menuType.add_command(label='Curve',command=drawCurve)

def drawLine():
    what.set(2)
menuType.add_command(label='Line',command=drawLine)

def drawRectangle():
    what.set(3)
menuType.add_command(label='Rectangle',command=drawRectangle)

def drawText():
    global text
    text = tkinter.simpledialog.askstring(title='Input what you want to draw',prompt='')
    what.set(4)
menuType.add_command(label='Text',command=drawText)


#-----------------------------------
menuType.add_separator()

def chooseForeColor():
    global foreColor
    foreColor = tkinter.colorchooser.askcolor()[1]
menuType.add_command(label='Choose Foreground Color',command=chooseForeColor)

def chooseBackColor():
    global backColor
    foreColor = tkinter.colorchooser.askcolor()[1]
menuType.add_command(label='Choose Background Color', command=chooseBackColor)

def onErase():
    what.set(5)
menuType.add_command(label='Erase',command=onErase)

menu.add_cascade(label='Type',menu=menuType)

def onRightButtonUP(event):
    menu.post(event.x_root,event.y_root)

canvas.bind('<ButtonRelease-3>',onRightButtonUP)

canvas.pack(fill=tkinter.BOTH,expand=tkinter.YES)


root.mainloop()
