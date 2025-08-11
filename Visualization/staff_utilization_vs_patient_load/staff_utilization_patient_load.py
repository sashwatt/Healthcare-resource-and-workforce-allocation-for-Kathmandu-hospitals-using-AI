import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('staff_utilization_patient_load.csv')

# Set positions and width for the bars
bar_width = 0.25
r1 = np.arange(len(df))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width*2 for x in r1]

plt.figure(figsize=(12, 7))

# Create bars for Nurses, Doctors, Patient Load
plt.bar(r1, df['Nurses'], color='cornflowerblue', width=bar_width, edgecolor='grey', label='Nurses')
plt.bar(r2, df['Doctors'], color='mediumseagreen', width=bar_width, edgecolor='grey', label='Doctors')
plt.bar(r3, df['Patient Load'], color='coral', width=bar_width, edgecolor='grey', label='Patient Load')

# Add labels and title
plt.xlabel('Department', fontweight='bold')
plt.ylabel('Count', fontweight='bold')
plt.title('Staff Utilization vs Patient Load by Department')
plt.xticks([r + bar_width for r in range(len(df))], df['Department'], rotation=45, ha='right')
plt.legend()

plt.tight_layout()
plt.savefig('staff_utilization_vs_patient_load.png')
plt.close()

print('Saved: staff_utilization_vs_patient_load.png')
