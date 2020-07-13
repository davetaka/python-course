import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())


# my suggestion

class MyDice:
    def roll(self):
        return random.randint(1, 6)


print("My suggestion")

dice1 = MyDice()
dice2 = MyDice()

print(f"({dice1.roll()}, {dice2.roll()})")
