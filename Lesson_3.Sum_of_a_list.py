summa = 0
[summa := summa + x for x in list(range(11+1))]
print(summa)

b = list(range(11+1))
summa = 0
i = 0
while i < len(b):
    summa += b[i]
    i += 1
print(summa)

