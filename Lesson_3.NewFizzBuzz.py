f = open("C:/Users/datex/Documents/FizzBuzz.txt", 'r')
for line in f:
    l = line.split()
    fizz_number,buzz_number,count_number = map(int, l)
    print(fizz_number,buzz_number,count_number)
    [print((not i % fizz_number) * "F" + (not i % buzz_number) * "B" or i) for i in range(1, count_number + 1)]
f.close()
