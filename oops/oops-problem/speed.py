class Vehicle:
    
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):
        print(f'The seating capacity of a {self.name} is {capacity} passengers') 

class Bus(Vehicle):
    def __init__(self):
        super().__init__("School Volvo", 180, 12)

School_bus = Bus()
print(f"Vehicle Name: {School_bus.name}, Speed:{School_bus.max_speed}, Mileage: {School_bus.mileage}")
School_bus.seating_capacity(50)

# modelX = Vehicle(240, 18)
# print(modelX.max_speed, modelX.mileage)