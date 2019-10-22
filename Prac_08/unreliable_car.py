# Import Statements
from Prac_08.car import Car
import random


class UnreliableCar(Car):
    """..."""

    def __init__(self, name, fuel, reliability):
        """..."""
        super().__init__(name, fuel)
        self.reliability = 70

    def drive(self, distance):
        random_number = random.randint(1, 101)
        if random_number > distance:
            pass
        else:
            distance_driven = super().drive(distance)
            return distance_driven

