# This is a sample Python script.

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

a = 1
d = 0.1
b = 0.1
x0 = 4.
y0 = 2.

def derivative(X, t, a, d, b):
    x, y = X
    dotx = x * (1 - x) - a * x * y / (d + x)
    doty = b * y * (1 - y / x)
    return np.array([dotx, doty])


if __name__ == '__main__':
    Nt = 1000
    tmax = 30.
    t = np.linspace(0., tmax, Nt)
    X0 = [x0, y0]
    res = integrate.odeint(derivative, X0, t, args=(a, d, b))
    x, y = res.T

    plt.figure()
    plt.grid()
    plt.title("odeint method")
    plt.plot(t, x, 'xb', label='Deer')
    plt.plot(t, y, '+r', label="Wolves")
    plt.xlabel('Time t, [days]')
    plt.ylabel('Population')
    plt.legend()

    plt.show()



