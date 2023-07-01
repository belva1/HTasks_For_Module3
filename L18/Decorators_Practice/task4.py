# Створіть декоратор, який перевіряє результат функції, якщо він менший 0, то декоратор повертає 0,
# в іншоум випадку повертає результат функції

def check_result(func):
    def wrapper(*args):
        result = func(*args)
        if result <= 0:
            return 0
        else:
            return result
    return wrapper


@check_result
def add(a, b):
    return a+b


print(add(1, 0))