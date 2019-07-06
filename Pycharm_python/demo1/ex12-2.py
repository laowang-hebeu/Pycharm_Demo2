import tkinter
import tkinter.messagebox
import tkinter.ttk

root = tkinter.Tk()
root.title('Selection widgets')
root['height'] = 400
root['width'] = 320

varName = tkinter.StringVar()
varName.set('')

labelName = tkinter.Label(root, text='Name:',justify=tkinter.RIGHT,width=50)
labelName.place(x=10,y=5,width=50,height=20)

entryName = tkinter.Entry(root, width=120, textvariable=varName)
entryName.place(x=70,y=5,width=120,height=20)

labelGrade = tkinter.Label(root, text='Grade:',justify=tkinter.RIGHT,width=50)
labelGrade.place(x=10,y=40,width=50,height=20)

studentClasses = {'1':['1','2','3','4'],'2':['1','2'],'3':['1','2','3']}

comboGrade = tkinter.ttk.Combobox(root,width=50,values=tuple(studentClasses.keys()))
comboGrade.place(x=70,y=40,width=50,height=20)

def  comboChange(event):
    grade = comboGrade.get()
    if grade:
        comboClass['values'] = studentClasses.get(grade)
    else:
        comboGrade.set([])
comboGrade.bind('<<ComboboxSelected>>',comboChange)

labelClass = tkinter.Label(root, text='Class:',justify=tkinter.RIGHT,width=50)
labelClass.place(x=130,y=40,width=50,height=20)

comboClass = tkinter.ttk.Combobox(root,width=50)
comboClass.place(x=190,y=40,width=50,height=20)

labelSex = tkinter.Label(root, text='Sex:',justify=tkinter.RIGHT,width=50)
labelSex.place(x=10,y=70,width=50,height=20)

sex = tkinter.IntVar()
sex.set(1)

radioMan = tkinter.Radiobutton(root, variable=sex,value=1,text='Man')
radioMan.place(x=70,y=70,width=50,height=20)

radioWoman = tkinter.Radiobutton(root, variable=sex,value=0,text='Woman')
radioWoman.place(x=130,y=70,width=70,height=20)

monitor = tkinter.IntVar()
monitor.set(0)

checkMonitor = tkinter.Checkbutton(root,text='Is monitor?',variable=monitor,onvalue=1,offvalue=0)
checkMonitor.place(x=20,y=100,width=100,height=20)

def addInformation():
    result = 'Name:'+entryName.get()
    result = result + ';Grade:' + comboGrade.get()
    result = result + ';Class:' + comboClass.get()
    result = result + ';Sex:' + ('Man' if sex.get() else 'Woman')
    result = result + ';Monitor:' + ('Yes' if monitor.get() else 'No')

    listboxStudents.insert(0,result)

buttonAdd = tkinter.Button(root, text='Add',width=40,command=addInformation)
buttonAdd.place(x=130,y=100,width=40,height=20)

def deleteSelection():
    selection = listboxStudents.curselection()
    if not selection:
        tkinter.messagebox.showinfo(title='Information',message='No Selection')
    else:
        listboxStudents.delete(selection)

buttonDelete = tkinter.Button(root,text='DeleteSelection',width=100,command=deleteSelection)
buttonDelete.place(x=180,y=100,width=100,height=20)

listboxStudents = tkinter.Listbox(root,width=300)
listboxStudents.place(x=10,y=130,width=300,height=200)


root.mainloop()
