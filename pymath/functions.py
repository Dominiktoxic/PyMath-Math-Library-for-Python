import sys
import math
import random

PI = 3.14159265359

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def addArray(nums, number):
    return [num + number for num in nums]

def subtractArray(nums, number):
    return [num - number for num in nums]

def multiplyArray(nums, number):
    return [num * number for num in nums]

def divideArray(nums, number):
    return [num / number for num in nums]

def factors(x):
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    return factors

def is_prime(x):
    return True if len(factors(x)) <= 2 else False

def exp(x, y):
    return x**y

def sqrt(x):
    return x ** 0.5

def ceil(x):
    if isinstance(x, int):
        return x
    
    y = int(x)
    return y + 1 if x > y else y

def percent(value, percentage):
    return value * percentage / 100

def avg(nums):
    if not nums:
        raise ValueError("Cannot find the average of an empty list.")
    
    return sum(nums) / len(nums)

def is_int(num):
    return True if isinstance(num, int) else False

def bytesize(var):
    return sys.getsizeof(var)

def curt(num):
    return num ** (1 / 3)

def delta(x, y):
    return abs(x - y)

def deltaArray(nums):
    numbers = [num for num in nums]
    return delta(max(numbers), min(numbers))

def root(num, root):
    return num ** (1 / root)

def mod(x, y):
    return x % y

def factorial(num):
    result = 1

    for i in range(1, num + 1):
        result *= i

    return result

def log(base, x):
    result = 0

    if x <= 0 or base <= 0 or base == 1:
        raise ValueError("Base and x must be positive and base must not be 1.")

    while x >= base:
        x /= base
        result += 1

    return result

def gcf(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return abs(x * y) // gcf(x, y)

def is_nan(num):
    return False if not isinstance(num, bool) or isinstance(num, int) and isinstance(num, float) else True

def hypot(a, b):
    return sqrt(a * a + b * b)

def circleArea(radius):
    return PI * (radius * radius)

def cos(angle):
    return math.cos(math.radians(angle))

def sin(angle):
    return math.sin(math.radians(angle))

def tan(angle):
    return math.tan(math.radians(angle))

def acos(adjacent, hypotenuse):
    return math.acos(adjacent / hypotenuse)

def asin(opposite, hypotenuse):
    return math.asin(opposite / hypotenuse)

def atan(opposite, adjacent):
    return math.atan(opposite / adjacent)

def degrees(radians):
    return math.degrees(radians)

def radians(degrees):
    return math.radians(degrees)

def randint(x, y):
    return random.randint(x, y)

def randArray(x, y, length):
    return [randint(x, y) for num in range(length)]

class Shape:
    def __init__(self):
        pass
    
    def area(self):
        pass

    def perimeter(self):
        pass

    def volume(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return (self.length * 2) + (self.width * 2)

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length * self.length
    
    def perimeter(self):
        return self.length * 4

class Cuboid(Shape):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
    
    def volume(self):
        return self.length * self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height, equilateral=False):
        self.base = base
        self.height = height
        self.equilateral = equilateral
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        return self.base * 3 if self.equilateral else self.base + 2 * self.calculate_side()

    def calculate_side(self):
        return sqrt((self.base / 2) ** 2 + self.height ** 2)

def sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums