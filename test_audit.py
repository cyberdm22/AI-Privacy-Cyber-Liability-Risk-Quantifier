import pandas as pd
import joblib
import warnings

# Suppress minor warnings for a clean terminal output
warnings.filterwarnings("ignore")

print("\n--- AIPCUE: AI-Powered Privacy Compliance & Underwriting Engine ---")
print("Loading trained AI model...")

# 1. Load the compiled AI model and the feature structure
try:
    rf_model = joblib.load('financial_risk_model.pkl')
    model_features = joblib.load('model_features.pkl')
except FileNotFoundError:
    print("Error: Model files not found. Run train_ai_model.py first.")
    exit()

# 2. Function to collect manual audit data from the user
def collect_audit_data():
    print("\n[ ENTER AUDIT TELEMETRY ]")
    
    # Technical Parameters
    records = int(input("1. Number of SPDI Records Exposed (e.g., 50000): "))
    vuln = input("2. Primary Vulnerability (SQL_Injection, SSRF, CSRF, XSS, Exception_Handling_Failure, None): ")
    spdi_cat = input("3. SPDI Category (Rule_3_i_Passwords, Rule_3_ii_Financial_Data, Rule_3_iii_v_Health_Medical_Records, Rule_3_vi_Biometric_Information, Multi_Category_SPDI): ")
    
    # ITGC / Statutory Parameters (1 = Yes, 0 = No)
    print("\n[ ENTER STATUTORY CONTROLS (1 = Yes, 0 = No) ]")
    iso_27001 = int(input("4. Rule 8: ISO 27001 Audited? "))
    encryption = int(input("5. Rule 8: Encryption at Rest Active? "))
    consent = int(input("6. Rule 5(1): Explicit Written Consent Obtained? "))
    grievance = int(input("7. Rule 5(9): Active Grievance Officer? "))
    ir_tested = int(input("8. BCP: Incident Response Plan Tested? "))
    
    # 3. Structure the input to match the training data
    input_dict = {
        'SPDI_Records_Exposed': records,
        'Rule_8_ISO27001_Audited': iso_27001,
        'Rule_8_Encryption_Active': encryption,
        'Rule_5_Explicit_Consent': consent,
        'Rule_5_Grievance_Mechanism': grievance,
        'BCP_IR_Plan_Tested': ir_tested
    }
    
    # Convert to DataFrame
    input_df = pd.DataFrame([input_dict])
    
    # Handle the categorical variables (Vulnerability and SPDI Category)
    input_df[f'Primary_Vulnerability_{vuln}'] = 1
    input_df[f'SPDI_Category_{spdi_cat}'] = 1
    
    # 4. Align the new input with the exact structure the AI was trained on
    # Fill missing columns with 0
    for col in model_features:
        if col not in input_df.columns:
            input_df[col] = 0
            
    # Ensure column order matches exactly
    input_df = input_df[model_features]
    
    return input_df

# 5. Run the prediction
new_audit_data = collect_audit_data()
predicted_liability = rf_model.predict(new_audit_data)[0]

print("\n=======================================================")
print("             AUDIT RESULT & RISK PREDICTION            ")
print("=======================================================")
print(f"Predicted Total Financial Liability: ₹{predicted_liability:,.2f}")
print("=======================================================\n")
