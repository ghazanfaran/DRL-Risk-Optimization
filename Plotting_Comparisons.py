import numpy as np
import matplotlib.pyplot as plt

# Load the text file
data = np.loadtxt('Comparison.txt', delimiter='\t')

# Extract the columns for each distribution
distribution1 = data[:, 0]
distribution2 = data[:, 1]
distribution3 = data[:, 2]

# Create a figure and subplots
fig, ax = plt.subplots()

# Plot the histograms for each distribution
ax.hist(distribution1, density=True, bins=20, alpha=0.5,  edgecolor='black',linewidth=0.5, label='Not optimized')
ax.hist(distribution2, density=True, bins=20, alpha=0.5,  edgecolor='black',linewidth=0.5,  color='orange', label='Randomly optimized')
ax.hist(distribution3, density=True, bins=8, alpha=0.5,  edgecolor='black',linewidth=0.5,  color='green', label='Optimized')

# Set labels and title
ax.set_xlabel('Retrofit Costs', fontname='Times New Roman', fontsize=12)
ax.set_ylabel('Density', fontname='Times New Roman', fontsize=12)
ax.set_title('Multiple Distributions', fontname='Times New Roman', fontsize=12)

# Remove tick marks
ax.tick_params(axis='both', which='both', bottom=False, top=False, left=False, right=False)

# Add a legend
ax.legend()

# Adjust spacing
fig.tight_layout()

# Save the plot to a file
#output_path = r'E:\2-Journals\DRL\2-Analysis\ResultMaps\ZOutput.png'
output_path = r'E:\2-Journals\14-DRL\2-Analysis\ResultMaps2\ZOutput.svg'
plt.savefig(output_path, dpi=300)

# Display the plot
plt.show()


