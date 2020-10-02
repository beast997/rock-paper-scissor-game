import random

user = None

computer = random.choice(['rock','paper','scissor'])
notification = print('please enter the value you wish to choose or press q to quit the game:')
while user == None:
    user = input('please enter the value you wish to choose or press q to quit the game:')
    if user not in ['rock','paper','scissor']:
        print('You need to choose valid value')
        user = None
i = 1
for(i<=3):           //Iterate The Loop Three Times
    user = input('please enter the value you wish to choose:')
    if user == computer:
        print('Draw')
    if user == 'rock':
        if computer == 'paper':
            print('computer wins')
        elif computer == 'scissor':
            print('user wins')
    if user == 'paper':
        if computer == 'scissor':
            print('computer wins')
        elif computer == 'rock':
            print('user wins')
    if user == 'scissor':
        if computer == 'rock':
            print('computer wins')
        elif computer == 'paper':
            print('user wins')
    elif user=='q':
        exit()

print('computer is {}'.format(computer))
print('user is {}'.format(user))
