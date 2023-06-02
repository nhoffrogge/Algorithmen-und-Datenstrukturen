import numbers
from math import sqrt
from functools import total_ordering

@total_ordering
class Vector2D:
    def __init__(self, x=0.0, y=0.0):
        if isinstance(x,  numbers.Real) and isinstance(y, numbers.Real):
            self.x = x
            self.y = y
        else:
            raise TypeError('You must pass in int/float value for x and y')

    def __call__(self):
        print("Calling the __call__ method")

    def __repr__(self):
        return f'vector.Vector2D({self.x}, {self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __abs__(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __eq__(self, other_vector):
        if isinstance(other_vector, Vector2D):
            raise TypeError('You must pass a Vector2D instance!')
        return self.x == other_vector.x and self.y == other_vector.y

    def __lt__(self, other_vector):
        if not isinstance(other_vector, Vector2D):
            raise TypeError('You must pass a Vector2D instance!')
        return abs(self) < abs(other_vector)

    def __add__(self, other_vector):
        if not isinstance(other_vector, Vector2D):
            raise TypeError('You must pass a Vector2D instance!')
        x = self.x + other_vector.x
        y = self.y + other_vector.y
        return Vector2D(x, y)

    def __sub__(self, other_vector):
        if not isinstance(other_vector, Vector2D):
            raise TypeError('You must pass a Vector2D instance!')
        x = self.x - other_vector.x
        y = self.y - other_vector.y
        return Vector2D(x, y)

    def __mul__(self, other):
        if isinstance(other, Vector2D):
            result = self.x * other.x + self.y * other.y
            return result
        if not isinstance(other, numbers.Real):
            raise TypeError('You must pass in an int/float!')
        return Vector2D(sefl.x * other, self.y * other)

    def __turediv__(self, other):
        if not isinstance(other, numbers.Real):
            raise TypeError('You must pass in an int/float!')
        return Vector2D(sefl.x * other, self.y * other)



v1 = Vector2D(0, 0)
v2 = Vector2D(1, 1)

print(hex(id(v1)))
print(hex(id(v2)))

print(v1 > v2)
print(v1 < v2)
print(v1 - v2)