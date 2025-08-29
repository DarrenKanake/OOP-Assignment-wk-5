# # Assignment 1 : Polymorphism  Challenge
# Author : Kanake Darren Rene

# Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️

# Step 1: Define the base class
# 1.Create a class representing vehicles.
class Vehicle:
    # Inside it, define a method called move()
    def move(self):
        print("The vehicle is moving")

# Step 2: Create classes that inherit from the base class
# 2.Create a class representing cars that inherits from Vehicle.
class Car(Vehicle):
    # Inside Car, define its own move() method that prints "Driving "
    def move(self):
        print("Driving")

# 3.Create a class representing planes that inherits from Vehicle.
class Plane(Vehicle):
    # Inside Plane, define its own move() method that prints "Flying "
    def move(self):
        print("Flying")

# Step 3: Demonstrate polymorphism
# 4.Make a list of different objects (Car, Plane).
vehicles = [Car(), Plane()]
# 5.Loop through the list and call the move() method on each object.
for vehicle in vehicles:
    vehicle.move()
# This code defines a base class Vehicle with a method move(), and two subclasses Car and Plane that override the move() method to provide specific implementations. 
# It demonstrates polymorphism by calling the move() method on different objects in a list, resulting in different outputs based on the object's class.
# End of Activity 2