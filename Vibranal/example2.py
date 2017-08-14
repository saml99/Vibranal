import matplotlib.pyplot as plt
import numpy as np

t1 = np.arange(0.0, 10.0, 0.1)
m = 20.0
b = 10.0
k = 1.0
w = np.sqrt((b**2)-4*m*k)/(2*m)
x0 = 1.0

if b**2 == 4*m*k:
    plt.plot(t1, x0*np.exp(-(b*t1)/(2*m))+ b*x0/(2*m)*t1*np.exp(-(b*t1)/(2*m)))
elif b**2 < 4*m*k:
    plt.plot(t1, x0*np.exp(-(b*t1)/(2*m))*np.cos(w*t1))
elif b**2 > 4*m*k:
    plt.plot(t1, (x0*(b/(4*m*w)+0.5)*np.exp((-(b/(2*m))+w)*t1)+(x0*(0.5-(b/(4*m*w)*np.exp((-(b/(2*m))-w)*t1))))))


plt.show()
