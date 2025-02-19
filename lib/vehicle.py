class Vehicle:
    def __init__(self, wheel_size, wheel_number):
        """Initialize a vehicle with wheel size and number."""
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def go(self):
        """Simulate vehicle movement."""
        return "vrrrrrrrooom!"

    def fill_up_tank(self):
        """Simulate filling up the vehicle's tank."""
        return "filling up!"
