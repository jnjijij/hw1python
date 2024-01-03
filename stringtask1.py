import re

st = 'as 23 fdfdg544'
numbers = re.findall(r'\d+', st)
result = ','.join(numbers)
print(result)