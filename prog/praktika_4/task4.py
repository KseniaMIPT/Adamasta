import robot
r = robot.rmap()
r.lm('task4')
r.sleep = 0.02
def test():
	def task1():
	    r.lt(1)
	    r.pt('red')
	    r.dn()
	def task2():
	    r.pt('red')
	    r.rt()
	    r.up()
	while r.fu():
	    r.up()
	while r.fr():
	    r.rt()
	r.dn(1)
	for i in range(5):
	    task1()
	r.dn(1)
	for i in range(5):
	    task2()
	r.rt(1)
	r.dn(3)
	for i in range(5):
	    task1()

r.start(test) 
