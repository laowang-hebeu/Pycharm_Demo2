import re

text = 'alpha. beta...gamma delta'
ree = re.split('[. ]+', text)
print(ree)

reee = re.split('[\. ]+', text,maxsplit = 2)
print(reee)

pat = '[a-zA-Z]+'
reeee = re.findall(pat, text)
print(reeee)

