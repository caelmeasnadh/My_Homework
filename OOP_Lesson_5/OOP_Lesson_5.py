import csv
import datetime
from exceptions import EmailAlreadyExistsException
import traceback
import requests


class Employee:
    def __init__(self, name, salary_for_one_day, email):
        self.name = name
        self.salary_for_one_day = salary_for_one_day
        self.email = email
        self.set_email(email)

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

    def save_email(self):
        with open("emails.csv", 'a', newline='') as file:
            write = csv.writer(file)
            write.writerow([self.email])

    def validate_email(self, email):
        with open("emails.csv", 'r', newline='') as file1:
            read = csv.reader(file1)
            for row in read:
                if email in row:
                    raise EmailAlreadyExistsException("Email already exists")
        print("Validation successful")

    def invalid_email(self):
        with open("logs.txt", 'a', newline='') as file2:
            time = datetime.datetime.now().strftime("%D - %H:%M:%S")
            trace = traceback.format_exc()
            file2.write(f'{time} :\n {trace} \n')

    def set_email(self, email):
        try:
            self.validate_email(email)
            self.save_email()
        except EmailAlreadyExistsException:
            self.invalid_email()


class Recruter(Employee):
    def work(self):
        return 'I come to the office and start hiring'


class Developer(Employee):
    def __init__(self, *args, tech_stack, **kwargs):
        super().__init__(*args, **kwargs)
        self.tech_stack = tech_stack

    def __add__(self, other):
        new_name = self.name + ' ' + other.name
        new_max_salary = max(self.salary_for_one_day, other.salary_for_one_day)
        new_tech_stack = set(self.tech_stack + other.tech_stack)
        return Developer(new_name, new_max_salary, tech_stack = new_tech_stack, email = None)

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
        today = datetime.date.today()
        month_start = today.replace(day=1)
        start_of_month = month_start
        days_number = 0

        while start_of_month <= today:
            if start_of_month.weekday() < 5:
                days_number += 1
            start_of_month += datetime.timedelta(days=1)
        return self.salary_for_one_day * days_number


class Candidate():
    def __init__(self, first_name, last_name, email, tech_stack, main_skill, main_skill_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def generate_candidates(cls, url):
        x = requests.get(url)
        candidates = []
        row = x.text.split('\n')
        for line in row[1:]:
            info = line.strip().split(',')
            if len(info) == 5:
                full_name, email, tech_stack, main_skill, main_skill_grade = info
                first_name, last_name = full_name.split()
                tech_stack = tech_stack.split(';')
                candidate = cls(first_name, last_name, email, tech_stack, main_skill, main_skill_grade)
                candidates.append(candidate)
        return candidates

candidates_info = Candidate.generate_candidates('https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv')

for candidate in candidates_info:
    print(f"Full Name: {candidate.full_name}")
    print(f"Email: {candidate.email}")
    print(f"Tech Stack: {candidate.tech_stack}")
    print(f"Main Skill: {candidate.main_skill}")
    print(f"Main Skill Grade: {candidate.main_skill_grade}")
    print()


employee_1 = Employee("George", 1500, "blablabla@gmail.com")
employee_2 = Employee("Lucas", 1750, "blablabla2@gmail.com")
recruter_1 = Recruter("Denis", 2000, "blablabla3@gmail.com")
recruter_2 = Recruter("Will", 2250, "blablabla4@gmail.com")
developer_1 = Developer("Arnold", 2500, tech_stack = ['Java'], email = "blablabla5@gmail.com")
developer_2 = Developer("Harry", 3000, tech_stack = ['FrontEnd', 'Python', 'Java'], email = "blablabla6@gmail.com")
candidate_1 = Candidate('Arnold', 'Schwarzenegger', 'terminator@gmail.com', ['Java'], 'Python', 'Junior')

print(candidate_1.full_name)
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
