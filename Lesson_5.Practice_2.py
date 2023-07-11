def kvadrat(number):
    return number ** 2

print(kvadrat(32))
print(kvadrat(8))
print(kvadrat(12))

def simple_number(number) :
    for i in range(2, number // 2) :
        if not number % i:
            return False
    return True

print(simple_number(5))

prostie_chisla = (list(filter(simple_number,range(50))))
print(prostie_chisla)
kvadratu_prostix_chisel = list(map(kvadrat, prostie_chisla))
print(kvadratu_prostix_chisel)