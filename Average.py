average = 0
total = 0
howManyEntered = 0
howMany = int(input('How many test scores would you like to average: '))
while howManyEntered < howMany:
    testScore = int(input('Enter test score: '))
    total = total + testScore
    howManyEntered = howManyEntered + 1
average = total / howMany
print('The average for test scores you entered is: ',average)
