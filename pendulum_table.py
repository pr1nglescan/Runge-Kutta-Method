from math import sin, cos
import pandas as pd
import numpy as np

# setting constants
g = 9.8
l = g / np.pi ** 2
omega = np.sqrt(g / l)

# setting initial conditions
h = 0.02  # described as delta t in pset
theta_naught = 0.1
theta_dot_naught = 0

# defining approximation equations
def theta(t):
    s = round(t, 2)
    if s == 0:
        return theta_naught
    elif s == h / 2:
            return h * theta_dot_naught
    else:
        return theta(s - h) + h * theta_dot(s - (h / 2))


def theta_dotdot(t):
    if t == 0:
        return (-g / l) * sin(theta_naught)
    else:
        return (-g / l) * sin(theta(t))


#helper method for theta(t)
def theta_dot(t):
    s = round(t, 2)
    if s == h / 2:
        return 0.5 * h * theta_dotdot(0)
    elif s == 0:
        return theta_dot_naught
    else:
        return theta_dot(s - h) + h * theta_dotdot(s - (h / 2))


#create a table
motion = pd.DataFrame(columns=['theta', 'SHM theta'])
for n in np.arange(0, 0.2, 0.02):
    motion.loc[n, 'theta'] = theta(n)
    motion.loc[n, 'SHM theta'] = theta_naught * cos(omega * n)

print(motion)

