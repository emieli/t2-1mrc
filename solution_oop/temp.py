class Temp:
    """
    Class Temp is a blueprint/template for how city temperature measurements
    are handled. We want to keep track of the min/max/avg recorded temperatures
    for the city and display the data in a standardized format.
    """

    def __init__(self, city: str, temp: float):
        """
        Initialize new Temp instance; creating local variables and supplying
        first measurement value (temp)
        """
        self.city: str = city
        self.min: float = temp
        self.max: float = temp
        self._sum: float = temp
        self._sum_counter: int = 1

    def add_measurement(self, temp: float):
        """Add measurement to existing instance"""
        if temp < self.min:
            self.min = temp
        if temp > self.max:
            self.max = temp
        self._sum += temp
        self._sum_counter += 1

    def __str__(self) -> str:
        """Print instance in this particular format"""
        return f"{self.city}={self.min}/{self.avg:.1f}/{self.max}"

    @property
    def avg(self) -> float:
        """
        Return average value by dividing the sum of all
        measurements by the number of recorded measurements
        """
        return self._sum / self._sum_counter
