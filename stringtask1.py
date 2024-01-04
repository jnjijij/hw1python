st = 'as 23 fdfdg544'

numbers = []
current_number = ''

for char in st:
    if char.isdigit():
        current_number += char
    elif current_number:
        numbers.append(current_number)
        current_number = ''

# Adding the last number if there's any
if current_number:
    numbers.append(current_number)

numbers.append('33')   # Add '33' to the list

result = ','.join(numbers)
print(result)
