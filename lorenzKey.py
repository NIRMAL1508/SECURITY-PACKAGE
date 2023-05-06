# Importing the required libraries
import numpy as np
import matplotlib.pyplot as plt

def lorenz_key(xinit, yinit, zinit, num_steps):

    # Initializing dt to a small value
    dt = 0.01

    # Initializing 3 empty lists
    xs = np.empty(num_steps + 1)
    ys = np.empty(num_steps + 1)
    zs = np.empty(num_steps + 1)

    # Initializing initial values
    xs[0], ys[0], zs[0] = (xinit, yinit, zinit)

    # Initializing constants
    s = 10
    r = 28
    b = 2.667
    for i in range(num_steps):
        xs[i + 1] = xs[i] + (s * (ys[i] - xs[i]) * dt)
        ys[i + 1] = ys[i] + ((xs[i] * (r - zs[i]) - ys[i]) * dt)
        zs[i + 1] = zs[i] + ((xs[i] * ys[i] - b * zs[i]) * dt)


    return xs, ys, zs


