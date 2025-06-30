
# the most accurate and easiest
def easiest_way(a,b):
    return a / (1/b)

'''
using addition
'''

class int_using_addition: # easy doesn't deal with floats some reffer them to decimals, doubles or fractions
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return f"{self.a =} {self.b =}"
    def multiply(self):

        # is your gross input negative? read keenly
        negative = False
        if self.a == 0 or self.b == 0:
            return 0
        if self.a < 0:
            self.a = self.a * -1
            if self.b < 0:
                negative = False
                self.b = self.b * -1
            else:
                negative = True
        else:
            if self.b < 0:
                self.b = self.b * -1
                negative = True
            else:
                negative = False
        
        def add(a,b):
            return b + add(a - 1, b) if a-1 > 0 else b
        return add(self.a,self.b) if not negative else - add(self.a,self.b)


class using_addition:
    def __init__(self,a,b):
        while a % 2 != 0:
            a = a / .5 # double a
            b = b / 2 # give half of b to b
        self.a = a
        self.b = b
    def __str__(self):
        return f"{self.a =} {self.b =}"
    def multiply(self):

        # is your gross input negative? read keenly
        negative = False
        if self.a == 0 or self.b == 0:
            return 0
        if self.a < 0:
            self.a = self.a * -1
            if self.b < 0:
                negative = False
                self.b = self.b * -1
            else:
                negative = True
        else:
            if self.b < 0:
                self.b = self.b * -1
                negative = True
            else:
                negative = False
        
        def add(a,b):
            return b + add(a - 1, b) if a-1 > 0 else b
        return add(self.a,self.b) if not negative else - add(self.a,self.b)




# main.py 