import csv


class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def to_csv_row(self):
        return [self.name, str(self.age), self.country]

    @staticmethod
    def from_csv_row(row):
        name, age, country = row
        return Person(name, int(age), country)

    @staticmethod
    def write_to_csv(people, fields, filename):
        try:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(fields)
                for person in people:
                    writer.writerow(person.to_csv_row())
            print(f"Data written to '{filename}' successfully.")
        except IOError:
            print(f"Error writing to file '{filename}'.")

    @staticmethod
    def read_from_csv(filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                people = []
                count = 0
                for row in reader:
                    if count == 0:
                        count += 1
                        continue
                    person = Person.from_csv_row(row)
                    people.append(person)

                return people
        except FileNotFoundError:
            print(f"File '{filename}' not found.")


people = [
    Person('John', 25, 'USA'),
    Person('Emma', 30, 'Canada'),
    Person('Michael', 35, 'Australia')
]

Person.write_to_csv(people, ["name", "age", "country"], 'people.csv')

people_from_csv = Person.read_from_csv('people.csv')
for person in people_from_csv:
    print(person.name, person.age, person.country)

