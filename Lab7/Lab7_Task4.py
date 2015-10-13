import numpy as np
import pylab
from matplotlib import mlab

tlist= mlab.frange (-2*np.pi,2*np.pi, 0.1)

pylab.ion()

for a in range (100):
        ylist = [np.cos(2*t) for t in tlist]
        xlist = [np.sin (t + a*0.1) for t in tlist]
        pylab.clf()
        pylab.plot (xlist,ylist)
        pylab.plot ()
        pylab.draw()

pylab.close()
