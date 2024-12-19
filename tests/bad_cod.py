import os
import sys

import numpy as np
import requests
from my_project.module import something


def calculate(x, y, operation="add"):
    if operation == "add":
        return x + y
    elif operation == "multiply":
        return x * y
    elif operation == "divide":
        return x / y
    elif operation == "subtract":
        return x - y
    else:
        print("Unknown operation")
        return None


a, b = 1, 2
do_something(a, b)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []
for n in nums:
    if n % 2 == 0:
        result.append(n * 10)
    else:
        result.append(n - 1)
for i in range(20):
    print("Processing:", i)
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 15 == 0:
        print("FizzBuzz")
    else:
        print("None")




def check_numbers(nums):
    even = []
    odd = []
    for n in nums:
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)
            print("Even numbers:", even)
            print("Odd numbers:", odd)


check_numbers(nums)


def long_loop_function():
    for x in range(50):
        for y in range(10):
        print(x, "*", y, "=", x * y)


long_loop_function()

a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
j = 10
print(a, b, c, d, e, f, g, h, i, j)
def redundant_func1(): pass ; def redundant_func2(): pass; def redundant_func3(): pass
def check_prime(n): if n < 2: return False; for i in range(2, int(n**0.5) + 1): if n % i == 0: return False; return True


primes = [n for n in range(100) if check_prime(n)]
print("Primes:", primes)


def string_operations(s): print(s.upper()); print(s.lower()); print(
    s[::-1]); print(s.replace(" ", "_")); print("Length:", len(s))


string_operations("This is a test string for black formatter")
time.sleep(1)
for x in range(100):
    if x % 10 == 0:
        print("Ten:", x)
        else:
        pass


def calculate_area(l, w): return l * w; def calculate_perimeter(l, w): return 2 * (l + w)


l = 10
w = 20
print("Area:", calculate_area(l, w), "Perimeter:", calculate_perimeter(l, w))
x = [1, 2, 3]
y = [4, 5, 6]
z = x + y
print("Combined list:", z)
def power_func(x, p): return x**p; print(power_func(2, 3))


a = 5
b = 10
print(
    "Sum:",
    a + b,
    "Difference:",
    a - b,
    "Product:",
    a * b,
    "Quotient:",
    a / b)


def another_long_loop(): for i in range(30): for j in range(5): print("Index", i, j)


another_long_loop()

r_list = []
for i in range(20):
    r_list.append(random.randint(1, 100))
print("Random list:", r_list)

while a < 20:
    print(a)
    a += 1
    time.sleep(0.1)


def edge_cases(): print("Edge Case 1"); print(
    "Edge Case 2"); print("Edge Case 3")


edge_cases()
def useless_func(): return None
