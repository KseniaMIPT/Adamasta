class Add():
    def __init__(self):
        self.val = 1
    def __addc__(self, other):
        return self.val + other.val
a = Add()
b = Add()
print(a + b)
