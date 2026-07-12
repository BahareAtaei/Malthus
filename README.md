# Malthus
Food Supply Prediction
# MORE PHYSICS WITH MATLAB BY DAN GREEN
# CHAPTER 1 / MATHEMATICS / 1.2 MALTHUS

---

**Program Summary:**

This program models and compares **two population growth models** for bacteria:

1. **Malthusian (Exponential) Growth:**
   - Equation: `dN/dt = a·N`
   - Assumes unlimited resources
   - Solution: `N(t) = N0·exp(a·t)`
   - Population grows indefinitely (unconstrained)

2. **Logistic Growth (Limited Resources):**
   - Equation: `dN/dt = -b·(N-c)·N/c`
   - Accounts for carrying capacity `c` (maximum population environment can support)
   - Solution: `N(t) = c / (1 + (c/N0 - 1)·exp(-b·t))`
   - Population approaches carrying capacity `c` asymptotically (constrained)

**Parameters (user inputs):**
- `a`: Malthusian growth rate
- `b`: Logistic growth rate
- `c`: Carrying capacity (food-limited maximum population)
- `N0`: Initial population size

**What the program does:**
1. Takes user-defined parameters
2. Computes both growth models analytically (closed-form solutions)
3. Plots both curves on a **semi-logarithmic scale** to clearly show growth patterns
4. Compares unconstrained vs. constrained growth visually

**Key insight:** Shows how limited resources (carrying capacity) prevent exponential growth, causing the population to stabilize at `c` instead of growing indefinitely.

---

**In one sentence:** *A comparative simulation of unconstrained (Malthusian) vs. resource-limited (logistic) bacterial population growth, demonstrating how carrying capacity constrains population size.*
