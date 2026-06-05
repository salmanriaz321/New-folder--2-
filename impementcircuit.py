import numpy as np

# Change these to match your circuit values
R1, R2, R3 = 10, 4, 5
V1, V2 = 12, 9

# Matrix A (Resistor mesh) & Vector B (Voltage sources)
A = np.array([[1, 1, -1], [R1, 0, R3], [0, R2, R3]])
B = np.array([0, V1, V2])

# Solve for currents [I1, I2, I3]
I = np.linalg.solve(A, B)
print(f"Currents (A): I1={I[0]:.2f}, I2={I[1]:.2f}, I3={I[2]:.2f}")

