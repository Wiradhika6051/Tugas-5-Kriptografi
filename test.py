import numpy as np
import matplotlib.pyplot as plt

# Hénon map parameters
a = 1.4
b = 0.3

# Initial condition
x0 = 0

# Number of iterations
max_iterations = 10000

# Threshold for variation detection
variation_threshold = 1e-5
window_size = 2

# Function to detect small variation
def detect_small_variation(values, threshold, window_size):
    if len(values) < window_size:
        return False
    window = values[-window_size:]
    variation = np.std(window)
    return variation < threshold

# Function to iterate Hénon map
def iterate_henon_map(x0, a, b, iterations, variation_threshold, window_size):
    x = x0
    x_values = []
    for i in range(iterations):
        x = 1 - a * x**2 + b * x
        x_values.append(x)
        if detect_small_variation(x_values, variation_threshold, window_size):
            return x_values, True, i
    return x_values, False, iterations

# Loop until the system no longer reaches small variation
all_x_values = []
small_variation_detected = True

while small_variation_detected:
    x_values, small_variation_detected, iteration_count = iterate_henon_map(
        x0, a, b, max_iterations, variation_threshold, window_size
    )
    all_x_values.extend(x_values)
    
    if small_variation_detected:
        print(f"Small variation detected with x0 = {x0:.5f} after {iteration_count} iterations.")
        x0 += 1e-5
        all_x_values.append(None)  # Marker to show a reset in the plot

# Remove None values and separate runs
runs = []
current_run = []
for value in all_x_values:
    if value is None:
        runs.append(current_run)
        current_run = []
    else:
        current_run.append(value)
if current_run:
    runs.append(current_run)
def flatten_extend(matrix):
     flat_list = []
     for row in matrix:
         flat_list.extend(row)
     return flat_list
a = flatten_extend(runs)
print(a)
# for elmt in a:
#     string = str(elmt).split(".")[-1]
    
# Plot the values of x
# plt.figure(figsize=(12, 6))
# for i, run in enumerate(runs):
#     plt.plot(run, marker='o', linestyle='-', markersize=1, label=f'Run {i + 1}')
# plt.title('Hénon Map Iterations with Incremented x0')
# plt.xlabel('Iteration')
# plt.ylabel('x')
# plt.grid(True)
# plt.legend()
# plt.show()
