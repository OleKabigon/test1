#This app will draw an F with X

numbers = [1, 1, 1, 1, 5]

for x_count in numbers:  # outside loop will step through the list of numbers
    output = ''  # initialize variable that will store the letter x
    for count in range(x_count):  # sets x_count to number in list of "numbers"
        output += 'x'  # appending the letter x to the variable output
    print(output)
