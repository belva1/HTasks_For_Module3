# EXAMPLE 1 FROM LESSON 14
class Car:
    color = 'red'

    _top_speed = 250
    __max_carrying = 1000

    def find_color_and_top_speed(self):
        return 'this car top speed is {} and color is {}'.format(self._top_speed, self.color)

    def is_can_go_with_needed_speed(self, speed):
        return speed < self._top_speed

    def is_can_get_weight(self, weight):
        return self.__max_carrying > weight

    def change_max_carrying(self, new_carrying):
        self.__max_carrying = new_carrying

    def __private_method(self):
        print('this is private method')

    def _this_is_protected_method(self):
        print('this is protected method')

    def run_hidden_and_protected_methods(self):
        self.__private_method()
        self._this_is_protected_method()


car = Car()
# car.color  # все нормально
# car._top_speed  # спрацює, але ми самі описали цю властивість так що б повідомити, що не треба так його використовувати
# car.__max_carrying  # не спрацює (буде помилка, що цей атрибут не знайдено)
# car._Car__max_carrying  # Спрацює і це якраз опис того, що дістатися можна куди завгодно. Але сам синтаксис нам каже, що ми щось робимо
# car.__max_carrying = 800  # не спрацює
# car.change_max_carrying(800)  # спрацює
# сar.__hidden_method()  # не спрацює (буде помилка, що цього методу не існує)
# car._this_is_protected_method()  # спрацює, але знову ж таки не треба цього робити
# car.run_hidden_and_protected_methods()  # спрацює та викличе захищений та приватний методи


# EXAMPLE 2 FROM LESSON 14


class Animal:
    name = ''

    def get_name(self):
        return self.name


class Dog(Animal):
    breed = ''

    def get_breed(self):
        return self.breed


dog = Dog()
dog.name = 'Bob'
dog.breed = 'doberman'

print(dog.get_name())  # Bob
print(dog.get_breed())  # doberman


# EXAMPLE 3 FROM LESSON 14

class PriceCounter:
    price = 100

    def calculate_price(self):
        print('In original price')
        return self.price


class DiscountCounter(PriceCounter):

    def calculate_price(self):
        print('In discount calculate')
        return super().calculate_price() * 0.8


class SuperDiscountCounter(DiscountCounter):

    def calculate_price(self):
        print('In super discount calculate')
        return super().calculate_price() * 0.8


price_counter = PriceCounter()
discount_counter = DiscountCounter()
super_discount_counter = SuperDiscountCounter()

print(price_counter.calculate_price())
""" In original price 100 """
print(discount_counter.calculate_price())
""" In discount calculate In original price 80.0 """
print(super_discount_counter.calculate_price())
""" In super discount calculate In discount calculate In original price 64.0 """


# EXAMPLE 4 FROM LESSON 14
class Animal:

    def say(self):
        ...


class Dog(Animal):

    def say(self):
        return f'woof'


class Cat(Animal):
    def say(self):
        return f'meow'


dog = Dog()
cat = Cat()

print(dog.say())  # woof
print(cat.say())  # meow

animals = (dog, cat)
for animal in animals:
    print(animal.say())

