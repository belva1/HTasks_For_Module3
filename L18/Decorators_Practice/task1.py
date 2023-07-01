# Задача про логування:
# Розробіть декоратор, який реєструє інформацію про виклик функції і її
# аргументи, а також результат виконання.

def info(func):
    def arguments(a, b):
        print("CALL FUNCTION")
        print("Args: ", a, b)
        print("Result: ", func(a, b))  # те саме, що й add
        print("END")
    return arguments


@info
def add(a, b):
    return a+b


add(5, 5)

