---
layout: default
title: Labetalol
parent: Moderate Evidence (L3-L4)
nav_order: 284
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-15
description: "Labetalol: predicted new indication Malignant renovascular hypertension (evidence level L4). Approved use: Hypertensive disorder / hypertension"
monitor_inn: "LABETALOL"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Labetalol
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **4** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Labetalol: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Labetalol is a combined alpha-1 and beta-adrenergic blocker, originally used to treat hypertension and hypertensive disorders.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but there are **no registered clinical trials** and only **1 publication** (a 1981 case report) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder / hypertension (the registration entry carries no indication text, so this comes from the knowledge graph) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, labetalol blocks both alpha-1 and beta-adrenergic receptors. Alpha-1 blockade causes vasodilation, and beta-blockade reduces heart rate and renin release.

Malignant renovascular hypertension is a severe form of hypertension in which the renin-angiotensin system plays a major role. Reduced renin release and vasodilation are therefore mechanistically plausible. However, this is largely an extension of the existing hypertension indication rather than true repurposing. The high TxGNN score probably reflects how close the prediction sits to the approved hypertension indication in the knowledge graph.

Other predicted indications in the data (malignant hypertensive renal disease, and two forms of pulmonary hypertension) are weaker. The two pulmonary hypertension predictions have no supportive evidence and carry safety concerns, because non-selective beta-blockade is generally cautioned in pulmonary vascular disease and lung disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7242419](https://pubmed.ncbi.nlm.nih.gov/7242419/) | 1981 | Case report | Med J Aust | A 20-year-old man with malignant hypertension and vasculitis linked to hallucinogenic drug use. Minoxidil and labetalol were used for initial blood pressure control, and the vasculitis resolved with prednisone. |

This is a single case report and does not establish efficacy.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| J/7.1.3/52 | Trandate | Tablet (oral) | Not stated in the data compiled for this report |

Essential Medicines List (EML) status could not be determined from the data compiled for this report.

## Safety Considerations

- **Knowledge-graph contraindication signals** (these come from a knowledge graph, not from label text, and need verification against the PI): liver failure, liver disease, hepatic coma/encephalopathy, kidney disease, anuria, atrioventricular block, pulmonary emphysema, bronchial disease, diabetes mellitus, diabetic ketoacidosis, hypotensive disorder, pancreatitis, gallbladder disease, systemic lupus erythematosus, gout, potassium deficiency, hypercalcaemia, hyperparathyroidism, anxiety and related disorders, and others.
- **Drug interactions** (100 recorded in total; examples):
  - **Major**: epinephrine, dolasetron
  - **Moderate**: corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), anticholinergics (atropine, hyoscyamine, dicyclomine, methscopolamine), morphine, cimetidine, canagliflozin, dapagliflozin, chlorpropamide, calcium salts
  - **Minor**: acetylsalicylic acid, magnesium oxide
- For the pulmonary hypertension predictions, non-selective beta-blockade may worsen bronchospasm, hypoxia and right ventricular function.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests mainly on the model score and the overlap with labetalol's existing hypertension use. There are no trials and only one 1981 case report. The package insert safety information has not yet been obtained, so safety screening cannot proceed.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications and approved indications)
- Mechanism of action data from DrugBank
- Clinical evidence in malignant or renovascular hypertension (trials, guidelines or systematic reviews)
- Confirmation that the benefit exceeds what is already covered by labetalol's approved hypertension indication
- Deprioritising the pulmonary hypertension predictions unless supportive clinical evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

