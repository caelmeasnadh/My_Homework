def spam(number):
    return "bulochka" * number


def my_sum(list_of_numbers):
    result = 0
    for number in list_of_numbers:
        result += number
    return result


def shortener(string):
    result = []
    for word in string.split():
        if len(word) > 6:
            result.append(word[:6] + '*')
        if len(word) < 6:
            result.append(word)
    return ' '.join(result)


def compare_ends(words):
    result = 0
    for word in words:
        if len(word) > 2 and word[0] == word[-1]:
            result += 1
    return result


