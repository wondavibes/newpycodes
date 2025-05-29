""""to use a module into a python program we usethe keyword import"""
import random
coin = random.choice(["heads", "tails"])
print(coin)
"""from is another keyword for importing specific functions from a module (from random import choice,then coin=choice)"""

num = random.randint(1,5)
print(num)

cards = ["jack","queens","king"]
random.shuffle(cards)
for card in cards:
    print(card)