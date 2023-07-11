# Ввести число, вивести усі його дільники.

number = int(input("Enter your number : "))
i = [n for n in range(1, number+1) if not number % n]
print(i)

# Ввести число, вивести його розряди та їх множники.

def rozryad(number: int) -> str:
    result = []
    a = str(number)
    for id, item in enumerate(a):
        result.append(f'{item}*10**{len(a) - id - 1}')
    return result
print(rozryad(12391))

# Задача fizz-buzz:

fizz_number = int(input("Enter your fizz number : "))
buzz_number = int(input("Enter your buzz number : "))
count_number = int(input("Enter your count number : "))
[print((not i % fizz_number)*"F" + (not i % buzz_number)*"B" or i) for i in range(1, count_number + 1)]
