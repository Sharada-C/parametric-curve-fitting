Parametric Curve Parameter Estimation
1. Objective

The objective of this assignment is to determine the unknown parameters θ, M, and X of a given parametric curve using the provided xy_data.csv dataset.

The parameter constraints given in the assignment are:

0 < θ < 50°
-0.05 < M < 0.05
0 < X < 100
6 < t < 60
2. Given Parametric Equation

The curve is defined by:

x = t*cos(θ) - exp(M|t|)*sin(0.3t)*sin(θ) + X

y = 42 + t*sin(θ) + exp(M|t|)*sin(0.3t)*cos(θ)

The supplied data points are provided in xy_data.csv.

Since the given range is 6 < t < 60, t is positive and therefore:

|t| = t

The equations can therefore be written as:

x = t*cos(θ) - exp(Mt)*sin(0.3t)*sin(θ) + X

y = 42 + t*sin(θ) + exp(Mt)*sin(0.3t)*cos(θ)
3. Mathematical Approach

The parameter estimation was performed by transforming the coordinates into a rotated coordinate system.

Define the first transformed coordinate as:

u = (x - X)*cos(θ) + (y - 42)*sin(θ)

Substituting the parametric equations into this expression gives:

u = t

The perpendicular coordinate is defined as:

v = -(x - X)*sin(θ) + (y - 42)*cos(θ)

Substituting the parametric equations gives:

v = exp(Mt)*sin(0.3t)

Since u = t, this becomes:

v = exp(Mu)*sin(0.3u)

Therefore, the original curve-fitting problem can be transformed into a parameter estimation problem. The values of θ, M, and X are adjusted so that the transformed data follows the relationship:

v = exp(Mu)*sin(0.3u)
4. Numerical Optimization

Python was used to estimate the unknown parameters from the supplied data.

The optimization was performed using:

scipy.optimize.differential_evolution

The search was constrained according to the parameter ranges specified in the assignment:

0 < θ < 50°
-0.05 < M < 0.05
0 < X < 100

For every candidate set of parameters:

The corresponding t values are recovered using the rotated coordinate transformation.
The perpendicular coordinate v is calculated from the data.
The expected value exp(Mt)*sin(0.3t) is calculated.
The difference between the observed and expected values is used to calculate the fitting error.
A penalty is applied when recovered t values fall outside the required range 6 < t < 60.

The implementation is provided in solution.py.

5. Estimated Parameters

The estimated parameters are:

θ = 30°
M = 0.03
X = 55

These values satisfy the parameter ranges specified in the assignment.

6. Final Parametric Curve

Substituting the estimated parameters into the original equations gives:

x = t*cos(30°)
    - exp(0.03t)*sin(0.3t)*sin(30°)
    + 55

y = 42
    + t*sin(30°)
    + exp(0.03t)*sin(0.3t)*cos(30°)

with:

6 < t < 60
7. Repository Contents
solution.py   - Python implementation for parameter estimation
xy_data.csv  - Provided curve data
README.md    - Explanation of the mathematical and numerical approach
8. Result

The final estimated values are:

θ = 30°
M = 0.03
X = 55

These values satisfy the specified parameter constraints and provide a close fit to the supplied curve data.

9. Desmos Visualization

The final parametric curve was also plotted in Desmos using the estimated parameters.

Desmos graph:

[Add the shared Desmos link here]
10. Conclusion

The unknown parameters of the given parametric curve were estimated using a coordinate transformation followed by numerical optimization.

The final estimated parameters are:

θ = 30°
M = 0.03
X = 55

The approach combines mathematical transformation with numerical optimization to recover the parameters from the supplied (x, y) data.
