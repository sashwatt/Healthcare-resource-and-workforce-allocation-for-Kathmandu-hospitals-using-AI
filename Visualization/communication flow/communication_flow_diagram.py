import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv('communication_flow.csv')


df['Fragmented_Complexity'] = df['Current Communication Flow (Fragmented)'].apply(len)

# Sort descending by complexity (longer text = more complexity/delay assumed)
df_sorted = df.sort_values('Fragmented_Complexity', ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(df_sorted['Department'], df_sorted['Fragmented_Complexity'], color='coral')
plt.xlabel('Department')
plt.ylabel('Communication Complexity (proxy)')
plt.title('Estimated Communication Delays in Fragmented Systems by Department')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('communication_delays_fragmented.png')
plt.close()

print('Saved: communication_delays_fragmented.png')
