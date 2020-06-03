import random

MIN = 1
MAX = 6
roll_again = 'y'
while roll_again == 'y':
    print('Rolling the dices...')
    print('The values are....')
    dice1 = random.randint(MIN, MAX)
    print("The value of the dice 1 is: ",dice1)
    dice2 = random.randint(MIN, MAX)
    print("The value of the dice 2 is: ", dice2)


    roll_again = input('Roll the dices again? (y / n): ')