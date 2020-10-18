import random

print('\n\nWelcome to the dice roller!\n\n')

#create a function to test if the input is an integer and prompt for a integer if not
def input_number(message):
    while True:
        try:
            userinput =int(input(message))
        except ValueError:
            print('This is not an integer! Try again.')
            continue
        else:
            return userinput
            break
        
results = []

#Prompt user for how many rolls will be needed
rolls = input_number('Enter how many die rolls you need using a digit: ')

#prompt user for how many sides the die should have    
die = input_number('How many sides on the die?:')



#for $rolls roll a die with values between 1 and the number of side
for x in range(int(rolls)):
    results.append(random.randint(1,die))

#print the results of the die roller in a list
print('Your rolls are : ')
print(results)
