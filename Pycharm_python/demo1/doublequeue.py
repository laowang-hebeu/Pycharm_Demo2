from MyQueue import MyQueue

q = MyQueue(range(5))
print(str(q))
print(len(q))

q.appendLeft(-1)
q.appendRight(5)
print(repr(q))
print(len(q))

ql = q.popLeft()
print(ql)
qr = q.popRight()
print(qr)

q.reverse()
print(str(q))

qq = q.isEmpty()
print(qq)

q.rotate(-3)
print(str(q))

q.setSize(20)
print(str(q))

q.clear()
print(str(q))

qqq = q.isEmpty()
print(qqq)