with open("C:/Users/datex/Documents/FizzBuzz.txt", 'r+') as f, open("C:/Users/datex/Documents/FizzBuzzResult.txt", 'r+') as f1 :
    for line in f:
        l = line.split()
        fizz_number,buzz_number,count_number = map(int, l)
        result = [((not i % fizz_number) * "F" + (not i % buzz_number) * "B" or i) for i in range(1, count_number + 1)]
        f1.write(' '.join(str(item) for item in result))
f.close()
f1.close()