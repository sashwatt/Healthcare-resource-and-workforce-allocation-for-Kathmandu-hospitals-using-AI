import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

df = pd.read_csv('ai_decision_accountability.csv')

# Create figure
fig, ax = plt.subplots(figsize=(12, 8))
ax.axis('off')

# Define box properties
box_width = 4
box_height = 1.2

# New (x, y) positions spaced better
x_positions = [4, 4, 1, 7, 4]
y_positions = [8, 6, 4, 4, 2]

# Draw boxes and texts
for i, row in df.iterrows():
    x = x_positions[i]
    y = y_positions[i]
    box = FancyBboxPatch((x, y), box_width, box_height,
                         boxstyle="round,pad=0.3", fc="lightblue", ec="black", linewidth=1.5)
    ax.add_patch(box)
    ax.text(x + box_width / 2, y + box_height / 2,
            f"Step {int(row['Step'])}\n{row['Description']}",
            ha='center', va='center', fontsize=11, wrap=True)

# Helper to draw arrow from bottom center of one box to top center of another
def draw_arrow(start_idx, end_idx):
    start_x = x_positions[start_idx] + box_width / 2
    start_y = y_positions[start_idx]
    end_x = x_positions[end_idx] + box_width / 2
    end_y = y_positions[end_idx] + box_height
    arrow = FancyArrowPatch((start_x, start_y), (end_x, end_y),
                            arrowstyle='->', mutation_scale=20, linewidth=1.5)
    ax.add_patch(arrow)

# Draw arrows for flow
draw_arrow(0, 1)  
draw_arrow(1, 2)  
draw_arrow(1, 3)  
draw_arrow(2, 4)  
draw_arrow(3, 4)  

# Set limits and save
ax.set_xlim(0, 12)
ax.set_ylim(1, 10)
plt.tight_layout()
plt.savefig('ai_decision_accountability_flowchart_better.png')
plt.close()

print('Saved: ai_decision_accountability_flowchart_better.png')
