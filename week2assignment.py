# Variant 4: Concert Hall
class ConcertHall:
    def __init__(self, name: str, total_seats: int, booked_seats: int = 0):
        self._name = name
        self.total_s = total_seats
        self.booked_seats = booked_seats
    @property
    def name(self) -> str:
        return self._name
    @property
    def total_s(self) -> int:
        return self._total_s
    @total_s.setter
    def total_s(self, value):
        if value < 1:
            raise ValueError("Total seats must be at least 1")
        self._total_s = value
    @property
    def booked_s(self) -> int:
        return self._booked_seats
    @booked_s.setter
    def booked_seats(self, value) -> int:
        if value < 0:
            raise ValueError("Booked seats cannot be negative")
        if value > self.total_s:
            raise ValueError("Booked seats cannot exceed total seats")
        self._booked_seats = value
    @property
    def available_seats(self) -> int:
        return self.total_s - self.booked_seats
    @property
    def booking_rate(self) -> float:
        return round((self.booked_seats / self.total_s) * 100, 1)
    def reserve(self, seats) -> None:
        if seats <= 0:
            raise ValueError("Number of seats must be positive")
        if seats > self.available_seats:
            raise ValueError("Not enough available seats")
        self.booked_seats += seats
    def cancel(self, seats) -> None:
        if seats <= 0:
            raise ValueError("Number of seats must be positive")
        if seats > self.booked_seats:
            raise ValueError("Cannot cancel more than booked")
        self.booked_seats -= seats

h = ConcertHall("Grand", 200)
print(h.name, h.available_seats, h.booking_rate)

h.reserve(150)
print(h.booked_seats, h.booking_rate)

h.cancel(30)
print(h.available_seats)

try:
    h.reserve(100)
except ValueError as e:
    print(e)

try:
    h.name = "X"
except AttributeError:
    print("Cannot change hall name")

