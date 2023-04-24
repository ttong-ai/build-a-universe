from decimal import Decimal, getcontext
import math
from mpmath import mp, mpc
from typing import Union

# Set the desired precision
getcontext().prec = 30  # 30 decimal places

# Taylor series terms
EXP_TERMS = 100
LN_TERMS = 100


def fmt(v: Union[Decimal, "DecimalComplex"], precision: int = 14):
    if isinstance(v, Decimal):
        return f"{v:.{precision}E}"
    elif isinstance(v, DecimalComplex):
        if v.imag >= 0:
            return f"{fmt(v.real)} + {fmt(v.imag)}j"
        else:
            return f"{fmt(v.real)} - {fmt(-v.imag)}j"


class DecimalComplex:
    def __init__(self, real, imag):
        self.real = Decimal(str(real))
        self.imag = Decimal(str(imag))

    def __repr__(self):
        if self.imag >= 0:
            return f"{fmt(self.real)} + {fmt(self.imag)}j"
        else:
            return f"{fmt(self.real)} - {fmt(-self.imag)}j"

    def __add__(self, other):
        if isinstance(other, DecimalComplex):
            return DecimalComplex(self.real + other.real, self.imag + other.imag)
        elif isinstance(other, Decimal):
            return DecimalComplex(self.real + other, self.imag)
        elif isinstance(other, (float, int)):
            return DecimalComplex(self.real + Decimal(other), self.imag)

    def __sub__(self, other):
        if isinstance(other, DecimalComplex):
            return DecimalComplex(self.real - other.real, self.imag - other.imag)
        elif isinstance(other, Decimal):
            return DecimalComplex(self.real - other, self.imag)
        elif isinstance(other, (float, int)):
            return DecimalComplex(self.real - Decimal(other), self.imag)

    def __mul__(self, other):
        if isinstance(other, DecimalComplex):
            real = self.real * other.real - self.imag * other.imag
            imag = self.real * other.imag + self.imag * other.real
            return DecimalComplex(real, imag)
        elif isinstance(other, Decimal):
            real = self.real * other
            imag = self.imag * other
            return DecimalComplex(real, imag)
        elif isinstance(other, (float, int)):
            real = self.real * Decimal(other)
            imag = self.imag * Decimal(other)
            return DecimalComplex(real, imag)

    def __truediv__(self, other):
        if isinstance(other, DecimalComplex):
            denominator = other.real**2 + other.imag**2
            real = (self.real * other.real + self.imag * other.imag) / denominator
            imag = (self.imag * other.real - self.real * other.imag) / denominator
            return DecimalComplex(real, imag)
        elif isinstance(other, Decimal):
            denominator = other ** 2
            real = self.real * other / denominator
            imag = self.imag * other / denominator
            return DecimalComplex(real, imag)
        elif isinstance(other, (float, int)):
            denominator = Decimal(other) ** 2
            real = self.real * Decimal(other) / denominator
            imag = self.imag * Decimal(other) / denominator
            return DecimalComplex(real, imag)

    def polar(self):
        r = (self.real**2 + self.imag**2).sqrt()
        theta = Decimal(math.atan2(self.imag, self.real))
        return r, theta

    @staticmethod
    def from_polar(r, theta):
        real = r * Decimal(math.cos(theta))
        imag = r * Decimal(math.sin(theta))
        return DecimalComplex(real, imag)

    def __pow__(self, other):
        if isinstance(other, int):
            result = DecimalComplex(1, 0)
            temp = self
            while other > 0:
                if other % 2 == 1:
                    result *= temp
                temp *= temp
                other //= 2
            return result
        elif isinstance(other, (Decimal, float)):
            if isinstance(other, float):
                other = Decimal(other)
            base = mpc(str(self.real), str(self.imag))
            exponent = mpc(str(other), "0.0")
            result = base ** exponent
            return DecimalComplex(result.real, result.imag)
        elif isinstance(other, DecimalComplex):
            base = mpc(str(self.real), str(self.imag))
            exponent = mpc(str(other.real), str(other.imag))
            result = base ** exponent
            return DecimalComplex(result.real, result.imag)


def quicktest_decimal_complex():
    # Example usage
    a = DecimalComplex(1.23456789, -2.3456789)
    # b = DecimalComplex(3.45678901, 4.56789012)
    c = DecimalComplex(0.5, 0.5)

    result = a ** c
    print(f"a ** c = {result}")
    print(f"a ** c = {(1.23456789-2.3456789j)**(0.5+0.5j)}")


if __name__ == "__main__":
    quicktest_decimal_complex()
