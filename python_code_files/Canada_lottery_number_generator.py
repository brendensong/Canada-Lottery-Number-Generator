import random
import sys

print('{:*^50}'.format(' Select your Canada lottery type '))
print('-' * 50)
print('{: ^50}'.format('1. Lotto Max | 2. Lotto 6/49 | 3. Daily Grand'))
print('-' * 50)

answer = input()

type = (('Lotto Max', 7),
        ('Lotto 6/49', 6),
        ('Daily Grand', 5))

if answer != '1' and answer != '2' and answer != '3':
    sys.exit('<<< You chose the wrong type of lottery. Please try again. >>>')
  
numbers = []
answer = int(answer)

for i in range(0, type[answer - 1][1]):
    number = random.randint(1, 49)
    
    while number in numbers:
        number = random.randint(1, 49)

    numbers.append(number)

numbers.sort()

numbers_string = map(str, numbers)    

lottery_numbers = '   '.join(numbers_string)

if answer == 3:
    lottery_numbers = lottery_numbers + '  &  GN ' + str(random.randint(1, 7))

lottery_type = ' Your ' + str(type[answer - 1][0]) + ' numbers '

print('\n{:=^50}'.format(lottery_type))
print('\n{: ^50}'.format(lottery_numbers))
print('\n{:=^50}'.format(' Good luck! '))
