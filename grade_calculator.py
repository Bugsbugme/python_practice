#Grade Calculator
#This calculator takes 2 student marks, averges them, and calculates their final Grade

divider = ('=' * 25)

#Validate input as an actual number that is not greater than 100 and ask for input again if criteria is not met
def InputValidation(userInput):

    while not userInput.isdecimal() or int(userInput) > 100:
        userInput = input('Invalid mark, try again: ')
    return int(userInput)

#Obtain marks from the user and print it after validating it then print them
projMark = int(InputValidation(input('What was your Project Mark?: ')))
examMark = int(InputValidation(input('What was you Exam Mark?: ')))
print(divider)
print('Project Mark:   |', projMark)
print('Exam Mark:      |', examMark)
print(divider)

#Calculate the final mark by adding the two marks together and dividing by two, then determine grade
def GradeCalc(mark1, mark2):
    markCalc = (mark1 + mark2) * 0.5

    if markCalc >= 80:
        grade = 'A'
    elif markCalc >= 70:
        grade = 'B'
    elif markCalc >= 60:
        grade = 'C'
    elif markCalc >= 50:
        grade = 'D'
    else: 
        grade = 'Fail'

    return [markCalc, grade]

#Create a new variable that executes the GradeCalc function on the final mark   
finalGrade = GradeCalc(projMark, examMark)

#Print the final mark and the final grade
print('Final Mark:     |',finalGrade[0])
print('Final Grade:    |',finalGrade[1])

#Testing
print(divider,'\n')
print('-=Test Cases=-\n')

#Test 1
testInput = [100, 100]
testOutput = [100, 'A']
# print('[Test 1]\n\nProject Mark    |',testInput[0],'\nExam Mark       |',testInput[1])
# print(divider)
# print('Final Mark      |',testOutput[0],'\nFinal Grade     |',testOutput[1])
# print(divider)
print('Test 1 |',testOutput == GradeCalc(*testInput))

#Test 2
testInput = [70, 70]
testOutput = [70, 'B']
print('Test 2 |',testOutput == GradeCalc(*testInput))

#Test 3
testInput = [60, 60]
testOutput = [60, 'C']
print('Test 3 |',testOutput == GradeCalc(*testInput))

#Test 4
testInput = [50, 50]
testOutput = [50, 'D']
print('Test 4 |',testOutput == GradeCalc(*testInput))

#Test 5
testInput = [40, 40]
testOutput = [40, 'Fail']
print('Test 5 |',testOutput == GradeCalc(*testInput))

#Test 6
testInput = [50, 28]
testOutput = [39, 'Fail']
print('Test 6 |',testOutput == GradeCalc(*testInput))

#Test 7
testInput = [34, 73]
testOutput = [53.5, 'D']
print('Test 7 |',testOutput == GradeCalc(*testInput))

#Test 8
testInput = [26, 49]
testOutput = [37.5, 'Fail']
print('Test 8 |',testOutput == GradeCalc(*testInput))

#Test 9
testInput = [69, 54]
testOutput = [61.5, 'C']
print('Test 9 |',testOutput == GradeCalc(*testInput))

#Test 10
testInput = [43, 72]
testOutput = [57.5, 'D']
print('Test 10|',testOutput == GradeCalc(*testInput))
