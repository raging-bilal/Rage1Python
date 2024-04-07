import math

class Polynomial:
    """
    Represents a polynomial function.
    """
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def evaluate(self, x):
        """
        Evaluates the polynomial function for the given value of x.
        """
        result = 0
        for i in range(len(self.coefficients)):
            result += self.coefficients[i] * (x ** (len(self.coefficients) - i - 1))
        return result

class Exponential:
    """
    Represents an exponential function.
    """
    def __init__(self, base):
        self.base = base

    def evaluate(self, x):
        """
        Evaluates the exponential function for the given value of x.
        """
        return math.exp(self.base * x)

arr = [4, 0, 2, 9]
f = Polynomial(arr)

x = 5
result = f.evaluate(x)
print(f"f({x}) = {result}")

