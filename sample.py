import os
import sys


def greet(name):
    msg = "Hello " + name + ", welcome to the matrix!"
    return msg


def add(a, b):
    return a + b


name = "phase"
print(greet(name))
print(add(40, 2), add(1, 2))

for i in range(3):
    print("Loop", i)

data = {"key": "value", "num": 42, "pi": 3.14}
print(data["key"], data["num"], data["pi"])

if sys.version_info.major >= 3:
    print("Python 3 confirmed")