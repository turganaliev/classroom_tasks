class Airplane():
    def __init__(self, make, model, year, max_speed, odometer=0, is_flying=False):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = odometer
        self.is_flying = is_flying

    def take_off(self):
        self.is_flying = True

    def land(self):
        self.is_flying = False

    def fly(self, km):
        self.odometer += km
        print(f'{self.make},{self.model},{self.year},{self.max_speed},{self.odometer},{self.is_flying}')


plane_1 = Airplane('Boeing', '700', 2020, '4000km/h')
plane_1.take_off()
#plane_1.land()
plane_1.fly(500)
