import robot
r = robot.rmap()
r.lm('task3')
r.sleep = 0.02
def task():
    r.rt(2)
    r.dn(1)
    r.up(1)
def test():
    for i in range(3):
        task()
    r.rt(2)
r.start(test)
