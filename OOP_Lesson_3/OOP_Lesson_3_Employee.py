import datetime


class Employee:
    def __init__(self, name, salary_for_one_day):
        self.name = name
        self.salary_for_one_day = salary_for_one_day

    def __str__(self):
        return (type(self).__name__)

    def __str__(self):
        return f'{(type(self).__name__)} : {(self.name)}'

    def __lt__(self, other):
        return self.salary_for_one_day > other.salary_for_one_day

    def __gt__(self, other):
        return self.salary_for_one_day < other.salary_for_one_day

    def __eq__(self, other):
        return self.salary_for_one_day == other.salary_for_one_day

    def work(self):
        return 'I come to the office'


class Recruter(Employee):
    def work(self):
        return 'I come to the office and start hiring'


class Developer(Employee):
    def __init__(self, name, salary_for_one_day, tech_stack):
        super().__init__(name, salary_for_one_day)
        self.tech_stack = tech_stack

    def __add__(self, other):
        new_name = self.name + ' ' + other.name
        new_max_salary = max(self.salary_for_one_day, other.salary_for_one_day)
        new_tech_stack = set(self.tech_stack + other.tech_stack)
        return Developer(new_name, new_max_salary, new_tech_stack)

    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def __lt__(self, other):
        return len(self.tech_stack) < len(other.tech_stack)

    def work(self):
        return 'I come to the office and start coding'

    def get_tech_stack(self):
        return self.tech_stack

    def check_salary(self, days):
        return self.salary_for_one_day * days

    def check_salary_until_today(self):
        days_number = 0
        for d in (datetime.date(2023, 8, i) for i in range(1, datetime.datetime.now().day)):
            if d.weekday() < 5:
                days_number += 1
        return self.salary_for_one_day * days_number


employee_1 = Employee("George", 1500)
employee_2 = Employee("Lucas", 1750)
recruter_1 = Recruter("Denis", 2000)
recruter_2 = Recruter("Will", 2250)
developer_1 = Developer("Arnold", 2500, ['Java'])
developer_2 = Developer("Harry", 3000, ['FrontEnd', 'Python', 'Java'])

print(employee_1.work())
print(recruter_1.work())
print(developer_1.work())

print(employee_1)
print(employee_2)
print(recruter_1)
print(recruter_2)
print(developer_1)
print(developer_2)

print(employee_1 > employee_2)
print(employee_1 < employee_2)
print(employee_1 == employee_2)

print(developer_1.check_salary(4))

print(developer_1 == developer_2)
print(developer_1 < developer_2)
print(developer_2 < developer_1)

new_developer = developer_1 + developer_2
print(f'Name : {new_developer.name}, Salary : {new_developer.salary_for_one_day}, Tech Stack : {new_developer.tech_stack}')
print(developer_1.check_salary_until_today())
print(developer_2.check_salary_until_today())

