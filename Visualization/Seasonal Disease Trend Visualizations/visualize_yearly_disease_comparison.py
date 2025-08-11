import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('csv_files/yearly_disease_comparison.csv')

# Plot
plt.figure(figsize=(10, 6))
for disease in df.columns[1:]:
    plt.plot(df['Year'], df[disease], marker='o', label=disease)

plt.title('Yearly Disease Comparison')
plt.xlabel('Year')
plt.ylabel('Number of Cases')
plt.legend()
plt.tight_layout()
plt.savefig('yearly_disease_comparison.png')
plt.close()

print('Saved: yearly_disease_comparison.png')
