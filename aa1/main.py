
# the most accurate and easiest
def easiest_way(a,b):
    return a / (1/b)

'''
using addition
'''

class using_addition:
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
        
