import numpy as np
import matplotlib.pyplot as plt

# Load the text file
data = np.loadtxt('Comparison.txt', delimiter='\t')

# Extract the columns for each distribution
distribution1 = data[:, 0]
distribution2 = data[:, 1]
distribution3 = data[:, 2]

# Calculate the histogram values and bin edges for distribution1
hist_values1, bin_edges1 = np.histogram(distribution1, bins=100, density=True)
x1 = bin_edges1[:-1]
y1 = np.cumsum(hist_values1 * np.diff(bin_edges1))

# Calculate the histogram values and bin edges for distribution2
hist_values2, bin_edges2 = np.histogram(distribution2, bins=100, density=True)
x2 = bin_edges2[:-1]
y2 = np.cumsum(hist_values2 * np.diff(bin_edges2))

# Calculate the histogram values and bin edges for distribution3
hist_values3, bin_edges3 = np.histogram(distribution3, bins=100, density=True)
x3 = bin_edges3[:-1]
y3 = np.cumsum(hist_values3 * np.diff(bin_edges3))

x=np.column_stack((x1, x2, x3))

# Create a figure and subplots
fig, ax = plt.subplots()

# Plot the extracted x and y values
ax.plot(x1, y1, color='blue', label='Not optimized')
ax.plot(x2, y2, color='green', label='Randomly optimized')
ax.plot(x3, y3, color='red', label='Optimized')

# Set labels and title
ax.set_xlabel('Repair Costs', fontname='Times New Roman', fontsize=12)
ax.set_ylabel('Cumulative Probability', fontname='Times New Roman', fontsize=12)
ax.set_title('CDF - Multiple Distributions', fontname='Times New Roman', fontsize=12)

# Add a legend
ax.legend()

# Save the plot to a file
output_path = r'E:\2-Journals\DRL\2-Analysis\ResultMaps\ZOutput.png'
plt.savefig(output_path, dpi=300)

# Display the plot
plt.show()
