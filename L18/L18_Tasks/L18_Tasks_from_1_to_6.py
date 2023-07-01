import requests
import csv


class Candidate:
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 email: str,
                 tech_stack: list,
                 main_skill: str,
                 main_skill_grade: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    def __str__(self):
        return f"{self.full_name}, {self.email}, {'|'.join(self.tech_stack)}, {self.main_skill}, {self.main_skill_grade}"

    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    @classmethod
    def generate_candidates(cls, url: str):
        list_of_candidates = []
        response = requests.get(url)
        flag = True  #
        with open('test_file.csv', 'w') as file:
            file.write(response.text)
        with open("test_file.csv", 'r') as infile:
            reader = csv.reader(infile, delimiter=",")
            for row in reader:
                if flag:
                    flag = False
                    continue
                full_name = list(row[0].split())
                cur_tech_stack = list(row[2].split('|'))
                candidate = cls(full_name[0], full_name[1], row[1], cur_tech_stack, row[3], row[4])
                list_of_candidates.append(candidate)
            return list_of_candidates

    @staticmethod
    def candidates_to_console(my_list):
        for i in my_list:
            print(i)


candidates = Candidate.generate_candidates('https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv')
Candidate.candidates_to_console(candidates)


