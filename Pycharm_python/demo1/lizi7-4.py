from random import choice
from string import ascii_letters, digits
from pypinyin import lazy_pinyin, pinyin


characters = digits + ascii_letters


def crypt(source, key):
    from itertools import cycle
    func = lambda x, y: chr(ord(x)^ord(y))
    return ''.join(map(func, source, cycle(key)))

def generatepassword(n):
    return ''.join((choice(characters) for _ in range(n)))


print(generatepassword(8))
print(generatepassword(15))
print('hello world')
print(lazy_pinyin('东付过'))

source = 'Beautiful is better than ugly.'
key = 'Python'

print('\nBefore Encrypted:'+source)
encrypted = crypt(source, key)
print('After Encrypted:' + encrypted)
decrypted = crypt(encrypted, key)
print('After Decrypted:' + decrypted)



