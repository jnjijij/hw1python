import re

st = 'as 23 fdfdg544 34'
numbers = re.findall(r'\d+', st)
print(', '.join(numbers))