import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('csv_files/monthly_disease_trend.csv')

# Plot
plt.figure(figsize=(10, 6))
for disease in df.columns[1:]:
    plt.plot(df['Month'], df[disease], marker='o', label=disease)

plt.title('Monthly Disease Trend')
plt.xlabel('Month')
plt.ylabel('Number of Cases')
plt.legend()
plt.tight_layout()
plt.savefig('monthly_disease_trend.png')
plt.close()

print('Saved: monthly_disease_trend.png')
