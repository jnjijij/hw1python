st = 'as 23 fdfdg544'

numbers = []
current_number = ''

for char in st:
    if char.isdigit():
        current_number += char
    elif current_number:
        numbers.append(current_number)
        current_number = ''


if current_number:
    numbers.append(current_number)

result = ','.join(numbers)
print(result)
