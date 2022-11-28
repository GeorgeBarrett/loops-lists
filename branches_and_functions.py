# importing exit module from sys
from sys import exit

# defining a function called gold_room
def gold_room():
    print('This room is full of gold bars. How many do you take?')

    # this a variable inside the function that stores a user input (with prompt >)
    choice = input('> ')

    # these conditions respond to the user's input
    # if the user enters 0 or 1 then this value will be stored how_much
    # the int(choice) will round the users number input down 
    # I include the 1 in this statement so that the variable how_much stores the numbers 1-50
    if '0' in choice or '1' in choice:
        # the int(choice) round the user's input number down
        how_much = int(choice)
    else: 
        dead('Please learn how to type a number.')

    # if user inputs 1-50 then the lines bellow will fire
    if how_much < 50:
        print('Nice, you\'re not too greedy.')
        # this exits the programme (the number 0 means no errors. Different numbers mean different errors)
        exit(0)    
    else: 
        dead('Your greed has been your demise.')


# defining a function called bear_room
def bear_room():
    print('There is a bear here.')
    print('There bear has a bunch of honey.')
    print('The fat bear is in front of another door.')
    print('How are you going to move the bear?')
    # bear_moved is a variable that has been set to false.
    # I can set this to true to affect the game
    bear_moved = False

    # this makes an infite loop
    while True:
        # this variable stores a user input with a prompt 
        choice = input('> ')

        # if the user inputs take honey then the line below will fire
        if choice == 'take honey':
            dead('The bear eats you for brunch with eggs and kale.')
        # if user inputs 'taunt bear' and the bear_moved remains false the lines below will fire
        elif choice == 'taunt bear' and not bear_moved:
            print('The bear has moved from the door.')
            print('You can go through it now.')
            # this line will fire, which opens the way to the door
            bear_moved = True
        # If the user inputs 'taunt bear' again, the line below will fire. This is because the elif above redfined bear_moved to true
        elif choice == 'taunt bear' and bear_moved:
            dead('The taunt failed and now you are on a silver platter')
        # when the user inputs open door then the function below will fire. the doorway is free due to bear_moved being set to true in previous elif
        elif choice == 'open door' and bear_moved:
            gold_room()
        else:
            print('I got no idea what that means')


def cthulhu_room():
    print('Here you see the great evil Cthulhu.')
    print('The stare makes you go insane.')
    print('Do you flee for you life or start applying nail polish?')

    choice = input('> ')

    if 'flee' in choice:
        start()
    elif 'applying' in choice:
        dead('Cthulhu hates the smell and kills you without question.')
    else: 
        cthulhu_room()

# this function gives functionality to all the 'dead' statements above and fires the line of code below 
# the function needs an argument and I am not sure why
def dead(why):
    print(why,'Nice work!')


# this function defines the begininning of the game
def start():
    print('You are in a dark room.')
    print('There is a door to your right and your left.')
    print('Which one do you take?')

    # this variable stores a user input with a prompt
    choice = input('> ')

    # if the user inputs left, then the bear_room function will fire
    if choice == 'left':
        bear_room()
    # if the user inputs right, then the cthulhu_room function will fire
    elif choice == 'right':
        cthulhu_room()
    # this prevents an infinte loop and returns a string if the user chooses to input something other than left or right
    else: 
        dead('You touch a wall and transport to the ninth dimension')


# this ensures the 'start' function fires first
start()








