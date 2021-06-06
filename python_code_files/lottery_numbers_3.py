import random
import sys

print('Select your lottery type: \n1. Lotto Max | 2. Lotto 6/49')

answer = int(input())

if answer != 1 and answer != 2:
    sys.exit('You chose the wrong type of lottery. Please try again.')
  
lottery_numbers = []

if answer == 1:
    numbers = 7
    
elif answer == 2:
    numbers = 6

for i in range(0, numbers):
    number = random.randint(1, 49)
    
    while number in lottery_numbers:
        number = random.randint(1, 49)

    lottery_numbers.append(number)

lottery_numbers.sort()

print('Your lottery numbers:\n')

for num in lottery_numbers:
    print(num, end=' ')
    
if answer == 3:
    print('& GN', random.randint(1, 7))
