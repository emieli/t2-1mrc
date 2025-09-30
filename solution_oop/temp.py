class Temp:
    def __init__(self, city: str, temp: float):
        """Create new Temp instance, containing min/max/sum values"""
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
    def avg(self) -> int:
        """
        Return average value by dividing the sum of all
        measurements by the number of recorded measurements
        """
        return self._sum / self._sum_counter
