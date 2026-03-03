import re

text = 'I am Asad Abbas'
matching = re.findall('am', text)
print(matching)

test = re.search('Asad', text)
print(test)