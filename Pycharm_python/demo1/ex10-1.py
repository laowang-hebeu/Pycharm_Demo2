from os import listdir
from os.path import join,isfile,isdir

def listDirdepthFirst(directory):
    for subPath in listdir(directory):
        path = join(directory,subPath)
        if isfile(path):
            print(path)
        elif isdir(path):
            print(path)
            listDirdepthFirst(path)




listDirdepthFirst('F:\\Pycharm_Demo\\Pycharm_python\\demo1')
