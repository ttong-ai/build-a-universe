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

d_0 = 44  # !5 derangement of 5
d_1 = 35  # 5*7
d_2 = 18  # 2 * (sqrt(d0-d1)+/-0)^2
d_3 = 8  # 2 * (sqrt(d0-d1)-1)^2
d_4 = 32  # 2 * (sqrt(d0-d1)+1)^2


def hyperbolic_vertext_equation(x):
    lhs = 1/x + x + x**3/(2*pi)
    rhs = Decimal(((1j**1j)**(-math.pi/2)).real) - m_p
    return lhs - rhs


def get_phi(n: int):
    """This function gets the Planck units digits"""
    if n < 0 or n > 4:
        raise ValueError("n needs to be within [0, 4]")
    if n == 0:
        return math.log(Decimal(d_0) / (pi * Decimal(math.sinh(0.5**2)**2)))
    elif n == 1:
        return math.log(Decimal(d_1) / Decimal(math.sinh(math.sinh(1./7))**-1))
    elif n == 2:
        return math.log(Decimal(d_2) / Decimal(5 / (math.sqrt(7*math.pi) * 3**(1/3)) * (2**(2*5) * math.e**math.pi)**(-1/8) * (math.gamma(1/4))**2))
    elif n == 3:
        return math.log(Decimal(d_3) / Decimal(2*pi*5 * Decimal(math.cos(7./5)**2)))
    elif n == 4:
        return math.log(Decimal(d_4) / Decimal(2 * math.cosh(math.log(7)) * math.cosh(5/2)**2 * math.cos(7/5)**2))


def calc_electron_mass(order: int = 1):
    if order == 0:
        return 2 * Vfe * m_p**4
    elif order == 1:
        return 2 * Vfe * Decimal(2.17642683817579E-8)**4 * (1 + Decimal(math.sinh(math.sinh(44/7)**(-1))**(-1)) * d_sq)
    else:
        raise NotImplementedError("n has to be 0 or 1")


phi_0 = get_phi(0)
phi_1 = get_phi(1)
phi_2 = get_phi(2)
phi_3 = get_phi(3)
phi_4 = get_phi(4)


print("==========================")
print(f"l_p = {fmt(l_p)} m")
print(f"t_p = {fmt(t_p)} s")
print(f"m_p = {fmt(m_p)} kg")
print(f"q_p = {fmt(q_p)} C")
print(f"T_p = {fmt(T_p)} K")
print(f"d_sq = {fmt(d_sq)}")
print(f"(Ж_1^2 + Ж_2^2 + Ж_3^2 + Ж_4^2) / 4Pi = {fmt((DecimalComplex(0, 0) + Ж_1**2 + Ж_2**2 + Ж_3**2 + Ж_4**2)/pi/4.0)}")
print()

print(f"fine structure constant = {fmt(alpha)}")
print(f"Ж_1^2 - alpha = {fmt(Ж_1**2 - alpha)}")
print("Residual of hyperbolic vortext equation:", hyperbolic_vertext_equation(Ж_1))
print(f"Electron Mass = {fmt(el_mass)}")
print(f"Calculated Electron Mass: ", fmt(calc_electron_mass(1)))
print()

print(f"Phi_0 = {phi_0}")
print(f"Phi_1 = {phi_1}")
print(f"Phi_2 = {phi_2}")
print(f"Phi_3 = {phi_3}")
print(f"Phi_4 = {phi_4}")
