from Stack import Stack

s = Stack()
print(str(s))

s.push(5)
s.push(8)
print(str(s))

ss = s.pop()
print(ss)

s.push('a')

s.setSize(3)

print(str(s))

print(s.isEmpty())
s.push('b')
s.push(8)