---
layout: default
title: Labetalol
parent: Model Prediction Only (L5)
nav_order: 284
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-29
monitor_inn: "LABETALOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
description: "Labetalol: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Labetalol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Labetalol: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Labetalol is a combined alpha-1 and beta-adrenergic blocker, originally used to treat hypertension and hypertensive disorders.
but there are **no registered clinical trials** and only **1 publication** (a 1981 case report) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9908 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 1 of 1) |
| Number of SAHPRA Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, labetalol blocks both alpha-1 and beta-adrenergic receptors. Alpha-1 blockade causes vasodilation, and beta-blockade reduces heart rate and renin release.

Malignant renovascular hypertension is a severe form of hypertension in which the renin-angiotensin system plays a major role. Reduced renin release and vasodilation are therefore mechanistically plausible. However, this is largely an extension of the existing hypertension indication rather than true repurposing.

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

