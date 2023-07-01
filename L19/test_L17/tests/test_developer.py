import unittest
from L19.test_L17.classes.employee_recruiter_developer import Developer


class TestDeveloper(unittest.TestCase):
    def test_str(self):
        dev = Developer('Valeriya Belyayeva', 20, '848belval848@gmail.com', ['Python', 'Excel', 'PSQL'])
        self.assertEqual("Developer: Valeriya Belyayeva, Salary: 0, Knowledge: ['Python', 'Excel', 'PSQL'].", f"Developer: {dev.name}, Salary: {dev.check_salary()}, Knowledge: {dev.tech_stack}.")

    def test_compare(self):
        dev1 = Developer('Valeriya Belyayeva', 20, '848belval848@gmail.com', ['Python', 'PSQL'])
        dev2 = Developer('Brittney Skil', 20, 'brittney36@ccategoryk.com', ['Python', 'C#'])
        dev3 = Developer('Brittney Well', 30, 'brittney36@ccategoryk.com', ['Python', 'Excel', 'PSQL'])
        self.assertTrue(dev1 == dev2)
        self.assertFalse(dev1 > dev2)
        self.assertTrue(dev3 > dev2)

    def test_work(self):
        dev1 = Developer('Valeriya Belyayeva', 20, '848belval848@gmail.com', ['Python', 'Excel', 'PSQL'])
        self.assertEqual('I come to the office and start to coding.', dev1.work())


