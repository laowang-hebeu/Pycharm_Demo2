class Stack:
    def __init__(self,maxlen = 10):
        self._content = []
        self._current = 0
        self._size = maxlen

    def __del__(self):
        del self._content

    def clear(self):
        self._content = []
        self._current = 0

    def isEmpty(self):
        return not self._content

    def isFull(self):
         return self._current == self._size

    def setSize(self,size):
        if size < self._current:
            print('new size must >= ' + str(self._current))
            return
        self._size = size

    def push(self,v):
        if self._current < self._size:
            self._content.append(v)
            self._current = self._current + 1
        else:
            print('Stack Full')

    def pop(self):
        if self._content:
            self._current = self._current - 1
            return self._content.pop()
        else:
            print('Stack is empty')

    def __str__(self):
        return 'Stack(' + str(self._content) + ',maxlen=' + str(self._size) + ')'

    __repr__ = __str__
