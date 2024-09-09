# - є функція:
# def pr():
#     return 'Hello_boss_!!!'
#  написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і
#  повертає це значення
# функцию pr менять не можно

def replace_decorator(func):
    def wrapper():
        result = func()
        return result.replace('_', ' ')
    return wrapper

@replace_decorator
def pr():
    return 'Hello_boss_!!!'


print(pr())  # 'Hello boss !!!'



# вивести послідовність Фібоначі, кількість вказана в знінній,
#   наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
#   (число з послідовності - це сума попередніх двох чисел)
def fibonacci(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

x = 10
print(fibonacci(x))




# порахувати кількість парних і непарних цифр числа,
#   наприклад: х = 225688 -> п = 5, н = 1;
#          х = 33294 -> п = 2, н = 3
def count(num):
    evens = 0
    odds = 0
    for digit in str(num):
        if int(digit) % 2 == 0:
            evens += 1
        else:
            odds += 1
    return evens, odds

x = 225688
evens, odds = count(x)
print(f"Парні: {evens}, Непарні: {odds}")





# прога, що виводить кількість кожного символа з введеної строки,
# наприклад:
# st = 'as 23 fdfdg544'  # введена строка
#
# 'a' -> 1  # вивело в консолі
# 's' -> 1
# ' ' -> 2
# '2' -> 1
# '3' -> 1
# 'f' -> 2
# 'd' -> 2
# 'g' -> 1
# '5' -> 1
# '4' -> 2

from collections import Counter

def count_characters(st):
    counter = Counter(st)
    for char, count in counter.items():
        print(f"'{char}' -> {count}")

st = 'as 23 fdfdg544'
count_characters(st)





# створити декоратор який буде рахувати кількість запущених функцій продекорованих цим декоратором
def count_decorator(func):
    func.call_count = 0

    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"Функція була викликана {wrapper.call_count} разів")
        return func(*args, **kwargs)

    wrapper.call_count = 0
    return wrapper

@count_decorator
def example_function():
    print("......")


example_function()
example_function()
example_function()
