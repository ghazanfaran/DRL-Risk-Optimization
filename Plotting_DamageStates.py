import numpy as np
import matplotlib.pyplot as plt

# Load the text file
data = np.loadtxt('Episodes_0.33_L.txt', delimiter='\t')

# Extract the columns for each distribution
distribution1 = data[:, 1]
distribution2 = data[:, 2]
distribution3 = data[:, 3]
distribution4 = data[:, 4]
distribution5 = data[:, 5]

# Create a figure and subplots
fig, ax = plt.subplots()

# Plot the histograms for each distribution
ax.hist(distribution1, density=True, bins=20, alpha=0.5,  edgecolor='black',linewidth=0.5, label='DS0')
ax.hist(distribution2, density=True, bins=20, alpha=0.5,  edgecolor='black',linewidth=0.5, label='DS1')
ax.hist(distribution3, density=True, bins=30, alpha=0.5,  edgecolor='black',linewidth=0.5, label='DS2')
ax.hist(distribution4, density=True, bins=20, alpha=0.5,  edgecolor='black',linewidth=0.5, label='DS3')
ax.hist(distribution5, density=True, bins=10, alpha=0.5,  edgecolor='black',linewidth=0.5, label='DS4')

# Set labels and title
ax.set_xlabel('Buildings', fontname='Times New Roman', fontsize=12)
ax.set_ylabel('Density', fontname='Times New Roman', fontsize=12)
ax.set_title('Damage states', fontname='Times New Roman', fontsize=12)

# Remove tick marks
ax.tick_params(axis='both', which='both', bottom=False, top=False, left=False, right=False)

# Add a legend
ax.legend()

# Adjust spacing
fig.tight_layout()

# Save the plot to a file
output_path = r'E:\2-Journals\14-DRL\2-Analysis\ResultMaps2\L_ZDamageStates.svg'
plt.savefig(output_path, dpi=600)

# Display the plot
plt.show()


