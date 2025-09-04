class Vehicle:
    def start_engine(self):
        return "The vehicle's engine ignites."

class Car(Vehicle):
    def start_engine(self):
        return "The car's engine fires up."

class Bike(Vehicle):
    def start_engine(self):
        return "The bike's engine cranks."


vehicle = Vehicle()
car = Car()
bike = Bike()

print(vehicle.start_engine())
print(car.start_engine())
print(bike.start_engine())

#Quastion 2

import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total

shapes1 =  (Circle(radius=19.21), Rectangle(width=25, height=3), Circle(radius=15))

print("Total area:", total_area(shapes1))

#Quastion 3

class Shape:
    def __init__(self):
        print("Initializing Shape")

    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

if __name__ == "__main__":
    rectangle = Rectangle(width=19, height=21)
    print(f"Area of the rectangle: {rectangle.calculate_area()}")

    #Quastion 4

    class Dog:
        @staticmethod
        def make_sound():
            return "Woof!"

    class Cat:
        @staticmethod
        def make_sound():
            return "Meow!"

    def process_sound(sound_object):
        sound = sound_object.make_sound()
        print(f"The sound is: {sound}")

    dog = Dog()
    cat = Cat()

    process_sound(dog)
    process_sound(cat)

    #Quastion 5

    from abc import ABC, abstractmethod

    class FileHandler(ABC):
        @abstractmethod
        def read(self):
            """Read data from the file."""
            pass

        @abstractmethod
        def write(self, data):
            """Write data to the file."""
            pass

    class TextFileHandler(FileHandler):
        def __init__(self, filename):
            self.filename = filename

        def read(self):
            with open(self.filename, 'r') as file:
                return file.read()

        def write(self, data):
            with open(self.filename, 'w') as file:
                file.write(data)

    class BinaryFileHandler(FileHandler):
        def __init__(self, filename):
            self.filename = filename

        def read(self):
            with open(self.filename, 'rb') as file:
                return file.read()

        def write(self, data):
            with open(self.filename, 'wb') as file:
                file.write(data)

    if __name__ == "__main__":
        text_handler = TextFileHandler('example.txt')
        text_handler.write("Hello, Brenda!")
        print(text_handler.read())

        binary_handler = BinaryFileHandler('example.bin')
        binary_handler.write(b'\x00\x01\x02\x03')
        print(binary_handler.read())