class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 70

    def __add_distance(self, km):
        self.odometer += km
        print(f'km has driven: {self.odometer}')

    def __subtract_fuel(self, km):
        self.fuel -= (km / 10)  #10lt/100km
        print(f'liters left: {self.fuel}')

    def drive(self, km):
        print(f'{self.make} {self.model} {self.year}')

        if km/10 < self.fuel:
            self.__add_distance(km)
            self.__subtract_fuel(km)
            print("Let's drive!")
        else:
            print('Need more fuel, please, fill more!')

car_1 = Car('bmw', 'i8', 2020)
car_1.drive(10)
