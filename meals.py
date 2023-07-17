from itertools import count


breakfast = ['Egg Sandwich', 'Bagel', 'Coffee']

lunch = ['BLT', 'PB&J', 'Turkey Sandwich']

dinner = ['Soup', 'Salad', 'Spaghetti', 'Taco']

#menus = [['Egg Sandwich', 'Bagel', 'Coffee'],
#        ['BLT', 'PB&J', 'Turkey Sandwich'],
#        ['Soup', 'Salad', 'Spaghetti', 'Taco']]

menus = { 'Breakfast' : ['Egg Sandwich','Bagel','Coffee'],
          'Lunch' : ['BLT','PB&J','Turkey Sandwich'],
          'Dinner' : ['Soup','Salad','Spaghetti','Taco']}

#print('Breakfast Menu:\t', menus[0])
#print('Lunch Menu:\t', menus[1])
#print('Dinner Menu:\t', menus[2])
#print(menus[0][1 ])
#                     \/Method\/
for name, menu in menus.items():
    print(name, ':', menu)
