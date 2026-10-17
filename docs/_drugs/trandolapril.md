---
layout: default
title: Trandolapril
parent: Model Prediction Only (L5)
nav_order: 455
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Trandolapril: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertension (hypertensive disorder). The SAHPRA registration record…"
monitor_inn: "TRANDOLAPRIL"
predicted_indications: ["malignant hypertensive renal disease", "chronic pulmonary heart disease"]
---

# Trandolapril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Trandolapril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Trandolapril is an ACE inhibitor originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but **no clinical trials** and **no publications** specific to this indication were found, so the support is a **model prediction only**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder). The SAHPRA registration record contains no approved indication text. |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, trandolapril is an angiotensin-converting enzyme (ACE) inhibitor. Its efficacy in hypertension is established, and mechanistically it may be applicable to renovascular hypertension.

Renovascular hypertension is strongly driven by activation of the renin-angiotensin-aldosterone system (RAAS), so RAAS blockade is biologically plausible. However, this is close to the original hypertension indication rather than a distinct new use.

There is also an important safety concern. ACE inhibitors can cause an acute decline in renal function in patients with bilateral renal artery stenosis, which is the typical substrate of renovascular hypertension. The very high TxGNN score reflects a model prediction only and does not replace clinical evidence.

**Other predicted indications (all Hold):**

| Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|
| Malignant hypertensive renal disease | 99.92% | L5 | RAAS inhibition may reduce intraglomerular pressure and proteinuria. No specific evidence; overlaps with the approved hypertension use. |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 99.92% | L4 | Only indirect animal and preclinical papers. No human evidence; ACE inhibitors are not established therapy here. |
| Pulmonary hypertension with unclear multifactorial mechanism | 99.92% | L5 | General vasoactive and remodelling rationale only. |
| Braddock syndrome | 99.88% | L5 | No identifiable mechanistic link; the score likely reflects network proximity rather than biology. |
| Chronic pulmonary heart disease | 99.19% | L4 | A single 1996 rat study; no human confirmation. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for malignant renovascular hypertension. No trials were found for the other predicted indications either.

---

## Literature Evidence

Currently no related literature available for malignant renovascular hypertension.

For context, the literature retrieved for the lower-ranked prediction "pulmonary hypertension owing to lung disease and/or hypoxia" is indirect and preclinical:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8166049](https://pubmed.ncbi.nlm.nih.gov/8166049/) | 1994 | Review | Am J Cardiol | Molecular basis of regression of cardiac hypertrophy after chronic mechanical overload |
| [7511729](https://pubmed.ncbi.nlm.nih.gov/7511729/) | 1994 | Animal study | J Cardiovasc Pharmacol | Trandolapril reduced blood pressure by 15% and affected ventricular stiffness and coronary resistance in aged spontaneously hypertensive rats |
| [9218195](https://pubmed.ncbi.nlm.nih.gov/9218195/) | 1997 | Preclinical study | J Hypertens Suppl | Preclinical rationale for the verapamil and trandolapril combination in hypertension and related conditions |
| [8909991](https://pubmed.ncbi.nlm.nih.gov/8909991/) | 1996 | Animal study | Gen Pharmacol | Trandolapril plus verapamil inhibited hypoxia-induced coronary vasospasm after ischaemia-reperfusion injury in dogs |
| [17393952](https://pubmed.ncbi.nlm.nih.gov/17393952/) | 2007 | Case report | J Natl Med Assoc | Resolution of chronic pain in one patient with sickle cell disease treated with an ACE inhibitor |

For "chronic pulmonary heart disease", one animal study is available: [8989645](https://pubmed.ncbi.nlm.nih.gov/8989645/) (1996, J Card Fail), which examined long-term trandolapril on augmented vasoconstriction in rats with chronic heart failure.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| A39/7.1.3/0508 | Tarka 180mg/2mg | Slow-release tablet (Srt) | Not listed in the registration record |

Essential Medicines List (EML) inclusion status is not available in the data compiled for this report.

---

## Safety Considerations

**Contraindications / conditions flagged in the knowledge graph** (these come from the TxGNN knowledge graph, not from SAHPRA label text, and should be verified against the Professional Information):
- **Angioedema** (including hereditary, acquired and RAAS-blocker-induced forms)
- **Renal and hepatic conditions**: kidney disease, liver disease, renal artery obstruction
- **Cardiovascular conditions**: aortic stenosis and aortic valve disease, hypertrophic cardiomyopathy, hypotensive disorder, ventricular tachycardia, atrioventricular block, heart failure
- **Haematological conditions**: neutropenia, agranulocytosis
- **Other**: gallbladder disease, connective tissue disease, bone and cartilage disease, myasthenia gravis

**Drug Interactions** (100 interactions recorded; examples shown):
- **Major**: potassium citrate and potassium bicarbonate (risk of hyperkalaemia)
- **Moderate**: corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), antidiabetic agents (metformin, alogliptin, glimepiride, chlorpropamide, canagliflozin, dapagliflozin, empagliflozin), acetylsalicylic acid, morphine, bupropion, dronabinol, and bowel-preparation agents (picosulfuric acid, polyethylene glycol with electrolytes)

Please refer to the SAHPRA-approved Professional Information (PI) for official warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials or literature for malignant renovascular hypertension. It also overlaps with the approved hypertension use, and ACE inhibitors carry a known renal risk in bilateral renal artery stenosis.

**To proceed, the following is needed:**
- The SAHPRA Professional Information, to confirm warnings, contraindications and the approved indication
- Detailed mechanism of action data
- Clinical or observational evidence of trandolapril in renovascular hypertension, with specific attention to renal safety
- A clear determination of whether this is a genuinely new indication or falls within the existing hypertension use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

