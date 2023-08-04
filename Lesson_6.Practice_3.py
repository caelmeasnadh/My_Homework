my_dict3 = {
    'XXS':
        {
            'Germany' : 36,
            'USA' : 8,
            'France' : 38,
            'Great Britain' : 24
        },
    'XS' :
        {
            'Germany' : 38,
            'USA' : 10,
            'France' : 40,
            'Great Britain' : 26
        },
    'S' :
        {
            'Germany' : 40,
            'USA' : 12,
            'France' : 42,
            'Great Britain' : 28
        },
    'M':
        {
            'Germany': 42,
            'USA': 14,
            'France': 44,
            'Great Britain': 30
        },
    'L':
        {
            'Germany': 44,
            'USA': 16,
            'France': 46,
            'Great Britain': 32
        },
    'XL':
        {
            'Germany': 46,
            'USA': 18,
            'France': 48,
            'Great Britain': 34
        },
    'XXL':
        {
            'Germany': 48,
            'USA': 20,
            'France': 50,
            'Great Britain': 36
        },
    'XXXL':
        {
            'Germany': 50,
            'USA': 22,
            'France': 52,
            'Great Britain': 38
        }
}

def find_size(regular_size):
    for key, values in my_dict3.items():
        if regular_size == key:
            result = str(values).replace('{','').replace('}','').replace('\'','')
            return result

print(find_size(input('Enter your size :')))