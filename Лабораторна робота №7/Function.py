from numpy import *
import matplotlib.pyplot as plt
def f(t):
    return t== 5*sin(10*t)*sin(3*t)
t=linspace(0, 8, 20)
y=f(t)
 
plt.plot(t,y)
plt.show()