# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
# #################################################################################

st = 'as 23 fdfdg544'
numbers1 = ','.join([num for num in st if num.isdigit()])
print(numbers1)





# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі
# #################################################################################

import re
st = 'as 23 fdfdg544 34'
numbers2 = ', '.join(re.findall(r'\d+', st))
print(numbers2)





# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

list1 = 'Hello, world'
upper_list1 = [char.upper() for char in list1]
print(upper_list1)






# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

squares = [x**2 for x in range(51) if x % 2 != 0]
print(squares)








# function
#
# - створити функцію яка виводить ліст
def print_list(lst):
    print(lst)

print_list([1, 2, 3, 4])




# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def max_of_all(a, b, c):
    return max(a, b, c)


print(max_of_all(2, 1, 3))




# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def min_max(*numbers):
    print(max(numbers))
    return min(numbers)

min_value = min_max(2, 10, 8, 200, 1)
print(min_value)




# - створити функцію яка повертає найбільше число з ліста
def max_in_list(lst):
    return max(lst)

print(max_in_list([1, 5, 10, 2, 7]))





# - створити функцію яка повертає найменьше число з ліста
def min_in_list(lst):
    return min(lst)

# Приклад використання:
print(min_in_list([1, 5, 10, 2, 7]))





# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
def sum_of_list(lst):
    return sum(lst)

print(sum_of_list([1, 2, 3, 4, 5]))





# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
def average_of_list(lst):
    return sum(lst) / len(lst)

print(average_of_list([1, 2, 3, 4, 5]))



################################################################################################
# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
#   - видалити усі дублікати
#   - замінити кожне 4-те значення на 'X'

lst = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


min_value = min(lst)
print("Мінімальне число:", min_value)


lst_no_duplicates = list(set(lst))
print("Список без дублікатів:", lst_no_duplicates)


for i in range(3, len(lst), 4):
    lst[i] = 'X'
print("Модифікований список:", lst)






# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def print_square(size):
    for i in range(size):
        if i == 0 or i == size - 1:
            print('*' * size)
        else:
            print('*' + ' ' * (size - 2) + '*')

print_square(5)




# 3) вывести табличку множення за допомогою цикла while

i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(f"{i * j:4}", end="")
        j += 1
    print()
    i += 1


# 4) переробити це завдання під меню
def menu():
    lst = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

    while True:
        print("1. Знайти мінімальне число")
        print("2. Видалити дублікати")
        print("3. Замінити кожне 4-те значення на 'X'")
        print("4. Вивести пустий квадрат з '*'.")
        print("5. Вивести табличку множення")
        print("6. Вийти")
        choice = input("Виберіть опцію: ")

        if choice == '1':
            # Фільтруємо список, залишаючи лише числа
            numeric_lst = [x for x in lst if isinstance(x, int)]
            print("Мінімальне число:", min(numeric_lst))

        elif choice == '2':
            lst = list(set(lst))
            print("Список без дублікатів:", lst)

        elif choice == '3':
            for i in range(3, len(lst), 4):
                lst[i] = 'X'
            print("Модифікований список:", lst)

        elif choice == '4':
            size = int(input("Введіть розмір квадрата: "))
            for i in range(size):
                if i == 0 or i == size - 1:
                    print('*' * size)
                else:
                    print('*' + ' ' * (size - 2) + '*')

        elif choice == '5':
            i = 1
            while i <= 10:
                j = 1
                while j <= 10:
                    print(f"{i * j:4}", end="")
                    j += 1
                print()
                i += 1

        elif choice == '6':
            print("Програма завершена.")
            break

        else:
            print("Неправильний вибір, спробуйте ще раз.")

menu()
