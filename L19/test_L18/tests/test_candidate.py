import unittest
from L19.test_L18.classes.candidate import Candidate


class TestCandidate(unittest.TestCase):
    def test_full_name(self):
        candidate = Candidate('Valeriya', 'Belyayeva', '848belval848@gmail.com', ['Python', 'QA'], 'QA', 'Junior')
        self.assertEqual('Valeriya Belyayeva', candidate.full_name)

    def test_str(self):
        candidate = Candidate('Valeriya', 'Belyayeva', '848belval848@gmail.com', ['Python', 'QA'], 'QA', 'Junior')
        expected_result = 'Valeriya Belyayeva, 848belval848@gmail.com, Python|QA, QA, Junior'
        self.assertEqual(expected_result, str(candidate))

    def test_generate_candidates(self):
        candidates = Candidate.generate_candidates(
            'https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv')
        self.assertEqual('Ivan Chechov', candidates[0].full_name)
        self.assertEqual('mpayne@example.com', candidates[1].email)
        self.assertEqual('Junior', candidates[2].main_skill_grade)
        self.assertEqual('PHP', candidates[1].main_skill)
        self.assertListEqual(['Python', 'CSS'], candidates[2].tech_stack)
