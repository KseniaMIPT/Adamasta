class Point:
    def __init__(self, line):
        self.x, self.y = [float(x) for x in line.split(',')]

    def __add__(self, other):
        """сумма векторов"""
        S_new = str(self.x + other.x) + ',' + str(self.y + other.y)
        return Point(S_new)

    def __sub__(self, other):
        """разность векторов"""
        S_new = str(self.x - other.x) + ',' + str(self.y - other.y)
        return Point(S_new)

    def __mul__(self, other):
        """скалярное умножение"""
        return float(self.x * other.x + self.y * other.y)

    def __rmul__(self, a):
        """умножение на число"""
        S_new = str(self.x * a) + ',' + str(self.y * a)
        return Point(S_new)

    def __str__(self):
        return str(self.x) + ',' +  str(self.y)

    def mass(self, other):
        S_new = str((self.x + other.x)/2) + ',' + str((self.y + other.y)/2)
        return Point(S_new)

    def len_point(self):
        """длина вектора"""
        len_point = (self.x ** 2 + self.y ** 2) ** (1/2)
        return len_point

    def triangle_perimeter(self, other, another):
        """периметр"""
        perimeter = float(self.__sub__(other).len_point() + other.__sub__(another).len_point() + another.__sub__(self).len_point())
        return perimeter

N = int(input())
Points = [Point(input()) for i in range(N)]
max_perimeter = 0
for i in range(N - 2):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if Points[i].triangle_perimeter(Points[j], Points[k]) > max_perimeter:
                max_perimeter = Points[i].triangle_perimeter(Points[j], Points[k])
print(max_perimeter)