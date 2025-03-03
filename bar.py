import matplotlib.pyplot as plt
import numpy as np

# Set Times New Roman as the default font
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Times New Roman'

# Age groups
age_groups = ["0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70+"]

# Population data
female_population = np.array([49, 19, 92, 70, 58, 37, 19, 18])
male_population = np.array([53, 19, 18, 18, 20, 9, 29, 19])

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Bar chart parameters
x = np.arange(len(age_groups))
width = 0.35

# Create bar chart
ax.bar(x - width/2, female_population, width, label='Female', color='purple')
ax.bar(x + width/2, male_population, width, label='Male', color='blue')

# Labels and titles
ax.set_xlabel('Age Group', fontsize=14, fontweight='bold')
ax.set_ylabel('Population Count', fontsize=14, fontweight='bold')
ax.set_title('Population Distribution by Age and Gender', fontsize=20, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(age_groups, fontsize=10, fontweight='bold', rotation=45, ha='right')

# Add value labels on the bars
for i, v in enumerate(female_population):
    ax.text(i - width/2, v + 1, str(v), ha='center', va='bottom', fontsize=9)
for i, v in enumerate(male_population):
    ax.text(i + width/2, v + 1, str(v), ha='center', va='bottom', fontsize=9)

# Legend
ax.legend(fontsize=10, loc='upper left')

# Add N546 to top right
ax.text(0.95, 0.95, '(N=546)', transform=ax.transAxes, fontsize=14, fontweight='bold',
        ha='right', va='top')

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add gridlines
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout and save
plt.tight_layout()
plt.savefig('population_bar_chart.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()
