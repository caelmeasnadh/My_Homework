from unittest import TestCase
from OOP_Lesson_4_Employee import Employee

class TestEmployee(TestCase):

    def test_lt(self):
        employee_1 = Employee('George', 1500, 'blablabla@gmail.com')
        employee_2 = Employee('Lucas', 1750, 'blablabla2@gmail.com')
        self.assertTrue(employee_1 > employee_2)

    def test_gt(self):
        employee_1 = Employee('George', 2000, 'blablabla@gmail.com')
        employee_2 = Employee('Lucas', 1750, 'blablabla2@gmail.com')
        self.assertTrue(employee_1 < employee_2)

    def test_eq(self):
        employee_1 = Employee('George', 1000, 'blablabla@gmail.com')
        employee_2 = Employee('Lucas', 1000, 'blablabla2@gmail.com')
        self.assertTrue(employee_1 == employee_2)

    def test_work_str(self):
        employee_1 = Employee('George', 1500, 'blablabla@gmail.com')
        self.assertTrue(employee_1.work(),'I come to the office')


