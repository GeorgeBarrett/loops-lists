the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'bananas', 'figs', 'dates']
change = [1, 'pennies', 2, 'pounds', 3, 'squillions']

for number in the_count:
    print(f'This is count {number}.')

for fruit in fruits:
    print(f'A fruit of type: {fruit}.')

for i in change:
    print(f'I got {i}.')

elements = []

for i in range(0, 6):
    print(f'adding {i} to the list.')
    elements.append(i)

for i in elements:
    print(f'Element was: {i}')
