import numpy as np
import pandas as pd
from scipy.optimize import differential_evolution


# Load the given data


data = pd.read_csv("xy_data.csv")

x = data["x"].to_numpy()
y = data["y"].to_numpy()


# Transform the coordinates


def calculate_residuals(params):

    theta, M, X = params

    c = np.cos(theta)
    s = np.sin(theta)

    # Recover t from the rotated coordinate system
    t = (x - X) * c + (y - 42) * s

    # Perpendicular coordinate
    v = -(x - X) * s + (y - 42) * c

    # Expected value from the parametric equation
    expected_v = np.exp(M * t) * np.sin(0.3 * t)

    return v - expected_v

# Objective function


def objective(params):

    theta, M, X = params

    c = np.cos(theta)
    s = np.sin(theta)

    # Recover t
    t = (x - X) * c + (y - 42) * s

    # Penalize t values outside the required range
    penalty = np.sum(
        np.maximum(6 - t, 0) ** 2 +
        np.maximum(t - 60, 0) ** 2
    ) * 100

    error = np.mean(np.abs(calculate_residuals(params)))

    return error + penalty


# Parameter bounds from the assignment


bounds = [
    (0, np.deg2rad(50)),   # theta: 0 to 50 degrees
    (-0.05, 0.05),         # M
    (0, 100)               # X
]


# Numerical optimization


result = differential_evolution(
    objective,
    bounds,
    seed=42,
    maxiter=2000,
    tol=1e-10,
    polish=True
)



# Final parameters


theta, M, X = result.x

print("Estimated parameters")
print("--------------------")
print(f"Theta = {np.rad2deg(theta):.6f} degrees")
print(f"M     = {M:.6f}")
print(f"X     = {X:.6f}")
print(f"Error = {result.fun:.10f}")
