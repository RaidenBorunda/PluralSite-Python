#Dictionary of strings to strings
acronyms = {'LOL':'laugh of loud',
            'IDK': "I don't know",
            'TBH': 'to be honest'}
#Dictionary of strings to numbers
menu = {'Soup':5, 'Salada':6, 'Bread':7}
#Dictionary of anything
my_dict = {10:'hello', 2:6.5}

#Create an empty dictionary
empty_dict = {}
#Add new dictionary items
empty_dict['H20'] = 'Water'
empty_dict['C02'] = 'Carbon Dioxide'
empty_dict['C0'] = 'Carbon Monoxide'
#Update a value
acronyms['TBH'] = 'honestly'
#Delete a value
del empty_dict['C02']
#If you want to get a word in the dictionary, use get()
definition = acronyms.get('BTW')

if definition:
    print(definition)
else:
    print("Key doesn't exist")

print(acronyms['TBH'])
print(menu['Soup'])
print(my_dict[10])
print(empty_dict['C0'])
print(empty_dict)
print(definition)

acronyms['TBH'] = 'to be honest'
sentence = 'IDK' + ' what happened ' + 'TBH'
translation = acronyms.get('IDK') + ' what happened ' + acronyms.get('TBH')
print('sentence:', sentence)
print('translation:', translation)