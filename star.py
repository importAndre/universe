import math

class Star:

    gravitational_constant = 6.673 * (10 ** (- 11)) # Gravitational constant in m^3 kg^-1 s^-2

    def __init__(self, mass, radius, lambda_max):
        """
            The mass should be in kilograms
            The radius should be in meters
            The lambda_max sould be in meters. Ex. 500nm = 5 * (10 ** -7)
        """

        self.mass = mass # star mass in kilograms
        self.radius = radius # star radius in meters
        self.lambda_max = lambda_max # highest intensity of the wavelength
        self.area = 4 * math.pi * (radius ** 2)

    def average_density(self):
        """
            return: density in kg/m³
        """
        volume = (4 / 3) * 3.1415 * (self.radius ** 3)
        return self.mass / volume
    
    def surface_gravitational_field(self):
        """
            return: surface gravity in N/kg
        """
        return Star.gravitational_constant * self.mass / (self.radius ** 2)
    
    def average_temperature(self):
        # Here I'm using Wien's Law
        wiens_constant = 2.897771955 * (10 ** (-3))
        return wiens_constant / self.lambda_max # returns the temperature in kelvin 
    
    def luminosity(self):
        """
            return: luminosity in watts (W)
        """
        stefan_boltzmann_constat = 5.670374419 * (10 ** -8)
        return 4 * math.pi * (self.radius ** 2) * stefan_boltzmann_constat * (self.average_temperature() ** 4)

    def central_pressure(self):
        return (2 / 3) * (Star.gravitational_constant * self.mass ** 2) / (4 * math.pi * self.radius **4)

sun_mass = 1.989 * (10 ** 30)
sun_radius = 696_340_000
sun_lambda_max = 5 * (10 ** (-7))
sun = Star(sun_mass, sun_radius, sun_lambda_max)