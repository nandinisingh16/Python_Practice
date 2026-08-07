# ==============================
# OBJECT ORIENTED PROGRAMMING IN PYTHON
# Demonstrates:
# 1. Class & Object
# 2. Constructor
# 3. Inheritance
# 4. Multilevel Inheritance
# 5. Multiple Inheritance
# 6. super()
# 7. Polymorphism
# 8. Method Overriding
# 9. Duck Typing
# 10. Class Method
# 11. Static Method
# ==============================


# ------------------------------
# Parent Class
# ------------------------------
class Vehicle:

    # Class Variable
    total_vehicles = 0

    # Constructor
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        Vehicle.total_vehicles += 1

    def start(self):
        print(f"{self.brand} vehicle is starting...")

    def info(self):
        print(f"Brand : {self.brand}")
        print(f"Year  : {self.year}")

    # Class Method
    @classmethod
    def showTotalVehicles(cls):
        print(f"Total Vehicles Created : {cls.total_vehicles}")

    # Static Method
    @staticmethod
    def fuelInfo():
        print("Vehicles can use Petrol, Diesel, Electric or CNG.")


# ------------------------------
# Single Inheritance
# ------------------------------
class Car(Vehicle):

    def __init__(self, brand, year, color):
        super().__init__(brand, year)
        self.color = color

    # Method Overriding
    def start(self):
        print(f"{self.brand} car starts with a key.")

    def show(self):
        print(f"Color : {self.color}")


# ------------------------------
# Multilevel Inheritance
# ------------------------------
class ElectricCar(Car):

    def __init__(self, brand, year, color, battery):
        super().__init__(brand, year, color)
        self.battery = battery

    def batteryInfo(self):
        print(f"Battery Capacity : {self.battery} kWh")


# ------------------------------
# Another Parent Class
# ------------------------------
class MusicSystem:

    def playMusic(self):
        print("Music is playing...")


# ------------------------------
# Multiple Inheritance
# ------------------------------
class SmartCar(Car, MusicSystem):

    def autoPilot(self):
        print("Auto Pilot Enabled")


# ------------------------------
# Polymorphism
# ------------------------------
class Bike:

    def start(self):
        print("Bike starts using self-start.")


class Truck:

    def start(self):
        print("Truck starts with a heavy engine.")


# ------------------------------
# Duck Typing
# ------------------------------
class Dog:

    def speak(self):
        print("Dog says: Woof Woof")


class Cat:

    def speak(self):
        print("Cat says: Meow")


def animalSound(animal):
    animal.speak()


# ------------------------------
# Main Program
# ------------------------------

print("===== CLASS & OBJECT =====")

car1 = Car("BMW", 2024, "Blue")
car1.info()
car1.show()
car1.start()

print("\n===== MULTILEVEL INHERITANCE =====")

tesla = ElectricCar("Tesla", 2025, "White", 75)
tesla.info()
tesla.show()
tesla.batteryInfo()

print("\n===== MULTIPLE INHERITANCE =====")

smart = SmartCar("Mercedes", 2025, "Black")
smart.info()
smart.show()
smart.playMusic()
smart.autoPilot()

print("\n===== POLYMORPHISM =====")

vehicles = [
    Car("Audi", 2023, "Red"),
    Bike(),
    Truck()
]

for v in vehicles:
    v.start()

print("\n===== DUCK TYPING =====")

dog = Dog()
cat = Cat()

animalSound(dog)
animalSound(cat)

print("\n===== CLASS METHOD =====")

Vehicle.showTotalVehicles()

print("\n===== STATIC METHOD =====")

Vehicle.fuelInfo()