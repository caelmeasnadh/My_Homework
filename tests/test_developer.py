from unittest import TestCase
from OOP_Lesson_4_Employee import Developer

class TestDeveloper(TestCase):

    def test_work_str(self):
        developer_1 = Developer('Inna', 2000, tech_stack = ['Python', 'Java'], email = 'blabla@gmail.com')
        self.assertTrue(developer_1.work(),'I come to the office and start coding')

    def test_add_developers(self):
        developer_1 = Developer('Inna', 2000, tech_stack=['Python', 'Java'], email='blabla@gmail.com')
        developer_2 = Developer('Bogdan', 2000, tech_stack=['FrontEnd'], email='blablabla@gmail.com')

        new_developer = developer_1 + developer_2
        expected_name = 'Inna Bogdan'
        expected_tech_stack = set(['Python', 'Java', 'FrontEnd'])
        expected_salary = max(developer_1.salary_for_one_day, developer_2.salary_for_one_day)

        self.assertEqual(expected_name, new_developer.name)
        self.assertEqual(expected_tech_stack, new_developer.tech_stack)
        self.assertEqual(expected_salary, new_developer.salary_for_one_day)

    def test_salary_result(self):
        developer_1 = Developer('Inna', 200, tech_stack=['Python', 'Java'], email='blabla@gmail.com')
        expected_salary = 1000

        self.assertEqual(expected_salary, developer_1.check_salary(5))

    def test_lt(self):
        developer_1 = Developer('Inna', 2000, tech_stack=['Python', 'Java'], email='blabla@gmail.com')
        developer_2 = Developer('Bogdan', 2000, tech_stack=['Python', 'Java', 'FrontEnd'], email='blablabla@gmail.com')
        self.assertTrue(developer_1 < developer_2)

    def test_eq(self):
        developer_1 = Developer('Inna', 2000, tech_stack=['Python', 'Java'], email='blabla@gmail.com')
        developer_2 = Developer('Bogdan', 2000, tech_stack=['FrontEnd', 'Java'], email='blablabla@gmail.com')
        self.assertTrue(developer_1 == developer_2)