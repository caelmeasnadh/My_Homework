class Employee:
    def __init__(self, name, salary_for_one_day):
        self.name = name
        self.salary_for_one_day = salary_for_one_day

    def work(self):
        return 'I come to the office'

# Тут був дублікат методу __str__, видалив його, залишивши тільки перероблений варіант
    def __str__(self):
        return f'{(type(self).__name__)} : {(self.name)}'

    def __lt__(self, other):
        return self.salary_for_one_day > other.salary_for_one_day

    def __gt__(self, other):
        return self.salary_for_one_day < other.salary_for_one_day

    def __eq__(self, other):
        return self.salary_for_one_day == other.salary_for_one_day


class Recruter(Employee):

    def work(self):
        return 'I come to the office and start hiring'


class Developer(Employee):
    def work(self):
        return 'I come to the office and start coding'

    def add_tech_stack(self, technology):
        self.tech_stack.extend(technology)

    def get_tech_stack(self):
        return self.tech_stack


employee_1 = Employee("George", 1500)
employee_2 = Employee("Lucas", 1750)
recruter_1 = Recruter("Denis", 2000)
recruter_2 = Recruter("Will", 2250)
developer_1 = Developer("Arnold", 2500)
developer_2 = Developer("Harry", 2500)
print(employee_1.work())
print(recruter_1.work())
print(developer_1.work())
# Викликав методи невірним способом - print(employee_1.__str__()).
print(employee_1)
print(employee_2)
print(recruter_1)
print(recruter_2)
print(developer_1)
print(developer_2)

print(employee_1 > employee_2)
print(employee_1 < employee_2)
print(employee_1 == employee_2)
