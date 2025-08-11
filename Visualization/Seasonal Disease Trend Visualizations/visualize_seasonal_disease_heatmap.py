import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('csv_files/seasonal_disease_heatmap.csv')

# If the first column is 'Disease' or similar, set it as index
if df.columns[0].lower() in ['disease', 'season', 'type']:
    df.set_index(df.columns[0], inplace=True)

# Plot heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df, annot=True, fmt='.0f', cmap='YlOrRd')
plt.title('Seasonal Disease Heatmap')
plt.xlabel('Season')
plt.ylabel('Disease')
plt.tight_layout()
plt.savefig('seasonal_disease_heatmap.png')
plt.close()

print('Saved: seasonal_disease_heatmap.png')
