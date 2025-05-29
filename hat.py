import random

class Hat:

    houses = ["Red", "Blue", "Green"]

    @classmethod    
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


name = input('enter a name: ')
Hat.sort(name)