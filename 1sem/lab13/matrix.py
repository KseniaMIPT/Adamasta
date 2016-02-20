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
        if type(m) == list and n is not None:
            raise ValueError()
        if n == None:
            M = m
            self.M = m
            self.m = len(M)
            if self.m != 0: 
                self.n = len(M[0])
            else:
                self.n = 0
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
                M_add[i][j] = self.M[i][j] + other.M[i][j]
        return Matrix(M_add)

    def determinant(self):
        if self.m != self.n:
            raise RuntimeError()
        det = 0
        if self.m == 1:
            return self.M[0][0]
        for i in range(self.n):
            det = det + (-1)**i * Matrix([ self.M[j][:i] + self.M[j][i+1: ] for j in range(1, self.m) ]).determinant() * self.M[0][i] 
        return det

    def __eq__(self, other):
        if self.m != other.m or self.n != other.n:
            raise RuntimeError()
        for i in range(self.m):
            for j in range(self.n):
                if self.M[i][j] != other.M[i][j]:
                    return False
        return True

    def transpose(self):
        M_trans = [[0]*self.m for i in range(self.n)]
        for i in range(self.m):
            for j in range(self.n):
                M_trans[j][i] = self.M[i][j]
        return Matrix(M_trans)
    
    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            M_new = [[0]*self.n for i in range(self.m)]
            for i in range(self.m):
                for j in range(self.n):
                    M_new[i][j] = self.M[i][j] * other
            return Matrix(M_new)
        if type(other) == Matrix:
            if self.n != other.m:
                raise RuntimeError()
        M_new_2 = [[0]*other.n for i in range(self.m)]
        for i in range(self.m):
            for j in range(other.n):
                M_new_2_item = 0
                for k in range(self.n):
                    M_new_2_item += self.get(i, k) * other.get(k, j)
                M_new_2[i][j] = M_new_2_item
        return Matrix(M_new_2)

    def __sub__(self, other):
        if self.m != other.m or self.n != other.n:
            raise ValueError()
        M_sub = [[0]*self.n for i in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                M_sub[i][j] = self.M[i][j] - other.M[i][j]
        return Matrix(M_sub)

    def __truediv__(self, other):
        if type(other) != int:
            if type(other) != float:
                raise ValueError()
        M_new = [[0]*self.n for i in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                M_new[i][j] = self.M[i][j] / other
        return Matrix(M_new)

    def minor(self):
        """для обратной матрицы"""
        if self.m != self.n:
            raise RuntimeError()
        if self.n == 2:
            return(Matrix([[self.M[1][1], self.M[1][0]], [self.M[0][1], self.M[0][0]]]))
        M_new = [[0]*(self.n) for i in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                D = [self.M[k][:j].extend(self.M[k][j+1:]) for k in range(self.m)]
                D = D[:i] + D[i+1:]
                M_new[i][j] = Matrix(D).determinant()
        return(Matrix(M_new))

    def invert(self): #FIX_ME
        if self.m != self.n:
            raise ValueError()
        if self.determinant() == 0:
            raise ValueError()
        return self.minor().transpose() / self.determinant()
