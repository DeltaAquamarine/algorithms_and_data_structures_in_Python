class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def rectangle_properties(self, other):
        w, h = abs(self.x - other.x), abs(self.y - other.y)
        return 2 * (w + h), w * h

p1, p2 = Point(1, 2), Point(4, 6)
print(p1)  
perimeter, area = p1.rectangle_properties(p2)
print(f'Периметр: {perimeter}, Площадь: {area}')