# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам
# потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи

from typing import List, Callable

def task_manager():
    tasks = []

    def add_task(task: str) -> None:
        tasks.append(task)

    def get_tasks() -> List[str]:
        return tasks

    return add_task, get_tasks

# Приклад використання:
add_task, get_tasks = task_manager()
add_task("Купити молоко")
add_task("Вивчити Python")
print(get_tasks())  # ['Купити молоко', 'Вивчити Python']







# 2) протипізувати перше завдання
from typing import List, Tuple, Callable

def task_manager() -> Tuple[Callable[[str], None], Callable[[], List[str]]]:
    tasks: List[str] = []

    def add_task(task: str) -> None:
        tasks.append(task)

    def get_tasks() -> List[str]:
        return tasks

    return add_task, get_tasks






# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'


def expanded_form(num: int) -> str:
    digits = list(str(num))
    length = len(digits)
    result = [
        str(int(digit) * (10 ** (length - i - 1))) for i, digit in enumerate(digits) if digit != '0'
    ]
    return ' + '.join(result)

# Приклад використання:
print(expanded_form(12))    # '10 + 2'
print(expanded_form(42))    # '40 + 2'
print(expanded_form(70304)) # '70000 + 300 + 4'







# 4) створити декоратор котрий буде підраховувати скільки разів була запущена
# функція продекорована цим декоратором, та буде виводити це значення після виконання функцій

def count_calls_decorator(func: Callable) -> Callable:
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Функція була викликана {count} разів")
        result = func(*args, **kwargs)
        return result.replace('_', ' ')

    return wrapper

@count_calls_decorator
def pr() -> str:
    return 'Hello_boss_!!!'

# Приклад використання:
print(pr())  # 'Hello boss !!!'
print(pr())  # 'Hello boss !!!'






