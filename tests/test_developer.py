from unittest import TestCase
from OOP_Lesson_4_Employee import Developer

class TestDeveloper(TestCase):

    def setUp(self):
        self.developer = Developer('Inna', 2000, tech_stack = ['Python', 'Java'], email = 'blabla@gmail.com')
        self.developer_2 = Developer('Bogdan', 2000, tech_stack=['FrontEnd'], email='blablabla@gmail.com')

    def test_work_str(self):
        self.assertTrue(self.developer.work(),'I come to the office and start coding')

    def test_add_developers(self):
        new_developer = self.developer + self.developer_2
        expected_name = 'Inna Bogdan'
        expected_tech_stack = set(['Python', 'Java', 'FrontEnd'])
        expected_salary = max(self.developer.salary_for_one_day, self.developer_2.salary_for_one_day)

        self.assertEqual(expected_name, new_developer.name)
        self.assertEqual(expected_tech_stack, new_developer.tech_stack)
        self.assertEqual(expected_salary, new_developer.salary_for_one_day)

    def test_salary_result(self):
        expected_salary = 10000
        self.assertEqual(expected_salary, self.developer.check_salary(5))

    def test_lt(self):
        self.assertTrue(self.developer < self.developer_2)

    def test_eq(self):
        self.assertTrue(self.developer == self.developer_2)