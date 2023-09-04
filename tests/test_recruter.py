from unittest import TestCase
from OOP_Lesson_4_Employee import Recruter

class TestRecruter(TestCase):

    def test_work_str(self):
        recruter_1 = Recruter('Inna', 2000, 'blabla@gmail.com')
        self.assertTrue(recruter_1.work(),'I come to the office and start hiring')

    def test_lt(self):
        recruter_1 = Recruter('Inna', 2000, 'blabla@gmail.com')
        recruter_2 = Recruter('Dima', 2500, 'blabla@gmail.com')
        self.assertTrue(recruter_1 > recruter_2)

    def test_gt(self):
        recruter_1 = Recruter('Inna', 2000, 'blabla@gmail.com')
        recruter_2 = Recruter('Dima', 1500, 'blabla@gmail.com')
        self.assertTrue(recruter_1 < recruter_2)

    def test_eq(self):
        recruter_1 = Recruter('Inna', 2000, 'blabla@gmail.com')
        recruter_2 = Recruter('Dima', 2000, 'blabla@gmail.com')
        self.assertTrue(recruter_1 == recruter_2)