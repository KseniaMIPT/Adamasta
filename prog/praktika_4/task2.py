import robot
r = robot.rmap()
r.lm('task2')
def task():
    r.up(1)
    r.pt()
    r.up(1)
    r.rt(1)
    r.pt()
    r.dn(1)
    r.rt(1)
    r.pt()
    r.dn(1)
    r.lt(1)
    r.pt()
    r.rt(2)
for i in range(5):
    task()
