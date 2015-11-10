class Point:
    def __init__(self, line):
        self.x, self.y = [float(x) for x in line.split(',')]
    def __add__(self, other): #сумма векторов
        S_new = str(self.x + other.x) + ',' + str(self.y + other.y)
        return Point(S_new)
    def __sub__(self, other): #разность векторов
        S_new = str(self.x - other.x) + ',' + str( self.y - other.y)
        return Point(S_new)
    def __mul__(self, other): #скалярное умножение
        return float(self.x * other.x +self.y * other.y)
    def __rmul__(self, a): #умножение на число
        S_new = str(self.x * a) + ',' + str(self.y * a)
        return Point(S_new)
    def __str__(self):
        return str(self.x) + ',' +  str(self.y)
    def mass(self, other):
        S_new = str((self.x + other.x)/2) + ',' + str((self.y + other.y)/2)
        return Point(S_new)
N = int(input())
a = Point(str(input()))
for i in range(N-1):
    b = Point(str(input()))
    a = a.mass(b)
print(a)
