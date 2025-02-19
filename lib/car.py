from vehicle import Vehicle

class Car(Vehicle):
    def go(self):
        """Override the go method to provide a louder engine sound."""
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
