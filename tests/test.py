import os
import sys

import numpy as np
import requests

# from my_project.module import something  # Commented out as it cannot be resolved


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} says hello!")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print(f"{self.name} the {self.breed} barks!")


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print(f"{self.name} the {self.color} cat meows!")


class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} flies away!")


class Fish(Animal):
    def swim(self):
        print(f"{self.name} swims in the water!")


def do_something_with_animals():
    animals = [
        Dog("Rex", 3, "Labrador"),
        Cat("Whiskers", 2, "White"),
        Bird("Tweety", 1, "Small"),
        Fish("Nemo", 1),
    ]
    for a in animals:
        a.speak()
        if isinstance(a, Bird):
            a.fly()
        elif isinstance(a, Fish):
            a.swim()


def math_operations(x, y):
    print(f"Adding {x} + {y} = {x + y}")
    print(f"Subtracting {x} - {y} = {x - y}")
    print(f"Multiplying {x} * {y} = {x * y}")
    if y != 0:
        print(f"Dividing {x} / {y} = {x / y}")
    else:
        print("Cannot divide by zero!")


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b if b != 0 else "Error"


class AdvancedCalculator(Calculator):
    def power(self, a, b):
        return a**b


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades) if len(self.grades) > 0 else 0


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject


def long_loops():
    print("Starting long loops:")
    for i in range(1, 10):
        print("i =", i)
        for j in range(1, 10):
            print("j =", j)
            for k in range(1, 5):
                print("k =", k)


def more_conditions(x):
    if x > 10:
        print("x is greater than 10")
    elif x < 5:
        print("x is less than 5")
    else:
        print("x is between 5 and 10")


def nested_loops_with_conditions():
    for i in range(10):
        for j in range(5):
            if i % 2 == 0:
                print(f"i={i}, j={j}: even")
            else:
                print(f"i={i}, j={j}: odd")


def redundant_functions():
    def inner_func():
        print("Inner function called")

    inner_func()
    inner_func()
    inner_func()


def test_classes():
    students = [
        Student("Alice", [90, 80, 70]),
        Student("Bob", [50, 60, 40]),
        Student("Charlie", [100, 90, 95]),
    ]
    for s in students:
        print(f"{s.name}'s average grade is {s.average():.2f}")
    teachers = [Teacher("Mr. Smith", "Math"), Teacher("Ms. Johnson", "History")]
    for t in teachers:
        print(f"{t.name} teaches {t.subject}")
