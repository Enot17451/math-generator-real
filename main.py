from random import *

class RealNumber:

    def __init__(self):
        self.mantissa = 10**randint(1,2)
        self.number = randint(11, 50)/self.mantissa
        self.sign = choice(["+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-"])

    def __str__(self):
        if self.sign == "+":
            return f"{self.number:.2f}"
        else:
            return f"{self.sign}{self.number:.2f}"

class RealQuestion:

    def __init__(self,action):
        if action == "*":
            self.sign = "*"
        else:
            self.sign = choice(["+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-"])
        self.a = RealNumber()
        self.b = RealNumber()

    def __str__(self):
        return f"{self.a} {self.sign} {self.b}"


n = 20
for x in range(n):
    print(RealQuestion("+"))
