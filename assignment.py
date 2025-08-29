# Assignment 1 : Design your own class
# Author : Kanake Darren Rene

# 1.Create a class representing cats.
class Cat:
    # 3.Used constructors to initialize each object with unique values.
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color  
# 2.Added attributes and methods to bring the class to life!
    def meow(self):
        return f"{self.name} says Meow!"

    def info(self):
        return f"Cat Name: {self.name}, Age: {self.age}, Color: {self.color}"   
    
# 4.Added an inheritance layer to explore polymorphism or encapsulation.
class PersianCat(Cat):
    def __init__(self, name, age, color, fur_length):
        super().__init__(name, age, color)
        self.fur_length = fur_length

    def info(self):
        base_info = super().info()
        return f"{base_info}, Fur Length: {self.fur_length}"
# 5.Created multiple objects to demonstrate the functionality of my class.
cat1 = Cat("Whiskers", 3, "Tabby")
cat2 = PersianCat("Fluffy", 2, "White", "Long")

print(cat1.meow())
print(cat1.info())

print(cat2.meow())
print(cat2.info())
# This code defines a Cat class with attributes and methods, and a PersianCat subclass that extends the Cat class. 
# It demonstrates object-oriented programming concepts such as encapsulation and inheritance.
# Multiple objects of both classes are created to showcase their functionality.
# End of Assignment 1  
    

