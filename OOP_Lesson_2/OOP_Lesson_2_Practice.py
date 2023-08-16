current_year = 2023
class Human:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def __str__(self):
        print(f'Name : {self.name}, Birth date : {self.date_of_birth}')

    def get_age(self):
        return current_year - self.date_of_birth


class Planet:
    def __init__(self, name):
        self.name = name
        self.population = []

    def __str__(self):
        print(f'This planet is : {self.name}')

    def add_human(self, population):
        self.population.extend(population)

    def get_count(self):
        return len(self.population)

    def __lt__(self, other):
        return len(self.population) < len(other.population)

    def __gt__(self, other):
        return len(self.population) > len(other.population)

    def __eq__(self, other):
        return len(self.population) == len(other.population)


person_1 = Human('Mark', 1998)
person_2 = Human('George', 1998)
print(person_1.get_age())
planet_1 = Planet('Earth')
planet_2 = Planet('Mercury')
planet_1.add_human([person_1, person_2])
planet_2.add_human([person_1])
print(planet_1.get_count())
print(planet_2.get_count())
print(planet_1 < planet_2)
print(planet_1 > planet_2)
print(planet_1 == planet_2)