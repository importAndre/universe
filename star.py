import math

class Star:

    gravitational_constant = 6.673 * (10 ** (- 11)) # Gravitational constant in m^3 kg^-1 s^-2

    def __init__(self, mass, radius, lambda_max, chemical_composition):
        """
            The mass should be in kilograms
            The radius should be in meters
            The lambda_max sould be in meters. Ex. 500nm = 5 * (10 ** -7)
        """

        self.mass = mass # star mass in kilograms
        self.radius = radius # star radius in meters
        self.lambda_max = lambda_max # highest intensity of the wavelength
        self.area = 4 * math.pi * (radius ** 2)
        self.chemical_composition = chemical_composition

    def average_density(self):
        """
            return: density in kg/m³
        """
        volume = (4 / 3) * Math.pi * (self.radius ** 3)
        return self.mass / volume
    
    def surface_gravitational_field(self):
        """
            return: surface gravity in N/kg
        """
        return Star.gravitational_constant * self.mass / (self.radius ** 2)
    
    def average_temperature(self):
        """
            return: the temperature in kelvin
        """
        # Here I'm using Wien's Law
        wiens_constant = 2.897771955 * (10 ** (-3))
        return wiens_constant / self.lambda_max 
    
    def luminosity(self):
        """
            return: luminosity in watts (W)
        """
        stefan_boltzmann_constat = 5.670374419 * (10 ** -8)
        return 4 * math.pi * (self.radius ** 2) * stefan_boltzmann_constat * (self.average_temperature() ** 4)

    def central_pressure(self):
        return (2 / 3) * (Star.gravitational_constant * self.mass ** 2) / (4 * math.pi * self.radius **4)

    def spectral_classification(self):
        temperature = self.average_temperature()

        if temperature < 3700:
            return 'M'
        elif temperature >= 3700 and temperature < 5200:
            return 'K'
        elif temperature >= 5200 and temperature < 6000:
            return 'G'
        elif temperature >= 6000 and temperature < 7500:
            return 'F'
        elif temperature >= 7500 and temperature < 10000:
            return 'A'
        elif temperature >= 10000 and temperature < 30000:
            return 'B'
        elif temperature > 30000:
            return 'O'
        else:
            return "This object doesn't have enough temperature to be a star"


sun_mass = 1.989 * (10 ** 30)
sun_radius = 696_340_000
sun_lambda_max = 5 * (10 ** (-7))
chemical_composition = {
    'hydrogen': 0.921,
    'helium': 0.079
}
sun = Star(sun_mass, sun_radius, sun_lambda_max, chemical_composition)
print(sun.spectral_classification())
