import re

text = 'I am Asad Abbas'

# It will print the list type with am exist in it. If am not exists, it will print the None.

matching = re.findall('am', text)
print(matching)

# It will print the true if the text exists else false

test = re.search('Asad', text)
print(test)

# It will print the None because it is not starting with am

test = re.search('^am',text)
print(test)

# It will print the true because it is starting with I

test = re.search('^I',text)
print(test)

pattern = r'[aeiouAEIOU]'
test = re.findall(pattern, 'education')
print(test)

text = 'Hi, I am Asad Abbas'
print(re.findall(pattern, text))