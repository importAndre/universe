class Star:

    def __init__(self, mass, radius, lambda_max):
        """
            The mass should be in kilograms
            The radius should be in meters
        """
        self.mass = mass # star mass in kilograms
        self.radius = radius # star radius in meters
        self.lambda_max = lambda_max # highest intensity of the wavelength

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
        gravitational_constant = 6.673 * (10 ** (- 11))
        return gravitational_constant * self.mass / (self.radius ** 2)
    
    def average_temperature(self):
        # Here I'm using Wien's Law
        wiens_constant = 2.897771955 * (10 ** (-3))
        return wiens_constant / self.lambda_max # returns the temperature in kelvin 
    


    
# earth_mass = 5.97 * 10 ** 24
# earth_radius = 6.38 * 10 ** 6
# earth = Star(earth_mass, earth_radius)

sun_mass = 2 * 10 ** 30
sun_radius = 696_340_000
sun_lambda_max = 5 * (10 ** (-7))
sun = Star(sun_mass, sun_radius, sun_lambda_max)
print(sun.average_temperature())