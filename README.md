cat << 'EOF' > README.md
# AI-Privacy-Cyber-Liability-Risk-Quantifier

**Predictive PII Leakage Liability & Breach Cost Simulator**
*An ML-Driven Quantitative Risk Modelling Framework for Cyber Insurance Underwriting and Privacy Compliance.*

---

## 🏛 Academic Context
**Institution:** The National Law Institute University (NLIU), Bhopal  
**Program:** Master of Cyber Law and Information Security (MCLIS) - III Semester  
**Course Focus:** Business Continuity Planning (BCP) and Information Technology (IT) Audit  

## 📖 Project Overview
The quantification of cyber liability and the optimization of cyber insurance underwriting remain significant challenges within enterprise risk management. Traditional static audit methodologies fail to dynamically translate technical infrastructure vulnerabilities into precise financial exposure. 

This project is an Artificial Intelligence (AI) driven quantitative risk modeling framework. It simulates the Total Cost of Ownership (TCO) of sensitive personal data breaches by synthesizing enterprise IT telemetry—specifically evaluating web application vulnerabilities such as Server-Side Request Forgery (SSRF) and Cross-Site Scripting (XSS)—with statutory penalty caps dictated by the Digital Personal Data Protection (DPDP) Act, 2023 and the GDPR.

The engine calculates actuarial risk and dynamically factors in penalty mitigations derived from the **Information Technology (Reasonable Security Practices and Procedures and Sensitive Personal Data or Information) Rules, 2011**. Utilizing a Random Forest Regressor, the simulator successfully maps compliance controls to financial risk, achieving a testing R² score of 0.9972.

## ⚖️ Regulatory & Legal Framework Mapping
This project programmatically integrates the following statutory frameworks:
* **IT Rules, 2011 (Rule 3):** Classification of Sensitive Personal Data or Information (SPDI) (e.g., Financial, Medical, Biometric).
* **IT Rules, 2011 (Rule 5):** Verification of explicit written consent and active grievance redressal mechanisms.
* **IT Rules, 2011 (Rule 8):** Validation of "Reasonable Security Practices," specifically through ISO/IEC 27001 audit verification and active encryption controls.
* **DPDP Act, 2023 & GDPR:** Penalty calculation structures representing strict liability caps (e.g., up to ₹250 Crores for data breaches under DPDP).

## 🛠 Technical Architecture
1. **Telemetry & Vulnerability Ingestion (generate_data.py):** Generates 5,000 synthetic enterprise audit records, mapping technical web vulnerabilities (SQLi, SSRF, CSRF, XSS, Exception Handling Failures) against SPDI volume.
2. **Financial Liability Engine (calculate_liability.py):** Translates raw telemetry into financial exposure, applying technical severity multipliers and statutory penalty reductions based on active IT General Controls (ITGC).
3. **ML Predictive Model (train_ai_model.py):** A Random Forest Regressor trained on the financial data to predict liability on unseen infrastructure. Hyper-parameters (n_estimators=100, max_depth=10) are tuned to prevent overfitting.
4. **Interactive Audit CLI (test_audit.py):** A command-line interface allowing IT auditors to manually input system parameters and instantly receive a predicted financial liability and insurance readiness score.

---

## 🚀 Installation & Setup (Kali Linux / Ubuntu)

**1. Clone the Repository**
Open your terminal and execute:
git clone https://github.com/cyberdm22/AI-Privacy-Cyber-Liability-Risk-Quantifier.git
cd AI-Privacy-Cyber-Liability-Risk-Quantifier

**2. Create the Virtual Environment**
python3 -m venv risk_env
source risk_env/bin/activate

**3. Install Dependencies**
pip install pandas numpy scikit-learn joblib

---

## 💻 Usage Instructions

To run the full risk quantification pipeline, execute the scripts in the following order:

### Step 1: Generate the Telemetry
Create the simulated enterprise audit dataset.
python generate_data.py
*(Outputs: breach_telemetry.csv)*

### Step 2: Calculate Financial Liability
Apply the DPDP/IT Rules 2011 logic to calculate the baseline costs and statutory fines.
python calculate_liability.py
*(Outputs: financial_risk_assessment.csv)*

### Step 3: Train the AI Model
Train the Random Forest Regressor and evaluate the R² and RMSE metrics.
python train_ai_model.py
*(Outputs: financial_risk_model.pkl, model_features.pkl)*

### Step 4: Run the Live Audit CLI
Launch the interactive underwriting engine to test new compliance scenarios.
python test_audit.py
*Follow the on-screen prompts to input data volume, vulnerability type, and statutory control status.*

---

## 📊 Model Performance Metrics
* **Algorithm:** Random Forest Regressor (scikit-learn)
* **Training R-Squared:** ~0.9984
* **Testing R-Squared:** ~0.9972
* **Testing RMSE:** ~₹8.37 Crores (against a ~₹250+ Crore penalty cap, representing a <3% error margin).

## 📜 License & Academic Integrity
This project was developed for academic research purposes at The National Law Institute University (NLIU), Bhopal. It is intended to demonstrate the intersection of machine learning, cyber law, and IT auditing frameworks.

---EOF---
