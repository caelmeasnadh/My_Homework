with open("C:/Users/datex/Documents/FizzBuzz.txt", 'r+') as f, open("C:/Users/datex/Documents/FizzBuzzResult.txt", 'r+') as f1 :
    for line in f:
        l = line.split()
        fizz_number,buzz_number,count_number = map(int, l)
        i = 1
        while i < count_number + 1 :
            if (not i % fizz_number and not i % buzz_number):
                f1.write('FB \n')
            elif not i % fizz_number :
                f1.write('F \n')
            elif not i % buzz_number :
                f1.write('B \n')
            else :
                f1.write(str(i) + '\n' )
            i += 1
        f1.write('\n')
f.close()
f1.close()
