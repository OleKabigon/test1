#This app finds the largest number in a list

numbers = [4, 3, 10, 20, 14, 13, 8]

# Need variable to evaluate and start at first position of list
max = numbers[0]





for number in numbers:  # setting number variable to first in list
    if number > max:  # Is 4>3,no,max stays same

        max = number

print(max)
