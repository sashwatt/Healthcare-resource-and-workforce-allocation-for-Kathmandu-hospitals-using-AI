import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv('csv_files/Total Employees of Private Hospitals by Area,Type and Bed category .csv')

df.columns = df.columns.str.strip()

# Ensure output directory exists
output_dir = 'private_hospital_charts'
os.makedirs(output_dir, exist_ok=True)

# For each unique Heading, plot a grouped bar chart for its Areas
for heading in df['Heading'].unique():
    sub_df = df[df['Heading'] == heading]
    areas = sub_df['Area']
    male = sub_df['Male']
    female = sub_df['Female']
    total = sub_df['Total']

    x = range(len(areas))
    width = 0.25

    plt.figure(figsize=(8, 5))
    plt.bar([i - width for i in x], male, width=width, label='Male', color='skyblue')
    plt.bar(x, female, width=width, label='Female', color='lightcoral')
    plt.bar([i + width for i in x], total, width=width, label='Total', color='gray')
    plt.xticks(x, areas, rotation=20, ha='right')
    plt.title(f'Total Employees by {heading}')
    plt.ylabel('Number of Employees')
    plt.xlabel(heading)
    plt.legend()
    plt.tight_layout()
    safe_heading = heading.replace(' ', '_').replace('/', '_').lower()
    plt.savefig(f'{output_dir}/employees_by_{safe_heading}.png')
    plt.close()

print(f'Charts saved in {output_dir}/')
