import unittest
from L19.test_L17.classes.employee_recruiter_developer import Employee


class TestEmployee(unittest.TestCase):
    def test_str(self):
        emp = Employee('Valeriya Belyayeva', 20, '848belval848@gmail.com')
        self.assertEqual("Employee: Valeriya Belyayeva, Salary: 0", f"Employee: {emp.name}, Salary: {emp.check_salary()}")

    def test_compare(self):
        emp1 = Employee('Valeriya Belyayeva', 20, '848belval848@gmail.com')
        emp2 = Employee('Brittney Skil', 20, 'brittney36@ccategoryk.com')
        emp3 = Employee('Brittney Well', 30, 'brittney36@ccategoryk.com')
        self.assertTrue(emp1 == emp2)
        self.assertFalse(emp1 > emp2)
        self.assertTrue(emp3 > emp2)

    def test_work(self):
        emp1 = Employee('Valeriya Belyayeva', 20, '848belval848@gmail.com')
        self.assertEqual('I come to the office.', emp1.work())


