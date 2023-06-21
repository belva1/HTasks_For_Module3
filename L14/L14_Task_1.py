class Telephone:
    def __init__(self, number):
        self.number = number
        self.__counter = 0  # Corrected counter

    def __str__(self) -> str:
        return f"Numbers: {self.number}, calls: {self.__counter}"

    def take_call(self):
        self.__counter += 1

    def get_number_of_calls(self):
        return self.__counter


def count_calls(phones):
    sum_of_calls = 0

    for one_phone in phones:
        sum_of_calls += one_phone.get_number_of_calls()

    return sum_of_calls


cell: Telephone = Telephone('0676890890')
home: Telephone = Telephone('0985486732')
work: Telephone = Telephone('0632456789')


for i in range(10):
    cell.take_call()


for i in range(5):
    home.take_call()


for i in range(33):
    work.take_call()

my_phones = [cell, home, work]

for i in my_phones:
    print(i)
print(f"Amount of calls: {count_calls(my_phones)}")

# "With open", which opens the file just before recording.
with open('output.txt', 'w') as f:
    for i in my_phones:
        f.write(f"{i}\n")
    f.write(f"Amount of calls: {count_calls(my_phones)}")