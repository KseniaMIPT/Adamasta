class Matrix:
    def __init__(self, m, n=None):
        if type(m) != list:
            if type(m) != int:
                raise ValueError()
        if type(n) != int:
            if n != None:
                raise ValueError()
        if type(n) == int and n < 1:
            raise ValueError()
        if type(m) == int and m < 1:
            raise ValueError()
        if n == None:
            M = m
            self.M = m
            self.m = len(M)
            self.n = len(M[0])
        else:
            self.m = m
            self.n = n
            self.M = [[0]*n for i in range(m)]


    def set(self, mm, nn, x):
        self.M[mm][nn] = x

    def get_m(self):
        return self.m
    def get_n(self):
        return self.n
    def get_size(self):
        return self.m, self.n
    def get(self, i, j):
        return self.M[i][j]

    def __add__(self, other):
        if self.m != other.m or self.n != other.n:
            raise ValueError()
        M_add = [[0]*self.n for i in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                M_add[i][j] = self.M[i][j] + self.M[i][j]
        return Matrix(M_add)