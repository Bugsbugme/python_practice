#Box Calculator
#This calculator takes a number of items and sorts them into the appropriate size boxes

divider = ('=' * 25)

#Validate input as an actual number and ask for input again if it isn't
def InputValidation(userInput):
    while not userInput.isdecimal():
        userInput = input('Only numbers are allowed, please input a valid number: ')
    return userInput

#Obtain number of items from the user and print it after validating it
userInput = int(InputValidation(input('Please specify how many items you want to store, rounding to whole numbers: ')))
print(divider)
print('Number of Items:   |', userInput)
print(divider)

#Define Box capacities
bigBox = 5
medBox = 3
smallBox = 1

#Calculate function
def BoxCalc(itemsNum):
    
    #Divide the number of items by the capacity of bigBox (5)
    bigboxTotal = itemsNum // bigBox

    #Create new variable from the number of items left over
    itemsLeft = itemsNum - bigboxTotal * bigBox

    #Take the number of items left and divide by the capacity of medBox (3)
    medboxTotal = itemsLeft // medBox

    #Update the itemsLeft variable with the new amount of items left over
    itemsLeft = itemsLeft - medboxTotal * medBox

    #Take the number of items left and divide by the capacity of smallBox (1)
    smallBoxTotal = itemsLeft // smallBox

    #Create a list with the results of each calculation
    return [bigboxTotal, medboxTotal, smallBoxTotal]

#Create a new variable that executes the BoxCalc function on the users input
answer = BoxCalc(userInput)

#Print the number of each size box needed and the total number of boxes
print('Big boxes Used:    |', answer[0])
print('Medium boxes Used: |', answer[1])
print('Small boxes Used:  |', answer[2])
print(divider)
print('Total boxes used:  |', answer[0] + answer[1] + answer[2])
print(divider,'\n')

#Testing
print('-=Test Cases=-\n')

#Test 1
testInput = 14
testOutput = [2, 1, 1]
print('Test 1 |',testOutput == BoxCalc(testInput))

#Test 2
testInput = 256
testOutput = [51, 0, 1]
print('Test 2 |',testOutput == BoxCalc(testInput))

#Test 3
testInput = 27
testOutput = [5, 0, 2]
print('Test 3 |',testOutput == BoxCalc(testInput))