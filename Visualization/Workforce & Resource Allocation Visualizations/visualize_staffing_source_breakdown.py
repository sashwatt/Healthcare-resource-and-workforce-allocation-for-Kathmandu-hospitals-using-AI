import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('csv_files/staffing_source_breakdown_by_district.csv')

# Set District as index for easier plotting
df.set_index('District', inplace=True)

# Plot stacked bar chart
plt.figure(figsize=(18, 8))
df[['Fulfilled (Regular)', 'Contract', 'Local Resource']].plot(
    kind='bar',
    stacked=True,
    color=['#4CAF50', '#FFC107', '#2196F3'],
    width=0.8
)
plt.ylabel('Number of Staff')
plt.title('Staffing Source Breakdown by District')
plt.xticks(rotation=90)
plt.legend(title='Staffing Source')
plt.tight_layout()
plt.savefig('staffing_source_breakdown_by_district.png')
plt.close()

print('Saved: staffing_source_breakdown_by_district.png')
