from const_of_nature import *
from const_of_nature.lib import Decimal, DecimalComplex, getcontext

# Set the desired precision
getcontext().prec = 30  # 30 decimal places


def fmt(v: Decimal, precision: int = 14):
    return f"{v:.{precision}E}"


def hyperbolic_vertext_equation(x):
    return 1/x + x + x**3/(2*Decimal(math.pi)) - Decimal(((1j**1j)**(-math.pi/2)).real) + Decimal(planck_mass)


alpha = Decimal(constants['fine_structure_constant'])

l_p = Decimal(planck_length)
t_p = Decimal(planck_time)
m_p = Decimal(planck_mass)
q_p = Decimal(planck_charge)
T_p = Decimal(planck_temperature)
d_sq = l_p * m_p / q_p**2

Ж_1 = Decimal(special_constants['Ж_1'])
Ж_2 = Decimal(special_constants['Ж_2'])
Ж_3 = DecimalComplex(special_constants['Ж_3'].real, special_constants['Ж_3'].imag)
Ж_4 = DecimalComplex(special_constants['Ж_4'].real, special_constants['Ж_4'].imag)
Ж_r = Decimal(special_constants['Ж_r'])
Ж_θ = Decimal(special_constants['Ж_θ'])


print(f"l_p = {fmt(l_p)}")
print(f"t_p = {fmt(t_p)}")
print(f"m_p = {fmt(m_p)}")
print(f"q_p = {fmt(q_p)}")
print(f"T_p = {fmt(T_p)}")
print(f"d_sq = {fmt(d_sq)}")
print(f"fine structure constant = {fmt(alpha)}")
print(f"Ж_1^2 - alpha = {fmt(Ж_1**2 - alpha)}")
print(hyperbolic_vertext_equation(Ж_1))

