import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('csv_files/fulfilled_percentage_by_district.csv')

# Sort by Fulfilled %
df_sorted = df.sort_values('Fulfilled %', ascending=False)

# Plot
plt.figure(figsize=(14, 7))
plt.bar(df_sorted['District'], df_sorted['Fulfilled %'], color='teal')
plt.xticks(rotation=90)
plt.ylabel('Fulfilled Percentage')
plt.title('Fulfilled Percentage by District')
plt.tight_layout()
plt.savefig('fulfilled_percentage_by_district.png')
plt.close()

print('Saved: fulfilled_percentage_by_district.png')
