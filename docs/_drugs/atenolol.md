---
layout: default
title: Atenolol
parent: Model Prediction Only (L5)
nav_order: 49
evidence_level: L5
indication_count: 5
monitor_inn: "ATENOLOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-10-23
description: "Atenolol: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension and myocardial infarction"
---

# Atenolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Atenolol: From Hypertension to Malignant Hypertensive Renal Disease
{: .text-alpha }

## One-Sentence Summary

Atenolol is a beta-1 selective blocker whose recorded uses in the knowledge graph include hypertension, myocardial infarction and related conditions.
The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**, but **no clinical trials and no publications** currently address this disease directly, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension and myocardial infarction (relations recorded in the knowledge graph; no approved-indication text is available in the local registrations) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 6 of 6) |
| Number of SAHPRA Registrations | 6 (valid: 6) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, atenolol blocks beta-1 adrenergic receptors. This lowers heart rate and cardiac output and reduces renin release from the kidney, which is why it lowers blood pressure.

Malignant hypertension with renal involvement is an extreme form of hypertension, so a plausible link to atenolol's blood-pressure-lowering effect exists. However, the high model score (0.9985) probably reflects atenolol's known association with hypertension rather than independent evidence for this condition. Beta-blockers are not first-line therapy for hypertensive emergencies. Management generally centres on controlled blood pressure reduction, often parenteral, and blockade of the renin-angiotensin system.

### Other predictions reviewed

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Pulmonary hypertension, unclear multifactorial mechanism | 0.9984 | L5 | No studies. Beta-blockade may reduce the cardiac output the right ventricle depends on, so the link is unsupported and possibly harmful. |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 0.9984 | L5 | The retrieved papers are animal or tangential studies with mixed results on hypoxia-induced right heart hypertrophy. None directly studies this disease in humans. |
| Braddock syndrome | 0.9980 | L5 | Ultra-rare condition with no studies and no defined mechanistic link. |
| Chronic pulmonary heart disease | 0.9904 | L5 | The papers are indirect (mostly atenolol in hypertension or beta-blocker safety in airway disease). None directly studies this disease. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for malignant hypertensive renal disease. The papers retrieved for the other predicted indications do not directly study those diseases either, so they do not raise the evidence level.

---

## South Africa Market Information

Atenolol is marketed in South Africa. All 6 SAHPRA registrations are valid and listed as single-ingredient records. Approved indication text is not available in the data compiled for this report. Essential Medicines List status is also not available in the data compiled for this report.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| 41/5.2/0005 | Gulf atenolol | Tablet |
| A38/5.2/0502 | Tenopress | Tablet |
| 32/5.2/0670 | B-block | Tablet |
| Y/7.1.3/24 | Sandoz Co-Tenidone 50/12.5 | Tablet |
| S/7.1.3/201 | Tenoret 50 50mg/12.5mg | Tablet |
| Z/7.1.3/0096 | Tenchlor hs 50mg/12.5mg | Tablet |

All registered products are oral tablets. The product names Co-Tenidone, Tenoret and Tenchlor suggest 50 mg/12.5 mg combination products, although they are recorded as single-ingredient. Please verify against the registration records.

---

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** The knowledge graph links atenolol with the following conditions as contraindications, which should be checked against the official label: asthma (including intrinsic and allergic asthma), atrioventricular block, Raynaud disease, anaphylaxis, diabetes mellitus (type 1, type 2, diabetic ketoacidosis), liver failure, pancreatitis, systemic lupus erythematosus, psoriasis, gout and hyperuricaemia, anuria, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, potassium deficiency, and anxiety, neurotic and dysthymic disorders.
- **Drug interactions:** 100 interactions were found. Examples with moderate severity include epinephrine, hydrocortisone, hyoscyamine, bupropion, triamcinolone, morphine, acetohexamide, atropine, betamethasone, budesonide and several calcium salts. Minor examples include acetylsalicylic acid, aluminium hydroxide and attapulgite.
- **Additional concern for the predicted uses:** beta-blockade may reduce right ventricular output, which is a concern in pulmonary hypertension and chronic pulmonary heart disease.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No clinical trials or publications directly study atenolol in malignant hypertensive renal disease, so the evidence level is L5. Beta-blockers are not first-line for hypertensive emergencies, and the high model score probably reflects the known hypertension relationship.
- The other predicted indications are also unsupported, and for the pulmonary indications beta-blockade may be harmful.

**To proceed, the following is needed:**
- Clinical or observational studies of atenolol in malignant hypertension with renal involvement, compared with standard care
- Mechanism of action data
- The SAHPRA Professional Information, to confirm approved indications, warnings and contraindications
- A safety assessment for patients with renal impairment and for those with lung or pulmonary vascular disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

