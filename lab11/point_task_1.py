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

#a = Point(str('4,5'))
#b = Point(str('1,2'))
#c = Point(str('2,1,1,2,2'))
#print(c)
#print(a.__str__())
#print(a.__add__(b))

max = Point(str('0,0'))
N = int(input())
for i in range(N):
    a = Point(str(input()))
    if (a.x**2 + a.y**2)**(1/2) > (max.x**2 + max.y**2)**(1/2):
        max = a
print(max)