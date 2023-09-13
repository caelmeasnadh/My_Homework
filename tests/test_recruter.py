from unittest import TestCase
from OOP_Lesson_4_Employee import Recruter

class TestRecruter(TestCase):

    def setUp(self):
        self.recruter = Recruter('Inna', 2000, 'blabla@gmail.com')
        self.recruter_2 = Recruter('Dima', 2500, 'blabla@gmail.com')

    def test_work_str(self):
        self.assertTrue(self.recruter.work(),'I come to the office and start hiring')

    def test_lt(self):
        self.assertTrue(self.recruter > self.recruter_2)

    def test_gt(self):
        self.assertTrue(self.recruter < self.recruter_2)

    def test_eq(self):
        self.assertTrue(self.recruter == self.recruter_2)