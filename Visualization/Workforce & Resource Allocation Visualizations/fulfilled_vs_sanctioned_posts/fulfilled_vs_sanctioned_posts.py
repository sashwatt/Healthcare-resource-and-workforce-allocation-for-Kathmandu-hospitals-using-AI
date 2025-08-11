import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('csv_files/fulfilled_vs_sanctioned_posts.csv')

# --- 1. Scatter Plot: Sanctioned vs Fulfilled ---
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x='Sanctioned_Post',
    y='Fulfilled_Post',
    hue='Fulfilled_Percentage',
    palette='viridis',
    s=80
)
plt.plot([df['Sanctioned_Post'].min(), df['Sanctioned_Post'].max()],
         [df['Sanctioned_Post'].min(), df['Sanctioned_Post'].max()],
         'r--', label='Ideal (Fulfilled = Sanctioned)')
plt.title('Sanctioned vs Fulfilled Posts by District')
plt.xlabel('Sanctioned Posts')
plt.ylabel('Fulfilled Posts')
plt.legend(title='Fulfilled %', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('fulfilled_vs_sanctioned_scatter.png')
plt.close()

# --- 2. Bar Chart: Fulfilled % by District ---
df_sorted = df.sort_values('Fulfilled_Percentage', ascending=False)
plt.figure(figsize=(14, 7))
plt.bar(df_sorted['District'], df_sorted['Fulfilled_Percentage'], color='teal')
plt.xticks(rotation=90)
plt.ylabel('Fulfilled Percentage')
plt.title('Fulfilled Percentage by District')
plt.tight_layout()
plt.savefig('fulfilled_percentage_by_district.png')
plt.close()

print('Saved: fulfilled_vs_sanctioned_scatter.png, fulfilled_percentage_by_district.png')
