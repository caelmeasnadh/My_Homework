f = open("C:/Users/datex/Documents/Sort.txt", 'r')
word_count = {}
for line in f:
    words = line.split()
    for word in words :
        word = word.lower()
        if word not in word_count :
            word_count[word] = 0
        word_count[word] += 1
word_count_sorted = sorted(word_count.items(), key=lambda item:item[1])
print(word_count_sorted)
