import re

text = input()
words = text.split()
for word in words:
    if re.match(r'(https?://)?(localhost|[\w.-]+\.\w+)(:\d*)?(/[\w./-]*)?', word.lower()):
        print(word)