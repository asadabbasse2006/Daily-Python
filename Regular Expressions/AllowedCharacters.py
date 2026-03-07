import re

def check(string):
    pattern = re.compile(r'[^a-zA-Z0-9]')
    stri = pattern.search(string)

    return not bool(stri)

print(check('education'))
print(check('education%-'))