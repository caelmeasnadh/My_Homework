from unittest import TestCase
from OOP_Lesson_5 import Candidate

class TestCandidate(TestCase):

    def test_full_name(self):
        candidate_1 = Candidate('John', 'Wick', 'myemail@gmail.com', ['Python'], 'Python', 'Senior')
        self.assertEqual(candidate_1.full_name, 'John Wick')

    def test_candidates(self):
        candidates_info = Candidate.generate_candidates(
            'https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv')

        self.assertEqual(candidates_info[0].full_name, 'Ivan Chechov')
        self.assertEqual(candidates_info[0].email, 'ichech@example.com')
        self.assertEqual(candidates_info[0].tech_stack, ['Python|Django|Angular'])
        self.assertEqual(candidates_info[0].main_skill, 'Python')
        self.assertEqual(candidates_info[0].main_skill_grade, ' Senior')

        self.assertEqual(candidates_info[1].full_name, 'Max Payne')
        self.assertEqual(candidates_info[1].email, 'mpayne@example.com')
        self.assertEqual(candidates_info[1].tech_stack, ['PHP|Laravel|MySQL'])
        self.assertEqual(candidates_info[1].main_skill, 'PHP')
        self.assertEqual(candidates_info[1].main_skill_grade, 'Middle')

        self.assertEqual(candidates_info[2].full_name, 'Tom Hanks')
        self.assertEqual(candidates_info[2].email, 'thanks@example.com')
        self.assertEqual(candidates_info[2].tech_stack, ['Python|CSS'])
        self.assertEqual(candidates_info[2].main_skill, 'Python')
        self.assertEqual(candidates_info[2].main_skill_grade, 'Junior')

