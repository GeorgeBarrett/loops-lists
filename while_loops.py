# two variables. one stores a number, the other an empty list
i = 0
numbers = []

# a while loop will keep looping until something returns false
# the loop will continue looping until the index number reaches 5
# the returns from the loop will be incremental
# 
while i < 6:
    # this loops will create an index of 0-5
    print(f'At the top i is {i}.')
    # this populates the empty list called numbers
    numbers.append(i)

    # short hand for i = i + 1
    # this is redifining the variable i from 5 to 6
    i += 1

    # this prints the numbers variable that stores number 0-5
    print(f'Numbers now: ', numbers)
    # this f string prints the redifined i variable
    print(f'At the bottom i is {i}.')

print('The numbers: ')

# num is the name of the index
# numbers is the variable that now has been populated by numbers 0-5
# the while loop populated that numbers variable
# this for loop is looping through the numbers variable, which contains a list of the numbers 0-5
for num in numbers:
    # printing the index
    print(num)
