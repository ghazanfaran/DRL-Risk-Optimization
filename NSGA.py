import Community as Co
from scipy.optimize import minimize_scalar

# Define the Objective Function
def objective_function(x):
    
    return x**2 + 4*x - 4

# Perform Single-Objective Optimization
result = minimize_scalar(objective_function, bounds=(-10, 10), method='bounded')

# Extract the Optimal Solution and Objective Value
optimal_x = result.x
objective_value = result.fun

print("Optimal Solution: x =", optimal_x)
print("Objective Value:", objective_value)