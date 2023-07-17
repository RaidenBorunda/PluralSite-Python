import random

computer_choice = random.choice(['rock', 'paper', 'scissors'])
#computer_choice = str('scissors')
user_choice = input('Do you want - rock, paper, or scissors?\n')

if computer_choice == user_choice:
    print('Tie!')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('Win!')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('Win!')
else:
    print('You lose :( Computer wins!')