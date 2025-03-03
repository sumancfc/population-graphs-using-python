import matplotlib.pyplot as plt
import numpy as np

# Set Times New Roman as the default font
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Times New Roman'

# Age groups (reversed so 0-9 starts at the bottom)
age_groups = ["0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70+"][::-1]

# Population data (reversed)
female_population = np.array([49, 19, 92, 70, 58, 37, 19, 18])[::-1]
male_population = np.array([53, 19, 18, 18, 20, 9, 29, 19])[::-1]

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Bar chart parameters
y_pos = np.arange(len(age_groups))
bar_width = 0.8

# Create horizontal bar chart for population pyramid with different color for female
ax.barh(y_pos, -female_population, color="purple", label="Female", height=bar_width)
ax.barh(y_pos, male_population, color="blue", label="Male", height=bar_width)

# Labels and titles
ax.set_yticks(y_pos)
ax.set_yticklabels(age_groups, fontsize=10, fontweight='bold')
ax.set_xlabel("Population Count", fontsize=14, fontweight='bold')
ax.set_ylabel("Age Group", fontsize=14, fontweight='bold')
ax.set_title("Population Pyramid", fontsize=40, fontweight='bold')

# Add N546 to top right
ax.text(0.95, 1.00, '(N=546)', transform=ax.transAxes, fontsize=14, fontweight='bold',
        ha='right', va='top')

# Ensure x-axis starts from 0 and increases in steps of 10
max_population = max(max(female_population), max(male_population))
max_x = ((max_population // 10) + 1) * 10  # Round up to nearest 10
ax.set_xticks(np.arange(-max_x, max_x + 10, 10))
ax.set_xlim(-max_x, max_x)
ax.set_xticklabels([str(abs(i)) for i in ax.get_xticks()], fontsize=10, fontweight='bold')

# Add vertical line at x=0
ax.axvline(x=0, color='gray', linestyle='-', linewidth=0.5)

# Add value labels on the bars
for i, v in enumerate(female_population):
    ax.text(-v - 2, i, str(v), va='center', ha='right', fontsize=9)
for i, v in enumerate(male_population):
    ax.text(v + 2, i, str(v), va='center', ha='left', fontsize=9)

# Keep age groups in bottom-to-top order
plt.gca().invert_yaxis()

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add "Male" and "Female" labels at the top
ax.text(0.20, 0.75, 'Female', transform=ax.transAxes, fontsize=24, color='purple',
        ha='left', va='bottom', fontweight='bold')
ax.text(0.80, 0.75, 'Male', transform=ax.transAxes, fontsize=24, color='blue',
        ha='right', va='bottom', fontweight='bold')

# Save the plot as a PNG file
plt.tight_layout()
plt.savefig('population_pyramid.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()
