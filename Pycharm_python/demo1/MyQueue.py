class MyQueue:
    def __init__(self,iterable=None,maxlen=10):
        if iterable == None:
            self._content = []
            self._current = 0
        else:
            self._content = list(iterable)
            self._current = len(iterable)
        self._size = maxlen
        if self._size < self._current:
            self._size = self._current

    def __del__(self):
        del self._current

    #修改队列大小
    def setSize(self,size):
        if size < self._current:
            for i in range(size,self._current)[::-1]:
                del self._current[i]
        self._size = size

    #从右侧入队列
    def appendRight(self,v):
        if self._current < self._size:
            self._content.append(v)
            self._current = self._current + 1
        else:
            print('The queue is full')

    #从左侧入队列
    def appendLeft(self,v):
        if self._current < self._size:
            self._content.insert(0,v)
            self._current = self._current + 1
        else:
            print('The queue is full')

    #从右侧出队列
    def popRight(self):
        if self._content:
            self._current = self._current - 1
            return self._content.pop()
        else:
            print('The queue is empty')

    #从左侧出队列
    def popLeft(self):
        if self._content:
            self._current = self._current -1
            return self._content.pop(0)
        else:
            print('The queue is empty')

    #循环移位
    def rotate(self,k):
        if abs(k) > self._current:
            print('k must <= '+str(self._current))
            return
        self._content = self._content[-k:] + self._content[:-k]

    #元素反转
    def reverse(self):
        self._content = self._content[::-1]

    #显示当前队列中元素个数
    def __len__(self):
        return self._current

    #用print()打印对象时，显示当前队列中的元素
    def __str__(self):
        return 'myDueue(' + str(self._content) + ',maxlen='+ str(self._size) + ')'

    __repr__ = __str__

    def clear(self):
        self._content = []
        self._current = 0

    def isEmpty(self):
        return not self._content

    def isFull(self):
        return self._current == self._size

if __name__ == '__name__':
    print('Pls use me as a module')


