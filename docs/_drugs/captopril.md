---
layout: default
title: Captopril
parent: Moderate Evidence (L3-L4)
nav_order: 97
evidence_level: L3
indication_count: 4
---

# Captopril
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **4** 
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

# Captopril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Captopril is an ACE inhibitor marketed in South Africa in tablet form. The registration data supplied do not state an approved indication.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**.
This is supported by **0 clinical trials** and **20 publications**, mostly reviews, case reports and diagnostic-test studies rather than treatment trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data supplied (captopril is a known ACE inhibitor used for hypertension) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L3 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Captopril blocks angiotensin-converting enzyme, so less angiotensin II is formed. Malignant renovascular hypertension is strongly driven by the renin-angiotensin system: renal ischaemia raises renin, which raises angiotensin II and blood pressure. Blocking that pathway is therefore mechanistically plausible, and it fits the very high TxGNN score.

The literature supports the biology but not the treatment claim. Several papers show a strong renin-angiotensin component in these patients. One case report describes blood pressure control with captopril in a patient with bilateral renal artery stenosis. The only drug-specific clinical report is a 1984 paper on captopril in stable and malignant hypertension (PMID 6145432). Its design and outcomes could not be verified from the title alone.

Detailed mechanism-of-action data and the labelled indication text are not available in the supplied data, so overlap with the registered hypertension use cannot be confirmed.

The other three predictions are weaker:

- **Malignant hypertensive renal disease** (score 99.28%): biologically plausible, but there are no trials or literature.
- **Pulmonary hypertension with unclear multifactorial mechanism** (score 99.15%): speculative, with no trials or literature.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (score 99.15%): none of the 20 retrieved articles concern captopril or pulmonary hypertension. They are generic hypoxia biology, so the count reflects keyword matching only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No RCTs were found. The table lists the most relevant items for the lead prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6145432](https://pubmed.ncbi.nlm.nih.gov/6145432/) | 1984 | Clinical study (design unverified) | Biull Vsesoiuz Kardiol Nauchn Tsentra AMN SSSR | Captopril in arterial hypertension with stable and malignant course; no abstract, so outcomes unverified |
| [2040938](https://pubmed.ncbi.nlm.nih.gov/2040938/) | 1991 | Review | J Pediatr | Overview of malignant hypertension |
| [17008836](https://pubmed.ncbi.nlm.nih.gov/17008836/) | 2006 | Review | Minerva Med | Clinical concepts of renovascular hypertension; treatment should target renal ischaemia |
| [8070421](https://pubmed.ncbi.nlm.nih.gov/8070421/) | 1994 | Review | Endocrinol Metab Clin North Am | Renin-secreting tumours cause severe hypertension; blood pressure falls on converting-enzyme inhibitor treatment |
| [10955932](https://pubmed.ncbi.nlm.nih.gov/10955932/) | 2000 | Review | Pediatr Nephrol | 27 children with neurofibromatosis type 1 followed for vascular lesions and hypertension; captopril test used in assessment |
| [11334320](https://pubmed.ncbi.nlm.nih.gov/11334320/) | 2001 | Case report | Clin Nephrol | Two cases of renovascular hypertension with neurofibromatosis; captopril used to test renin response |
| [3928961](https://pubmed.ncbi.nlm.nih.gov/3928961/) | 1985 | Not classified (case report) | Klin Wochenschr | Severe renal vascular hypertension with bilateral renal artery stenosis; patient declined surgery and was treated with captopril |
| [232024](https://pubmed.ncbi.nlm.nih.gov/232024/) | 1979 | Not classified (clinical physiology study) | Clin Sci (Lond) | Angiotensin blockade, including captopril, caused a marked renin rise in 43 of 44 patients with renovascular hypertension (diagnostic use) |
| [2887673](https://pubmed.ncbi.nlm.nih.gov/2887673/) | 1987 | Animal model | Jpn Heart J | Neurohormonal changes in benign and malignant phases of Goldblatt hypertension in dogs |
| [1572120](https://pubmed.ncbi.nlm.nih.gov/1572120/) | 1992 | Case report | Clin Nucl Med | False-positive captopril renogram in a patient with malignant hypertension but no renal artery stenosis |

Most of these papers use captopril as a diagnostic probe, not as treatment.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 31/7.1/0658 | Bio-captopril | Tablet | Not stated in supplied data |
| Reg. No. 31/7.1.3/0478 | Captoretic Hs | Tablet | Not stated in supplied data |
| Reg. No. Y/7.1.3/379 | Capozide | Tablet | Not stated in supplied data |

All three products are oral tablets. Essential Medicines List (EML) inclusion was not verified from the supplied data.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The following class-level guardrail comes from the mechanistic assessment, not from the PI. ACE inhibitors can cause acute renal failure in bilateral renal artery stenosis or in a solitary functioning kidney. Any use in renovascular hypertension would need close monitoring of renal function and serum potassium.

For the pulmonary hypertension predictions, vasodilators may worsen ventilation-perfusion mismatch and hypoxaemia in lung disease.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible and the TxGNN score is high. However, there are no clinical trials, and the literature is limited to reviews, case reports and diagnostic studies. The 1984 captopril report is unverified. The SAHPRA safety information has not been obtained, which blocks safety screening.

**To proceed, the following is needed:**
- Download and review the SAHPRA package insert (PI) for warnings, contraindications and the approved indication text.
- Obtain mechanism-of-action data from DrugBank.
- Retrieve the full text of PMID 6145432 to verify design and outcomes.
- Search for controlled or observational studies of ACE inhibitor treatment in malignant renovascular hypertension.
- Define a renal function and potassium monitoring plan for patients with renal artery stenosis.

This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation before any clinical use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

