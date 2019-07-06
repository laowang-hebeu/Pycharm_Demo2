import struct

with open('sample_struct.dat','rb') as f:
    sn = f.read(9)
    n,x,b1 = struct.unpack('if?',sn)
    print('n=',n,'x=',x,'b1=',b1)
    s = f.read(9).decode()
    print('s=',s)
    