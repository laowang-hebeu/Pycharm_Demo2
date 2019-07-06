import struct

n = 1300000000
x = 96.45
b = True
s = 'a1@中国'


sn =struct.pack('if?',n,x,b)
with open('sample_struct.dat','wb') as f:
    f.write(sn)
    f.write(s.encode())