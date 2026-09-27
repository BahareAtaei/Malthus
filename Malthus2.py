# import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# parameters
a = float(input("Please Enter a: "))
b = float(input("Please Enter b: "))
N0 = float(input("Please Enter N0: "))
c0 = float(input("Please Enter initial Carrying Capacity c0: "))

# time interval
t_start = 0
t_end = 10
t = np.linspace(t_start, t_end, 500)
#--------------------------------------------

# malthus equation
# dN/dt = aN
N_malthus = N0 * np.exp(a * t)
#--------------------------------------

# coupled logistic
# dc/dt = -aN + b
# dN/dt = -b(N-c)N/c

def coupled_malthus(t, y):
    N, c = y
    dNdt = -b * (N - c) * N / c
    dcdt = -a * N + b

    return [dNdt, dcdt]


# initial condition
y0 = [N0, c0]

solution = solve_ivp(
    coupled_malthus,
    [t_start, t_end],
    y0,
    t_eval=t
)

# extract solution
N_coupled = solution.y[0]
c_coupled = solution.y[1]
#------------------------------------

# plot results
plt.figure(figsize=(6, 4))

# plot malthus
plt.plot(
    t,
    N_malthus,
    color='blue',
    label='Malthus'
)

# coupled plot
plt.plot(
    t,
    N_coupled,
    color='red',
    label='Limited'
)

# carrying capacity
plt.plot(
    t,
    c_coupled,
    color='green',
    label='Coupled c(t)'
)

plt.xlabel('t (s)')
plt.ylabel('N / c(t)')
plt.title('Malthusian Growth and Coupled Population-Environment Model')
plt.grid(alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
