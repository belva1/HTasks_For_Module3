# Задача про вимірювання часу виконання функції:
# Напишіть декоратор, який вимірює час виконання функції і виводить його на екран.

import time


def log_time(func):
    def wrapper(*args):
        print("START FUNC")
        a = time.time()  # початок виклику
        result = func(*args)
        b = time.time()
        print("EXECUTION TIME", b-a)
        return result
    return wrapper


@log_time
def fac(num):
    time.sleep(2)
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


print(fac(6))