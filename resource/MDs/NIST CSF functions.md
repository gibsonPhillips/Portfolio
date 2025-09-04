# Unreal Inc. Missing Controls Breakdown

## Summary
| **Missing Control** | **NIST CSF Function** | **Type of Control** |
|---|---|---|
| Least Privilege | Protect|Preventive / Administrative|
| Disaster Recovery Plan | Recover(Respong) | Corrective / Administrative |
| Backups | Recover | Corrective / Technical |
| Password Policies (weak)|Protect|Preventive / Administrative |
| Encryption | Protect | Preventive / Technical |
| Intrusion Detection System (IDS) | Detect|Detective / Technical |
| PCI/GDPR/SOC Compliance | Cross-Cutting (Every Category) | Admin / Managerial |
---
## In Depth Breakdown
### 1. Least Privilege
- CSF Function: **Protect**
- Why: Access control is a protection mechanism to limit who can see or modify sensitive data. By giving all employees access to customer data, Unreal Inc. violates both PCI and DSS and least privilege principles. 
## 
### 2. Disaster Recovery Plan (DRP)
- CSF Function: **Recover** (also ties to respond)
- Why: DRP ensures that the organization can recover after an incident (cyberattack, outage, disaster). NIST CSF's Recover function is explicitly about restoring capabilities. 
## 
### 3. Backups
- CSF Function: **Recover**
- Why: Backups are a corrective control. They support recovery of critical data after an incident or loss. They also tie into business continuity. 
## 
### 4. Password Policies
- CSF Function: **Protect**
- Why: Strong password requirements are a fundamental identity management and authentication control. Weak policies equates to weak protection. 
## 
### 5. Encryption
- CSF Function: **Protect**
- Why: Encryption safeguards confidentiality of sensitive data both at rest and in transit. It's absense is a major compliance violation (PCI, GDPR).
## 
### 6. Initrusion Detection System (IDS)
- CSF Function: **Detect**
- Why: IDS is a detective control that identifies suspicious or malicious activity. Currently, Unreal Inc. has no visibility into intrusions. 
## 
### 7. Compliance Failures (PCR, GDPR, SOC)
- CSF Functions: **Identity, Protect, Detect, Respond, Recover**
- Why: Complience is every function. 
    - PCI DSS requires strong Protect (encryption, access controls)
    - GDPR requires identify (knowing where EU data resides), Protect (privacy safeguards), and respond (breach notification, etc)
    - SOC touches on availability (recover), integrity (protect), and confidentiality (protect). 