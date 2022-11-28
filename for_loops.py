# storing lists in variables
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'bananas', 'figs', 'dates']
change = [1, 'pennies', 2, 'pounds', 3, 'squillions']

# number is the index name that represents the items in the_count list
for number in the_count:
    print(f'This is count {number}.')

# fruit is the index name that represents the items in fruit list
for fruit in fruits:
    print(f'A type of fruit: {fruit}.')

# i is the index name that represents the items in change list
for i in change:
    print(f'I got {i}.')

# the for loop will loop through the list and I can print the index using an f string

# this is creating an empty list and storing it in a variable
elements = []

# i is the index name. range is creating a list that has the numbers 0 - 6
for i in range(0, 6):
    # this range will actually list the numbers 0-5 (that's just the way it works)
    print(f'adding {i} to the list.')
    # i is the index name and the index is the numbers 0-6.
    # the for loop, loops through the index
    # append adds range(0-6) to the empty list stored within the elements variable  
    elements.append(i)

# the variable elements now has an index name and has been populated ^^
for i in elements:
    print(f'Element was: {i}')
