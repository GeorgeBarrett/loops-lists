from sys import exit

def gold_room():
    print('This room is full of gold. How much should I take?')

    choice = input('> ')

    if '0' in choice or '1' in choice:
        how_much = int(choice)
    else: 
        dead('Please learn how to type a number.')

    if how_much < 50:
        print('Nice, you\'re not too greedy.')
        exit(0)    
    else: 
        dead('Your greed has been your demise.')


def bear_room():
    print('There is a bear here.')
    print('There bear has a bunch of honey.')
    print('The fat bear is in front of another door.')
    print('How are you going to move the bear?')
    bear_moved = False

    while True:
        choice = input('> ')

        if choice == 'Take honey':
            dead('The bear eats you for brunch with eggs and kale.')
        elif choice == 'Taunt bear' and not bear_moved:
            print('The bear has moved from the door.')
            print('You can go through it now.')
            bear_moved = True
        elif choice == 'Taunt bear' and bear_moved:
            dead('The taunt failed and now you are on a silver platter')
        elif choice == 'Open door' and bear_moved:
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
    elif 'nail' in choice:
        dead('Cthulhu hates the smell and kills you without question.')
    else: 
        cthulhu_room()

def dead(why):
    print(why, 'Nice work!')


def start():
    print('You are in a dark room.')
    print('There is a door to your right and your left.')
    print('Which one do you take?')

    choice = input('> ')

    if choice == 'left':
        bear_room()
    elif choice == 'right':
        cthulhu_room()
    else: 
        dead('You touch a wall and transpot to the ninth dimension')


start()






