class Vector2D(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return (self.x**2 + self.y**2)**0.5

    def distance_to(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"

    def __add__(self, other):
        return Vector2D(
            self.x + other.x,
            self.y + other.y
        )


# Example 1: magnitude
v = Vector2D(3, 4)
print(v.magnitude())
# 5.0


# Example 2: distance
a = Vector2D(1, 2)
b = Vector2D(4, 6)

print(a.distance_to(b))
# 5.0


# Example 3: addition
a = Vector2D(1, 2)
b = Vector2D(3, 4)

c = a + b

print(c)
# <4,6>


# Check that original objects are unchanged
print(a)
# <1,2>

print(b)
# <3,4>


# Edge case
zero = Vector2D(0, 0)

print(zero.magnitude())
# 0.0


# Negative coordinates
p = Vector2D(-1, -2)
q = Vector2D(1, 2)

print(p + q)
# <0,0>