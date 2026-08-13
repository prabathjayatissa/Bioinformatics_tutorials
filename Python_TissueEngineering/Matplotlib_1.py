import matplotlib.pyplot as plt
import numpy as np

# 1. Setup Data for Tissue Engineering Metrics
# Time points in days for a 3-week scaffold culture experiment
days = np.array([0, 3, 7, 14, 21])

# Data set A: Cell proliferation (Normalized DNA Content)
# Simulates exponential growth flattening as scaffold reaches confluence
dna_content = np.array([1.0, 1.8, 4.2, 8.5, 9.8])
dna_error = np.array([0.1, 0.15, 0.4, 0.6, 0.5])

# Data set B: Extracellular Matrix (ECM) Deposition (e.g., GAG or Collagen content in µg)
# Simulates lag phase followed by massive matrix deposition
ecm_deposition = np.array([0.2, 0.5, 2.1, 7.8, 14.5])
ecm_error = np.array([0.05, 0.08, 0.25, 0.8, 1.2])

# 2. Initialize Publication-Quality Figure (Dual-Y Axis Layout)
fig, ax1 = plt.subplots(figsize=(7, 5), dpi=300)

# Configure primary font properties for clarity and scannability
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 11

# 3. Plot Primary Axis: Cell Proliferation
color_dna = '#1f77b4'  # Deep Blue
ax1.set_xlabel('Culture Time (Days)', fontweight='bold', labelpad=10)
ax1.set_ylabel('Normalized DNA Content (Fold Change)', color=color_dna, fontweight='bold')

# Plot line with error bars and prominent markers
line1 = ax1.errorbar(days, dna_content, yerr=dna_error, fmt='-o', color=color_dna,
                     linewidth=2, markersize=8, capsize=5, elinewidth=1.5,
                     label='Cell Proliferation (DNA)')
ax1.tick_params(axis='y', labelcolor=color_dna)
ax1.set_ylim(0, 12)

# 4. Plot Secondary Axis: Matrix Deposition
# Create a twin axis sharing the same x-axis for direct comparison
ax2 = ax1.twinx()
color_ecm = '#d62728'  # Deep Red
ax2.set_ylabel('ECM Deposition ($\mu$g / Scaffold)', color=color_ecm, fontweight='bold')

# Plot secondary line with error bars and contrasting markers
line2 = ax2.errorbar(days, ecm_deposition, yerr=ecm_error, fmt='-s', color=color_ecm,
                     linewidth=2, markersize=8, capsize=5, elinewidth=1.5,
                     label='Matrix Deposition (ECM)')
ax2.tick_params(axis='y', labelcolor=color_ecm)
ax2.set_ylim(0, 18)

# 5. Visual Formatting & Polish
# Add light gridlines focused on the primary time intervals
ax1.grid(True, linestyle='--', alpha=0.5, which='both')

# Explicitly define X-axis ticks to match experimental timepoints
ax1.set_xticks(days)

# Combine legends from both axes into a single anchor box
lines = [line1[0], line2[0]]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', frameon=True, facecolor='white', edgecolor='none')

# Add descriptive title detailing key tissue milestones
plt.title('In Vitro Tissue Development Dynamics', fontsize=14, fontweight='bold', pad=15)

# Adjust layout automatically to prevent label clipping
plt.tight_layout()

# 6. Output and Display
# To save as a publication-ready vector graphic, uncomment the line below:
# plt.savefig('tissue_engineering_growth_plot.svg', format='svg', bbox_inches='tight')
plt.show()
