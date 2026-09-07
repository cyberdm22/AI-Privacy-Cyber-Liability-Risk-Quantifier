import pandas as pd
import numpy as np

# Set random seed for technical reproducibility
np.random.seed(42)

num_records = 5000

# 1. Statutory SPDI Categories as defined under Rule 3 of IT Rules, 2011
spdi_categories = [
    'Rule_3_i_Passwords',
    'Rule_3_ii_Financial_Data',
    'Rule_3_iii_v_Health_Medical_Records',
    'Rule_3_vi_Biometric_Information',
    'Multi_Category_SPDI'
]
spdi_weights = [0.20, 0.30, 0.25, 0.10, 0.15]
simulated_spdi_type = np.random.choice(spdi_categories, num_records, p=spdi_weights)

# 2. Web Application Vulnerability Vectors (Technical Audit Scope)
vulnerabilities = [
    'SQL_Injection', 
    'SSRF', 
    'CSRF', 
    'XSS', 
    'Exception_Handling_Failure', 
    'None'
]
vuln_weights = [0.15, 0.10, 0.15, 0.20, 0.10, 0.30]
simulated_vulns = np.random.choice(vulnerabilities, num_records, p=vuln_weights)

# 3. Volume of Compromised SPDI Records
spdi_volume = np.random.randint(5000, 2000000, num_records)

# 4. ITGC & Statutory Compliance Audit Controls (1 = Pass/Compliant, 0 = Fail/Non-Compliant)
# Rule 8: ISO/IEC 27001 Certification & Annual Third-Party Audit Status
iso_27001_audited = np.random.choice([0, 1], num_records, p=[0.35, 0.65])

# Rule 8: Technical Security Measures (Encryption at Rest)
encryption_at_rest = np.random.choice([0, 1], num_records, p=[0.30, 0.70])

# Rule 5(1): Written/Explicit Consent Recorded
explicit_consent_obtained = np.random.choice([0, 1], num_records, p=[0.25, 0.75])

# Rule 5(9): Active Grievance Officer & Redressal Mechanism
grievance_officer_active = np.random.choice([0, 1], num_records, p=[0.20, 0.80])

# NIST SP 800-34 / BCP: Incident Response Plan Tested
ir_plan_tested = np.random.choice([0, 1], num_records, p=[0.45, 0.55])

# 5. Build Calibrated Telemetry DataFrame
df = pd.DataFrame({
    'App_ID': [f"APP_NLIU_{i:04d}" for i in range(1, num_records + 1)],
    'SPDI_Category': simulated_spdi_type,
    'SPDI_Records_Exposed': spdi_volume,
    'Primary_Vulnerability': simulated_vulns,
    'Rule_8_ISO27001_Audited': iso_27001_audited,
    'Rule_8_Encryption_Active': encryption_at_rest,
    'Rule_5_Explicit_Consent': explicit_consent_obtained,
    'Rule_5_Grievance_Mechanism': grievance_officer_active,
    'BCP_IR_Plan_Tested': ir_plan_tested
})

# Export dataset
df.to_csv('breach_telemetry.csv', index=False)
print("Calibrated telemetry dataset successfully generated: 'breach_telemetry.csv'")
