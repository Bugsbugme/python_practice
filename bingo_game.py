# Bingo Game

import random
import sys
import os

divider = ('=' * 20)
trophy = '\U0001F3C6'
sadFace = '\U0001F641'
happyFace = '\U0001F603'
winFace = '\U0001F604'
woopsieFace = '\U0001F62E'
game = '\U0001F3B0'
dice = '\U0001F3B2'
flag = '\U0001F38C'

# Random Number Generator
# Genaerate a list of random numbers for the Bing Card
randmin = 1
randmax = 80
minsize = 0
maxsize = 10
bingoCard = []
for _ in range(minsize, maxsize):
    randomNumber = random.randint(randmin, randmax)
    bingoCard.append(randomNumber)

# Validate input as an actual number that is not greater than 80 and ask for input again if criteria is not met
def InputValidation(userInput):
    while not userInput.isdecimal() or int(userInput) > 80:
        print('Invalid Input!', woopsieFace)
        userInput = input('Try again: ')
    return int(userInput)

# Number Checker
# Take the user input and check it against the number list gernerated by the Random Number Generator
def NumberChecker(number, bingoCard):
    if number in bingoCard:
        print(number, 'is a match!', happyFace)
        bingoCard.remove(number)
        if bingoCard:
            print('Keep going: ', end="")
            return 'resultMatch'
        else:
            print(divider)
            print('       ', winFace)
            print('      Bingo!\nAll numbers cleared')
            print(trophy, '-=You Win!=-', trophy)
            print(divider)
            return 'resultWin'
    else:
        print('Sorry, no match', sadFace, '\nTry again: ', end="")
        return 'resultNoMatch'


# Welcome Message and Game Instructions
print(divider * 2)
print('           ', flag, winFace, flag)
print('-=Welcome to Bingo Supa Fun Game!=-')
print('           ', dice, dice, dice)
print(divider * 2)
print('-=Instructions=-\nYour Bingo Card has 10 random numbers on it.\nSimply enter a number between 1 and 80.\nIf your number matches a number on the Bingo Card, it gets cleared from the card.\nKeep guessing until you clear the whole card.\nGLHF!', winFace)
print(divider * 2)
print('DEBUG:', bingoCard)
print('Choose a number between 1 and 80: ', end="")

# Get user input, validate it, and run it through the Number Checker
while bingoCard:
    userNumber = NumberChecker(InputValidation(input()), bingoCard)

# Testing
print('\n-=Test Cases=-')

trophy = ''
sadFace = ''
happyFace = ''
winFace = ''
woopsieFace = ''
game = ''
dice = ''
flag = ''

testCard = [43, 21, 14]

# Test 1
testInput = 43
testResult = 'resultMatch'
sys.stdout = open(os.devnull, "w")
testOutput = NumberChecker(testInput, testCard)
sys.stdout = sys.__stdout__
print('Test 1 |', testOutput == testResult)

# Test 2
testInput = 5
testResult = 'resultNoMatch'
sys.stdout = open(os.devnull, "w")
testOutput = NumberChecker(testInput, testCard)
sys.stdout = sys.__stdout__
print('Test 2 |', testOutput == testResult)

# Test 3
testInput = 21
testResult = 'resultMatch'
sys.stdout = open(os.devnull, "w")
testOutput = NumberChecker(testInput, testCard)
sys.stdout = sys.__stdout__
print('Test 3 |', testOutput == testResult)

# Test 4
testInput = 14
testResult = 'resultWin'
sys.stdout = open(os.devnull, "w")
testOutput = NumberChecker(testInput, testCard)
sys.stdout = sys.__stdout__
print('Test 4 |', testOutput == testResult)
