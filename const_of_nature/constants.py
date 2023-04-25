# Importing the necessary libraries
import math

# Defining common physical constants
constants = {
    'pi': math.pi,
    'e': math.e,
    'golden_ratio': (1 + math.sqrt(5)) / 2,
    'P_up': 2.29558714939263,  # universal parabolic constant
    'tau': 2 * math.pi,
    'speed_of_light': 2.99792458e8,  # m/s
    'planck_constant': 6.62607015e-34,  # Js
    'reduced_planck_constant': 1.054571817e-34,  # Js
    'gravitational_constant': 6.67430e-11,  # m^3/kg/s^2
    'electron_charge': 1.602176634e-19,  # C
    'electron_mass': 9.1093837015e-31,  # kg
    'proton_mass': 1.67262192369e-27,  # kg
    'neutron_mass': 1.67492749804e-27,  # kg
    'avogadro_number': 6.02214076e23,  # mol^-1
    'boltzmann_constant': 1.380649e-23,  # J/K
    'gas_constant': 8.314462618,  # J/mol/K
    'stefan_boltzmann_constant': 5.670374419e-8,  # W/m^2/K^4
    'vacuum_electric_permittivity': 8.8541878128e-12,  # F/m (farads per meter),
    'vacuum_magnetic_permittivity': 1.25663706212e-6,  # N/A^2 (newtons per ampere squared)
    'vacuum_impedance': 376.730313668,  # ohms (volts per ampere)
    'electron_volt': 1.602176634e-19,  # J
    'atomic_mass_unit': 1.66053906660e-27,  # kg
    'bohr_radius': 5.29177210903e-11,  # m
    'hartree_energy': 4.3597447222071e-18,  # J
    'rydberg_constant': 10973731.568160,  # 1/m
    'fine_structure_constant': 7.2973525693e-3,  # 1
    'electron_g_factor': -2.00231930436182,  # 1
    'proton_g_factor': 5.585694702,  # 1
    'neutron_g_factor': -3.82608545,  # 1
    'standard_acceleration_gravity': 9.80665,  # m/s^2
    'standard_atmosphere': 101325,  # Pa
    'standard_state_pressure': 100000,  # Pa
    'standard_state_temperature': 273.15,  # K
    'standard_temperature': 273.15,  # K
    'standard_volume': 0.022413996,  # m^3/mol
    'standard_volume_temperature': 273.15,  # K
    'standard_volume_pressure': 101325,  # Pa
    'standard_volume_molar_mass': 0.022413996,  # m^3/mol
    'G_Gi': 1.01494160640965,  # Gieseking's constant
    'V_fe': 2.02988321281930,  # volume of figure eight knot complement
}

# Calculating Planck units
planck_length = math.sqrt(constants['reduced_planck_constant'] * constants['gravitational_constant'] / constants['speed_of_light']**3)
planck_time = math.sqrt(constants['reduced_planck_constant'] * constants['gravitational_constant'] / constants['speed_of_light']**5)
planck_mass = math.sqrt(constants['reduced_planck_constant'] * constants['speed_of_light'] / constants['gravitational_constant'])
planck_temperature = math.sqrt(constants['speed_of_light']**5 * constants['reduced_planck_constant'] / (constants['gravitational_constant'] * constants['boltzmann_constant']**2))
planck_charge = 2 * math.sqrt(math.pi * constants['vacuum_electric_permittivity'] * constants['speed_of_light'] * constants['reduced_planck_constant'])

# Defining Planck units as a dictionary
planck_units = {
    'planck_length': planck_length,
    'planck_time': planck_time,
    'planck_mass': planck_mass,
    'planck_temperature': planck_temperature,
    'planck_charge': planck_charge,
}

special_constants = {
    'Ж_1': 0.0854245431533304,
    'Ж_2': 3.66756753485499,
    'Ж_3': - 1.87649603900417 + 4.06615262615972j,
    'Ж_4': - 1.87649603900417 - 4.06615262615972j,
    'Ж_r': 4.47826244916751,
    'Ж_θ': 2.00316562310924,
}

# Printing common physical constants
print("Common Physical Constants:")
for name, value in constants.items():
    print(f"{name}: {value}")
print()

# Printing Planck units
print("\nPlanck Units:")
for name, value in planck_units.items():
    print(f"{name}: {value}")
print()
