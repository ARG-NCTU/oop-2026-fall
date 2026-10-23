class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2)**0.5

    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return False
        return (self.x == other.x) and (self.y == other.y)

    def __add__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError("Operand must be a Vector2D instance")
        newx = self.x + other.x
        newy = self.y + other.y
        return Vector2D(newx, newy)

def main():
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)

    print(v1)             # 輸出: (3, 4)
    print(v1.magnitude()) # 輸出: 5.0

    v3 = v1 + v2
    print(v3)             # 輸出: (4, 6)
    print(v3 == Vector2D(4, 6)) # 輸出: True

if __name__ == "__main__":
    main()