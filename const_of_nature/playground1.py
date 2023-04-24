import math

from const_of_nature import *
from const_of_nature.lib import Decimal, DecimalComplex, getcontext, fmt

# Set the desired precision
getcontext().prec = 30  # 30 decimal places


pi = Decimal(math.pi)
e = Decimal(math.e)
alpha = Decimal(constants['fine_structure_constant'])
el_mass = Decimal(constants['electron_mass'])
proton_mass = Decimal(constants['proton_mass'])
neutron_mass = Decimal(constants['neutron_mass'])

l_p = Decimal(planck_length)
t_p = Decimal(planck_time)
m_p = Decimal(planck_mass)
q_p = Decimal(planck_charge)
T_p = Decimal(planck_temperature)
d_sq = l_p * m_p / q_p**2
Vfe = Decimal(constants['V_fe'])

Ж_1 = Decimal(special_constants['Ж_1'])
Ж_2 = Decimal(special_constants['Ж_2'])
Ж_3 = DecimalComplex(special_constants['Ж_3'].real, special_constants['Ж_3'].imag)
Ж_4 = DecimalComplex(special_constants['Ж_4'].real, special_constants['Ж_4'].imag)
Ж_r = Decimal(special_constants['Ж_r'])
Ж_θ = Decimal(special_constants['Ж_θ'])


def hyperbolic_vertext_equation(x):
    return 1/x + x + x**3/(2*pi) - Decimal(((1j**1j)**(-math.pi/2)).real) + m_p


def calc_electron_mass(order: int = 1):
    if order == 0:
        return 2 * Vfe * m_p**4
    elif order == 1:
        return 2 * Vfe * m_p**4 * (1 + d_sq * Decimal(math.sinh(math.sinh(44.0/7)**-1)**-1))
    else:
        raise NotImplementedError("n has to be 0 or 1")


print(f"l_p = {fmt(l_p)} m")
print(f"t_p = {fmt(t_p)} s")
print(f"m_p = {fmt(m_p)} kg")
print(f"q_p = {fmt(q_p)} C")
print(f"T_p = {fmt(T_p)} K")
print(f"d_sq = {fmt(d_sq)}")
print(f"(Ж_1^2 + Ж_2^2 + Ж_3^2 + Ж_4^2) / 4Pi = {fmt((DecimalComplex(0, 0) + Ж_1**2 + Ж_2**2 + Ж_3**2 + Ж_4**2)/pi/4.0)}")

print(f"fine structure constant = {fmt(alpha)}")
print(f"Ж_1^2 - alpha = {fmt(Ж_1**2 - alpha)}")
print("Residual of hyperbolic vortext equation:", hyperbolic_vertext_equation(Ж_1))
print(f"Electron Mass = {fmt(el_mass)}")
print(f"Calculated Electron Mass: ", fmt(calc_electron_mass(1)))
