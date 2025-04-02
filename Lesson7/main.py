class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.tank_level = 0.0 #float from 0 to 1.0
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def fill_gas_tank(self,amount):
        self.tank_level += amount
        if self.tank_level > 1.0:
            self.tank_level = 1.0
            print("Your tank is full!")
        

class ElectricCar(Car):
    def __init__(self,make,model,year,battery_capacity):
        super().__init__(make,model,year)
        self.battery_capacity = battery_capacity

def main():
    my_leaf = ElectricCar("Nissan","Leaf",2024,60)
    print(my_leaf.battery_capacity)
    print(my_leaf.make)


if __name__ == '__main__':
    main()