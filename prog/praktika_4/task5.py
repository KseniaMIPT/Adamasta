import robot
r = robot.rmap()
r.lm('task5')
r.sleep = 0.02
def test():
    def pt():
        def pt1():
            r.pt('red')
            r.dn(3)
            r.pt('red')
            r.dn(3)
            r.pt('red')
        pt1()
        r.rt(1)
        r.up(5)
        pt1()
        r.rt(1)
        r.up(7)
        pt1()
    def go():
        r.up(6)
        r.rt(2)
    for i in range(3):
        pt()
        go()
    pt()
r.start(test)
