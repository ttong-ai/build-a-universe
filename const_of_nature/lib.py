from decimal import Decimal, getcontext

# Set the desired precision
getcontext().prec = 30  # 30 decimal places


class DecimalComplex:
    def __init__(self, real, imag):
        self.real = Decimal(str(real))
        self.imag = Decimal(str(imag))

    def __repr__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}j"
        else:
            return f"{self.real} - {-self.imag}j"

    def __add__(self, other):
        return DecimalComplex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return DecimalComplex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return DecimalComplex(real, imag)

    def __truediv__(self, other):
        denominator = other.real**2 + other.imag**2
        real = (self.real * other.real + self.imag * other.imag) / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator
        return DecimalComplex(real, imag)

    def __pow__(self, n):
        result = DecimalComplex(1, 0)
        temp = self
        while n > 0:
            if n % 2 == 1:
                result *= temp
            temp *= temp
            n //= 2
        return result
