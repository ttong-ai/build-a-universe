from decimal import Decimal, getcontext

from constants import *

# Set the desired precision
getcontext().prec = 30  # 30 decimal places


def fmt(v: Decimal, precision: int = 14):
    return f"{v:.{precision}E}"


l_p = Decimal(planck_length)
t_p = Decimal(planck_time)
m_p = Decimal(planck_mass)
q_p = Decimal(planck_charge)
T_p = Decimal(planck_temperature)

print(f"l_p = {fmt(l_p)}")
print(f"t_p = {fmt(t_p)}")
print(f"m_p = {fmt(m_p)}")
print(f"q_p = {fmt(q_p)}")
print(f"T_p = {fmt(T_p)}")
