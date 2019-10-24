import random


class Dice:

    def roll(self):
        number1 = random.randint(0,9)
        number2 = random.randint(0,9)
        return number1, number2


x = Dice()
print(x.roll())