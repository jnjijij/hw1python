my_list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

# Знайти мінімальне число
min_value = min(my_list)
print(f"Мінімальне число: {min_value}")

# Видалити усі дублікати
unique_list = list(set(my_list))
print(f"Список без дублікатів: {unique_list}")

# Замінити кожне 4-те значення на 'X'
modified_list = [val if (i + 1) % 4 != 0 else 'X' for i, val in enumerate(my_list)]
print(f"Список замінений на 'X' на кожному 4-тому місці: {modified_list}")



def draw_empty_square(side_length):
    if side_length <= 0:
        print("Сторона квадрата повинна бути більше 0.")
        return

    for i in range(side_length):
        if i == 0 or i == side_length - 1:
            # Верхня та нижня сторона квадрата
            print('* ' * side_length)
        else:
            # Бічні сторони квадрата
            print('* ' + '  ' * (side_length - 2) + '*')

# Приклад виклику:
side = int(input("Введіть сторону квадрата: "))
draw_empty_square(side)





def multiplication_table(n):
    i = 1
    while i <= n:
        j = 1
        while j <= 10:
            result = i * j
            print(f"{i} * {j} = {result}")
            j += 1
        i += 1

# Введення значення для таблички множення
table_size = int(input("Введіть розмір таблички множення: "))
multiplication_table(table_size)






def find_min_number(my_list):
    return min(my_list)

def remove_duplicates(my_list):
    return list(set(my_list))

def replace_every_fourth_with_x(my_list):
    modified_list = [val if (i + 1) % 4 != 0 else 'X' for i, val in enumerate(my_list)]
    return modified_list

# Функція для виведення меню
def menu(my_list):
    while True:
        print("\nМеню:")
        print("1. Знайти мінімальне число")
        print("2. Видалити дублікати")
        print("3. Замінити кожне 4-те значення на 'X'")
        print("4. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            print(f"Мінімальне число: {find_min_number(my_list)}")
        elif choice == '2':
            print(f"Список без дублікатів: {remove_duplicates(my_list)}")
        elif choice == '3':
            modified_list = replace_every_fourth_with_x(my_list)
            print(f"Список замінений на 'X' на кожному 4-тому місці: {modified_list}")
        elif choice == '4':
            break
        else:
            print("Неправильний вибір. Спробуйте знову.")

# Приклад виклику:
my_list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
menu(my_list)
