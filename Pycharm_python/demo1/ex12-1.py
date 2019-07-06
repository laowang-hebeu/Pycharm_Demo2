import tkinter
import tkinter.messagebox
import os
import os.path

path = os.getenv('temp')
filename = os.path.join(path,'info.txt')


root = tkinter.Tk()

root['height'] = 140
root['width'] = 200

labelName = tkinter.Label(root, text='User Name:', justify=tkinter.RIGHT, anchor = 'e', width=80)
labelName.place(x=10, y=5,width=80,height=20)

varName = tkinter.StringVar(root, value='')
entryName = tkinter.Entry(root,width=80,textvariable=varName)
entryName.place(x=100,y=5,width=80,height=20)



labelPwd = tkinter.Label(root, text='User Pwd:', justify=tkinter.RIGHT, anchor = 'e', width=80)
labelPwd.place(x=10, y=30,width=80,height=20)

varPwd = tkinter.StringVar(root, value='')
entryPwd = tkinter.Entry(root,show='*',width=80,textvariable=varPwd)
entryPwd.place(x=100,y=30,width=80,height=20)


try:
    with open(filename) as fp:
        n,p = fp.read().strip().split(',')
        varName.set(n)
        varPwd.set(p)
except:
    pass


remeberMe = tkinter.IntVar(root, value=1)
checkRemeber = tkinter.Checkbutton(root,text='Remeber me?',variable=remeberMe,onvalue=1,offvalue=0)
checkRemeber.place(x=30,y=70,width=120,height=20)


def login():
    name = entryName.get()
    pwd = entryPwd.get()

    if name == 'admin' and pwd =='123456':
        tkinter.messagebox.showinfo(title='恭喜',message='登录成功！')

        if remeberMe.get() == 1:
            with open(filename,'w') as fp:
                fp.write(','.join((name,pwd)))
        else:
            try:
                os.remove(filename)
            except:
                pass
    else:
        tkinter.messagebox.showinfo('警告',message='用户名或密码错误')


buttonOk = tkinter.Button(root,text='Login',command=login)
buttonOk.place(x=30,y=100,width=50,height=20)

def cancel():
    varName.set('')
    varPwd.set('')


buttonCancel = tkinter.Button(root,text='Cancel',command=cancel)
buttonCancel.place(x=90,y=100,width=50,height=20)


root.mainloop()