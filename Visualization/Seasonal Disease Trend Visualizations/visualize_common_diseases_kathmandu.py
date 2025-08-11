import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('csv_files/common_diseases_kathmandu.csv')

# Plot bar chart
plt.figure(figsize=(8, 5))
plt.bar(df['Disease'], df['Number of Cases'], color='mediumslateblue')
plt.xlabel('Disease')
plt.ylabel('Number of Cases')
plt.title('Common Diseases in Kathmandu')
plt.tight_layout()
plt.savefig('common_diseases_kathmandu.png')
plt.close()

print('Saved: common_diseases_kathmandu.png')
