# Створіть декоратор, який логує(print) винятки, що виникають під час виконання функції.

def log_exp(func):
    def wrapper(*args):
        try:
            return func(*args)
        except ZeroDivisionError as err:
            return err
    return wrapper


@log_exp
def divide(a, b):
    return a / b


print(divide(1, 0))