import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

print("Generating Risk Assessment Heatmap...")

# 1. Load the Risk Assessment Data
df = pd.read_csv('financial_risk_assessment.csv')

# 2. Create a Pivot Table averaging the Total Liability for each Vulnerability & SPDI combination
risk_matrix = df.pivot_table(
    values='Total_Liability_INR', 
    index='Primary_Vulnerability', 
    columns='SPDI_Category', 
    aggfunc=np.mean
)

# Convert to Crores (Divide by 10,000,000) for cleaner visualization
risk_matrix_crores = risk_matrix / 10000000

# 3. Configure the Matplotlib/Seaborn Visuals
plt.figure(figsize=(12, 7))
sns.set_theme(style="whitegrid")

# Create the Heatmap (YlOrRd = Yellow to Orange to Red color mapping)
heatmap = sns.heatmap(
    risk_matrix_crores, 
    annot=True, 
    fmt=".2f", 
    cmap="YlOrRd", 
    linewidths=.5,
    cbar_kws={'label': 'Average Financial Liability (in ₹ Crores)'}
)

plt.title('Enterprise Risk Assessment: Financial Liability by SPDI & Vulnerability Vector', fontsize=14, pad=15)
plt.xlabel('SPDI Category (IT Rules, 2011)', fontsize=12)
plt.ylabel('Primary Web Vulnerability', fontsize=12)

# Rotate x-axis labels for readability
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the visual to the project folder
plt.savefig('risk_heatmap.png', dpi=300)
print("Heatmap successfully generated and saved as 'risk_heatmap.png'")
