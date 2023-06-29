from datetime import datetime

import csv

import logging

logging.basicConfig(
    level=logging.INFO,
    filename="log_email.log",
    filemode="w",
    format="%(asctime)s %(levelname)s %(message)s")


class EmailAlreadyExistsException(Exception):
    pass


class SaveEmail:
    def __init__(self, file_info):
        self.file_info = file_info
        with open(file_info, 'w', newline='') as file:
            writer = csv.writer(file, lineterminator="\r")
            writer.writerow(["Name", "Salary", "Email"])  # will be written only once when created.

    def validate(self, email):
        with open(self.file_info, 'r') as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                try:
                    if email in row:  # row takes the whole string.
                        raise EmailAlreadyExistsException(f"{email} - this email is already in use.")
                except EmailAlreadyExistsException:
                    logging.exception(f"{email} - this email is already in use.")
            # якщо у вас будуть advices щодо переробки процесу логування, будь ласка, підкажіть.
            # я розумію, що не дуже логічно перехоплювати raise :с

    def save(self, emp):
        with open(self.file_info, 'a', newline='') as file:
            writer = csv.writer(file, lineterminator="\r")
            writer.writerow([
                emp.name,
                emp.salary_for_one_working_day,
                emp.email
            ])


class Employee:
    def __init__(self, name, salary_for_one_working_day, email, save_email: SaveEmail):
        self.name = name
        self.salary_for_one_working_day = salary_for_one_working_day
        self.save_email = save_email
        self.save_email.validate(email)
        self.email = email
        self.save_email.save(self)

    def __str__(self):
        return f"Employee: {self.name}, Salary: {self.check_salary()}"

    def __lt__(self, other):
        return self.salary_for_one_working_day < other.salary_for_one_working_day

    def __gt__(self, other):
        return self.salary_for_one_working_day > other.salary_for_one_working_day

    def __eq__(self, other):
        return self.salary_for_one_working_day == other.salary_for_one_working_day

    def work(self):
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
    def work(self):
        return f'I come to the office and start to hiring.'

    def __str__(self):
        return f"Recruiter: {self.name}, Salary: {self.check_salary()}."


class Developer(Employee):
    def __init__(self, name, salary_for_one_working_day, email, save_email, tech_stack: list):
        super().__init__(name, salary_for_one_working_day, email, save_email)
        self.tech_stack = tech_stack

    def __str__(self):
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

    def work(self):
        return f'I come to the office and start to coding.'


def added_devs(dev1: Developer, dev2: Developer) -> Developer:
    new_name = dev1.name + ' ' + dev2.name
    if dev1.salary_for_one_working_day > dev2.salary_for_one_working_day:
        new_salary = dev1.salary_for_one_working_day
    else:
        new_salary = dev2.salary_for_one_working_day
    new_tech_list = list(set(dev1.tech_stack).union(set(dev2.tech_stack)))
    new_dev: Developer = Developer(new_name, new_salary, new_tech_list)
    return new_dev


save_email = SaveEmail("file_info.csv")

emp1 = Employee('Valeriya Belyayeva', 20, '848belval848@gmail.com', save_email)
dev1_name_of_technology = ['Python', 'C#']
dev1 = Developer('Sua Like', 50, 'sualkeee200@soccerjh.com', save_email, dev1_name_of_technology)
rec1 = Recruiter('Lili Lula', 25, 'bholu1@psmscientific.com', save_email)
emp2 = Employee('Init Turbo', 20, 'gtyrbyf88@forward4families.org', save_email)
emp3 = Employee('Brittney Skil', 20, 'brittney36@ccategoryk.com', save_email)
emp4 = Employee('Brittney Well', 20, 'brittney36@ccategoryk.com', save_email)
emp5 = Employee('Brittney Sell', 20, 'brittney36@ccategoryk.com', save_email)