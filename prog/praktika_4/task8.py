import robot
r = robot.rmap()
r.lm('task8')
r.sleep = 0.05

def test():
    while r.fu():
        r.up()
    while r.fr():
        r.rt()
    a = 0
    while r.fl():
        r.lt()
        a += 1
    def go1():    
        r.dn(1)
        b = 0
        while r.fr():
            r.rt(1)
            b += 1
        if a == b:
            go1()
        else:
            while r.fl():
                r.pt()
                r.lt()
            r.pt()
            c = 0
            while r.fr():
                r.rt()
                c += 1
            if c == a:
                while r.fl():
                    r.lt()
                r.dn(1)
            else:
                r.pt()
                while r.fl():
                    r.lt(1)
            r.dn(1)
    go1()
r.start(test)
            
