from unittest import TestCase
from OOP_Lesson_4_Employee import Employee

class TestEmployee(TestCase):

    def setUp(self):
        self.employee = Employee('George', 1500, 'blablabla@gmail.com')
        self.employee_2 = Employee('Lucas', 1750, 'blablabla2@gmail.com')

    def test_lt(self):
        self.assertTrue(self.employee > self.employee_2)

    def test_gt(self):
        self.assertTrue(self.employee < self.employee_2)

    def test_eq(self):
        self.assertTrue(self.employee == self.employee_2)

    def test_work_str(self):
        self.assertTrue(self.employee.work(),'I come to the office')


