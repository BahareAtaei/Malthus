"""
dN/dt = a*N
dc/dt = -a*N + b
dN/dt = -b*(N-c)*N/c
"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt

# initial parameters:
a = float(input("Please Enter 'a' Parameter: ")) # Malthus growth rate
b = float(input("Please Enter 'b' Parameter: ")) # Modified equation growth rate
c = float(input("Please Enter 'c' Parameter: ")) # Carrying capacity (limited resources)
N0 = float(input("Please Enter 'N0' Parameter: ")) # Initial population
t = np.linspace(0, 3, 300)

# malthus solution: 
'''
 dN/dt = a*N
 dN/N = a*dt
 ln(N/N0) = a*t
 N = N0 exp(a*t)
 '''
Nm = N0 * np.exp(a*t)

# limited-resources (logistic) solution
# N(t) = c/(1+(c/N0 - 1)*np.exp(-b*t))

Nl = c / (1 + (c / N0 - 1) * np.exp(-b*t))

# ploting
plt.figure(figsize=(15, 8))
plt.semilogy(t, Nm, 'b--', lw=2, label='Malthus')
plt.semilogy(t, Nl, 'r--', lw=2, label='Limited')

plt.xlabel('time')
plt.ylabel('Nm, Nl')
plt.title('Number of Bacteria - Unconstrained and Constrained by Food')
plt.legend(loc='upper right')
plt.grid(alpha=0.5, ls='--')
plt.tight_layout()
plt.show()
