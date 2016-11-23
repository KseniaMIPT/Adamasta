def check():
    for i in range(5):
        yield i+1
print(check())
for i in check():
    print(i)
