import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('csv_files/patient_to_staff_ratio_by_district.csv')

# Sort by Patient_to_Staff_Ratio for better visualization
df_sorted = df.sort_values('Patient_to_Staff_Ratio', ascending=False)

# Plot bar chart
plt.figure(figsize=(12, 6))
plt.bar(df_sorted['District'], df_sorted['Patient_to_Staff_Ratio'], color='coral')
plt.xlabel('District')
plt.ylabel('Patient to Staff Ratio')
plt.title('Patient to Health Staff Ratio by District')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('patient_to_staff_ratio_by_district.png')
plt.close()

print('Saved: patient_to_staff_ratio_by_district.png')
