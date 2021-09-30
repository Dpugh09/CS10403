average = 0
total = 0
howManyEntered = 0
print('How many test scores would you like to average')
howMany = int(input(''))
while howManyEntered < howMany:
    print('Enter test score:')
    testScore = int(input(''))
    total = total + testScore
    howManyEntered = howManyEntered + 1
average = total / howMany
print('The average for test scores you entered is: ',average)
