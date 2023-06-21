# Typification added everywhere.
class Employee:
    def __init__(self, name, salary_for_one_working_day) -> None:
        self.name = name
        self.salary_for_one_working_day = salary_for_one_working_day

    def work(self) -> str:
        return f'I come to the office.'

    def __str__(self) -> str:
        return f"Employee: {self.name}"

    def __lt__(self, other) -> bool:
        return self.salary_for_one_working_day < other.salary_for_one_working_day

    def __gt__(self, other) -> bool:
        return self.salary_for_one_working_day > other.salary_for_one_working_day

    def __eq__(self, other) -> bool:
        return self.salary_for_one_working_day == other.salary_for_one_working_day


class Recruiter(Employee):
    def work(self) -> str:
        return f'I come to the office and start to hiring.'

    def __str__(self) -> str:
        return f"Recruiter: {self.name}"


class Developer(Employee):
    def work(self) -> str:
        return f'I come to the office and start to coding.'

    def __str__(self) -> str:
        return f"Developer: {self.name}"


e1 = Employee('Alex Gid', 1000)
e2 = Employee('Roberto Flamini', 1500)
r1 = Recruiter('Amy Smith', 1500)
d1 = Developer('Vamshikrisha', 2000)

print(e1)
print(e1.work())
print(r1)
print(r1.work())
print(d1)
print(d1.work())
print(e2 > e1)
print(e2 < e1)
print(e2 == e1)