class LoggerMixin:
    def __new__(cls, *args, **kwargs):
        print(cls)
        return super().__new__(cls)


# class Human
class Human(LoggerMixin):
    def __str__(self):
        return 'Human'
    YEAR = 2023

    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f"Name is - {self.name}, age is - {self.get_age()}"

    def get_age(self):
        return self.YEAR - self.date_of_birth

    def __lt__(self, other):
        return self.date_of_birth < other.date_of_birth

    def __gt__(self, other):
        return self.date_of_birth > other.date_of_birth


# class Planet
class Planet(LoggerMixin):
    def __str__(self):
        return 'Planet'

    def __init__(self, name, humans):
        self.name = name
        self.humans = humans

    def __str__(self):
        return f"Planet is {self.name}"

    def add_human(self, human):
        self.humans.append(human)

    def get_count(self):
        return len(self.humans)

    def __lt__(self, other):
        return len(self.humans) < len(other.humans)

    def __gt__(self, other):
        return len(self.humans) > len(other.humans)


human_1 = Human('Arsenii', 2005)
human_2 = Human('Lera', 2005)
human_3 = Human('Dima', 1980)
print(human_1)
print(human_2)
print(human_3)
planet_1 = Planet('Earth', [human_1, human_2])
planet_2 = Planet('Mars', [human_3])
print(planet_1)
print(planet_2)
print(human_2 < human_3)
print(planet_1 > planet_2)