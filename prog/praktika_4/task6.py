import robot
r = robot.rmap()
r.lm('task6')

x = int(input())
y = int(input())

def test():
    def go1():
        r.rt(1)
        r.pt()
    for i in range(x):
        go1()
    r.dn(1)
    r.lt(x // 2)
    def go2():
        r.pt()
        r.dn(1)
    for i in range(y - 1):
        go2()

r.start(test)
