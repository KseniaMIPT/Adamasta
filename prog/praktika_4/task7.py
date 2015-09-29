import robot
r = robot.rmap()
r.lm('task7')
r.sleep = 0.02
def test():
    while r.fu() or r.fl() == 0:
        while r.fr():
            r.lt()
        while r.fu():
            r.up()
    r.dn(1)
    a = 0
    while r.fu() or r.fd():
        while r.fr():
            r.rt()
        r.dn(1)
        a += 1
        while r.fl():
            r.lt()
        r.dn(1)
        a += 1
    while r.fu() and r.fd():
        r.pt()
        if a % 2 == 0:
            r.rt(1)
        else:
            r.lt(1)

r.start(test)
        
        
