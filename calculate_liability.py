import pandas as pd
import numpy as np

# 1. Load the dataset generated in Step 1
df = pd.read_csv('breach_telemetry.csv')

# 2. Define baseline financial metrics (in INR - Indian Rupees)
BASELINE_COST_PER_RECORD = 2000  # Cost for forensics, notification, and immediate response
DPDP_MAX_PENALTY_INR = 2500000000  # ₹250 Crores maximum statutory penalty cap

# 3. Define the Vulnerability Severity Multiplier
def get_vulnerability_multiplier(vuln):
    multipliers = {
        'SQL_Injection': 1.5,
        'SSRF': 1.4, # Deep backend infrastructure compromise
        'Exception_Handling_Failure': 1.35, # Information leakage enables further exploitation
        'CSRF': 1.2, # Client-side state manipulation
        'XSS': 1.1,
        'None': 1.0
    }
    return multipliers.get(vuln, 1.0)

# 4. Core Liability Calculation Function
def calculate_risk(row):
    # A. Calculate Baseline Operational Cost
    operational_loss = row['SPDI_Records_Exposed'] * BASELINE_COST_PER_RECORD
    
    # B. Apply Technical Severity Multiplier
    vuln_multiplier = get_vulnerability_multiplier(row['Primary_Vulnerability'])
    adjusted_operational_loss = operational_loss * vuln_multiplier
    
    # C. Calculate Statutory Fine Exposure
    # Base fine estimation before legal defenses (e.g., ₹500 per exposed record)
    base_statutory_fine = min(row['SPDI_Records_Exposed'] * 500, DPDP_MAX_PENALTY_INR)
    
    # D. Apply Statutory Defenses (IT Rules 2011 Compliance)
    penalty_reduction = 0.0
    
    # Rule 8: ISO 27001 Audited proves "Reasonable Security Practices"
    if row['Rule_8_ISO27001_Audited'] == 1:
        penalty_reduction += 0.40  # 40% reduction in statutory fine
        
    # Rule 8: Technical encryption at rest
    if row['Rule_8_Encryption_Active'] == 1:
        penalty_reduction += 0.25  # 25% reduction
        
    # Rule 5(1) & 5(9): Explicit Consent & Grievance Mechanism
    if row['Rule_5_Explicit_Consent'] == 1 and row['Rule_5_Grievance_Mechanism'] == 1:
        penalty_reduction += 0.15  # 15% reduction for robust privacy governance
        
    # Cap total possible reduction at 80% to account for strict liability
    penalty_reduction = min(penalty_reduction, 0.80)
    
    adjusted_statutory_fine = base_statutory_fine * (1 - penalty_reduction)
    
    # E. Calculate Total Cyber Liability for Insurance Underwriting
    total_liability = adjusted_operational_loss + adjusted_statutory_fine
    
    return pd.Series([
        adjusted_operational_loss, 
        adjusted_statutory_fine, 
        total_liability, 
        penalty_reduction * 100
    ])

# 5. Apply the calculation to our dataset
df[['Operational_Loss_INR', 'Statutory_Fine_INR', 'Total_Liability_INR', 'Penalty_Mitigation_Percentage']] = df.apply(calculate_risk, axis=1)

# 6. Generate the Insurance Underwriting Readiness Score (0-100)
# A higher score means better security and lower insurance premiums.
df['Insurance_Readiness_Score'] = (df['Penalty_Mitigation_Percentage'] + 
                                  (df['BCP_IR_Plan_Tested'] * 20)) 
df['Insurance_Readiness_Score'] = df['Insurance_Readiness_Score'].clip(upper=100)

# Save the processed Risk Audit Output
df.to_csv('financial_risk_assessment.csv', index=False)
print("Risk modeling complete. Output saved to 'financial_risk_assessment.csv'")
