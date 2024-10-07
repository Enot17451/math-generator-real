from random import *

class Real:

    def __init__(self):
        number = randint(0,9)
        real = randint(0,9)/10
        mantissa = randint(1,3)
        self.sign = choice(["+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-"])
        self.number = (number + real)/(10*mantissa)

    def __str__(self):
        return f"{self.sign}{self.number}"

n=10
for x in range(n):
    print(Real())

