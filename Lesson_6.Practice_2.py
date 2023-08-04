my_dict2 = {
    'Potter' : ['Python', 'Java'],
    'Weasley': ['FrontEnd'],
    'Lovegood': ['FullStack'],
    'Longbottom': ['FrontEnd', 'Java'],
    'Granger': ['FullStack'],
    'Hagrid': ['Java']
}

print(' & '.join([key for key, value in my_dict2.items() if len(value) >=2]))
print(' & '.join([key for key, value in my_dict2.items() if 'FrontEnd' not in value]))
print(' & '.join([key for key, value in my_dict2.items() if 'Python' in value or 'Java' in value]))