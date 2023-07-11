str = 'DmItRiY KiShInSkIy'
def my_str(str):
    return str.lower()
def my_str2(str):
    return str.upper()
def my_str3(str, my_str, my_str2):
    result1 = list(map(my_str, str))
    result2 = list(map(my_str2, str))
    print("".join(result1), "".join(result2))

print(my_str(str))
print(my_str2(str))
my_str3(str, my_str, my_str2)
