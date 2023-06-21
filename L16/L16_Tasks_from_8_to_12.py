from datetime import datetime


class Employee:
    def __init__(self, name: str, salary_for_one_working_day: int) -> None:
        self.name = name
        self.salary_for_one_working_day = salary_for_one_working_day

    def __str__(self) -> str:
        return f"Employee: {self.name}, Salary: {self.check_salary()}"

    def __lt__(self, other) -> bool:
        return self.salary_for_one_working_day < other.salary_for_one_working_day

    def __gt__(self, other) -> bool:
        return self.salary_for_one_working_day > other.salary_for_one_working_day

    def __eq__(self, other) -> bool:
        return self.salary_for_one_working_day == other.salary_for_one_working_day

    def work(self) -> str:
        return f'I come to the office.'

    def check_salary(self):
        now = datetime.now()
        cur_day = now.day
        cur_weekday = now.weekday()
        count_workday = 0

        for data in range(cur_day, 0, -1):  # counting work day since this month
            if 0 <= cur_weekday <= 4:  # work day
                count_workday += 1
            cur_weekday -= 1
            if cur_weekday == -1:
                cur_weekday = 6

        return count_workday * self.salary_for_one_working_day


class Recruiter(Employee):
    def work(self) -> str:
        return f'I come to the office and start to hiring.'

    def __str__(self) -> str:
        return f"Recruiter: {self.name}, Salary: {self.check_salary()}."


class Developer(Employee):
    def __init__(self, name: str, salary_for_one_working_day: int, tech_stack: list) -> None:
        super().__init__(name, salary_for_one_working_day)
        self.tech_stack = tech_stack

    def __str__(self) -> str:
        return f"Developer: {self.name}, Salary: {self.check_salary()}, Knowledge: {self.tech_stack}."

    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)

    def __lt__(self, other):
        return len(self.tech_stack) < len(other.tech_stack)

    def __ge__(self, other):
        return len(self.tech_stack) >= len(other.tech_stack)

    def __le__(self, other):
        return len(self.tech_stack) <= len(other.tech_stack)

    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def work(self) -> str:
        return f'I come to the office and start to coding.'


def added_devs(dev1: Developer, dev2: Developer) -> Developer:
    new_name: str = dev1.name + ' ' + dev2.name
    if dev1.salary_for_one_working_day > dev2.salary_for_one_working_day:
        new_salary: int = dev1.salary_for_one_working_day
    else:
        new_salary: int = dev2.salary_for_one_working_day
    new_tech_list: list = list(set(dev1.tech_stack).union(set(dev2.tech_stack)))
    new_dev: Developer = Developer(new_name, new_salary, new_tech_list)
    return new_dev


e1: Employee = Employee('Alex Gid', 100)
e2: Employee = Employee('Roberto Flamini', 150)
r1: Recruiter = Recruiter('Amy Smith', 150)
d1_name_of_technology = ['Python', 'C#']
d1: Developer = Developer('Denys', 190, d1_name_of_technology)
d2_name_of_technology = ['C++', 'Java', 'Ruby']
d2: Developer = Developer('Vamshi', 200, d2_name_of_technology)


print(e1)
print(e2)
print(r1)
print(d1)
print(d2)


if d1 > d2:
    print(f'{d1.name} knows more technologies than {d2.name}.')
else:
    print(f'{d2.name} knows more technologies than {d1.name}.')

if r1 > d1:
    print(f'{r1.name} has bigger salary than {d1.name}.')
else:
    print(f'{d1.name} has bigger salary than {r1.name}.')

print(added_devs(d1, d2))