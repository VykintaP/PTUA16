class Maintenance:
    def __init__(self, maintenance_cost):
        self.maintenance_cost = maintenance_cost

    def calculate_maintenance(self):
        return f"Maintenance cost is {self.maintenance_cost} EUR."


class Transport:

    def __init__(self, capacity, max_speed, fuel):
        self.capacity = capacity
        self.max_speed = max_speed
        self.fuel = fuel

    def calculate_fare(self):
        return self.capacity * 100

    def info(self):
        return f"Passengers: {self.capacity}, Max Speed: {self.max_speed}, Fuel Type: {self.fuel}"


class Bus(Transport, Maintenance):
    def __init__(self, capacity, max_speed, fuel, route, maitenance_cost):
        self.route = route
        Transport.__init__(self, capacity, max_speed, fuel)
        Maintenance.__init__(self, maitenance_cost)

    def calculate_fare(self):
        base_fare = super().calculate_fare()
        return base_fare * 1.1

    def route_info(self):
        return f"Bus operates on route: {self.route}"


class Taxi(Transport, Maintenance):
    def __init__(self, capacity, max_speed, fuel, rate_per_km, maitenance_cost):
        Transport.__init__(self, capacity, max_speed, fuel)
        Maintenance.__init__(self, maitenance_cost)

        self.rate_per_km = rate_per_km

    def trip_cost(self, distance):
        return self.rate_per_km * distance


class Train(Transport, Maintenance):
    def __init__(self, capacity, max_speed, fuel, seats, maitenance_cost):
        Transport.__init__(self, capacity, max_speed, fuel)
        Maintenance.__init__(self, maitenance_cost)

        self.seats = seats

    def train_info(self):
        return f"Train has {self.seats} seats available."


bus = Bus(50, 80, "Diesel", "Route 10", 500)
taxi = Taxi(4, 120, "Petrol", 2, 200)
train = Train(400, 150, "Electric", 10, 3000)

print(bus.info())
print(bus.calculate_fare())
print(bus.route_info())
print(bus.calculate_maintenance())

print(taxi.info())
print(taxi.trip_cost(10))
print(taxi.calculate_maintenance())

print(train.info())
print(train.train_info())
print(train.calculate_maintenance())
