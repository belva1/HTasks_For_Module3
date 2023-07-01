import unittest
from L19.test_L17.classes.employee_recruiter_developer import Recruiter


class TestRecruiter(unittest.TestCase):
    def test_str(self):
        rec = Recruiter('Valeriya Belyayeva', 20, '848belval848@gmail.com')
        self.assertEqual("Recruiter: Valeriya Belyayeva, Salary: 0", f"Recruiter: {rec.name}, Salary: {rec.check_salary()}")

    def test_compare(self):
        rec1 = Recruiter('Valeriya Belyayeva', 20, '848belval848@gmail.com')
        rec2 = Recruiter('Brittney Skil', 20, 'brittney36@ccategoryk.com')
        rec3 = Recruiter('Brittney Well', 30, 'brittney36@ccategoryk.com')
        self.assertTrue(rec1 == rec2)
        self.assertFalse(rec1 > rec2)
        self.assertTrue(rec3 > rec2)

    def test_work(self):
        rec1 = Recruiter('Valeriya Belyayeva', 20, '848belval848@gmail.com')
        self.assertEqual('I come to the office and start to hiring.', rec1.work())