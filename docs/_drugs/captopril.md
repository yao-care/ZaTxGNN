---
layout: default
title: Captopril
parent: 僅模型預測 (L5)
nav_order: 96
evidence_level: L5
indication_count: 4
---

# Captopril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Captopril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Captopril is a first-generation ACE inhibitor with well-established global use in the treatment of hypertension, heart failure, and diabetic nephropathy.
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**, with **20 publications** currently supporting this direction.
No registered clinical trials were identified for this specific indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension (established global pharmacological indication; no SAHPRA registration data currently available) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L3 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data was not retrieved as part of this evidence pack. Based on established pharmacology, captopril is a first-generation, orally active angiotensin-converting enzyme (ACE) inhibitor that blocks the conversion of angiotensin I to angiotensin II — thereby reducing activity across the renin-angiotensin-aldosterone system (RAAS), lowering systemic and renal vascular resistance, and suppressing aldosterone secretion.

Malignant renovascular hypertension arises from critical renal artery stenosis causing renal ischaemia, which triggers severe and sustained RAAS over-activation that drives blood pressure to life-threatening levels with rapid end-organ damage. Captopril directly blocks ACE, interrupting angiotensin II-mediated vasoconstriction and aldosterone secretion and reducing renovascular resistance. In the malignant phase — where diffuse microvascular damage and rapidly escalating angiotensin II concentrations are central features — RAAS blockade is mechanistically critical.

Importantly, the captopril renogram (captopril renal scintigraphy) is an established diagnostic test for renovascular hypertension, exploiting captopril's pharmacodynamic interaction with the renal renin system to unmask asymmetric perfusion caused by renal artery stenosis. The broad clinical application of captopril in both the diagnosis and treatment of renovascular conditions directly supports the mechanistic plausibility of the TxGNN prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [6145432](https://pubmed.ncbi.nlm.nih.gov/6145432/) | 1984 | Observational | Biull Vsesoiuznogo kardiologicheskogo nauchnogo tsentra AMN SSSR | Clinical experience with captopril in both stable and malignant arterial hypertension |
| [232024](https://pubmed.ncbi.nlm.nih.gov/232024/) | 1979 | Clinical Study | Clinical Science (London) | Captopril induced reactive hyperreninaemia (PRA >14 ng/h/ml) in 43 of 44 patients with untreated renovascular hypertension, a response absent in normal-renin essential hypertension; confirms captopril as both diagnostic and therapeutic tool |
| [8070421](https://pubmed.ncbi.nlm.nih.gov/8070421/) | 1994 | Review | Endocrinol Metab Clin North Am | Renin-secreting tumour series: blood pressure consistently drops with ACE inhibitor treatment; captopril used to characterise secretory autonomy of the renin system |
| [11334320](https://pubmed.ncbi.nlm.nih.gov/11334320/) | 2001 | Case Report | Clinical Nephrology | Renovascular hypertension with neurofibromatosis type 1; captopril challenge increased PRA from 2.8 to 12.6 ng/ml/h, confirming RAAS over-activation as primary treatment target |
| [10955932](https://pubmed.ncbi.nlm.nih.gov/10955932/) | 2000 | Case Series | Pediatric Nephrology | 27 NF1 patients (mean age 12.8 years) assessed over 2–10 years; captopril test used as part of standard diagnostic workup for renovascular hypertension |
| [17008836](https://pubmed.ncbi.nlm.nih.gov/17008836/) | 2006 | Review | Minerva Medica | Comprehensive clinical review of renovascular hypertension; RAAS inhibition identified as central to management; distinguishes true renovascular hypertension from incidental renal artery stenosis |
| [2040938](https://pubmed.ncbi.nlm.nih.gov/2040938/) | 1991 | Review | Journal of Pediatrics | Overview of malignant hypertension including clinical presentation and treatment approaches |
| [2887673](https://pubmed.ncbi.nlm.nih.gov/2887673/) | 1987 | Experimental | Japanese Heart Journal | Two-kidney two-clip Goldblatt model: serial neurohormonal measurements characterise RAAS changes during evolution from benign to malignant hypertension phase; supports RAAS as the primary mechanistic driver |
| [1572120](https://pubmed.ncbi.nlm.nih.gov/1572120/) | 1992 | Case Report | Clinical Nuclear Medicine | Captopril renal scintigraphy applied in a malignant hypertension case; false-positive CRS described despite absence of renal artery stenosis on angiography, illustrating the clinical importance of contextual interpretation |
| [3928961](https://pubmed.ncbi.nlm.nih.gov/3928961/) | 1985 | Case Report | Klinische Wochenschrift | NF patient with bilateral renal artery stenosis and abdominal aortic coarctation; elevated renal venous renin activity confirmed RAAS involvement; captopril administered as antihypertensive after surgical refusal |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Captopril's mechanism of RAAS inhibition is directly aligned with the core pathophysiology of malignant renovascular hypertension, and 20 observational and review publications provide consistent mechanistic and clinical support (L3 evidence). Notably, the captopril renogram is already a recognised clinical diagnostic tool in this disease area, further reinforcing the pharmacodynamic rationale behind the TxGNN prediction.

**To proceed, the following is needed:**
- Verification of current SAHPRA registration status (0 registrations in this data set may reflect incomplete retrieval; the SAHPRA medicine register should be consulted directly, as captopril is a WHO essential medicine)
- Full mechanism of action documentation (not retrieved in this evidence pack)
- Comprehensive safety review covering contraindications, key warnings, and drug-drug interactions (refer to approved PI)
- Specific caution regarding acute kidney injury risk in patients with bilateral renal artery stenosis or a solitary functioning kidney — RAAS blockade can precipitate acute renal failure in these settings and must be weighed carefully in the malignant phase
- Renal function and electrolyte monitoring protocol (serum creatinine, eGFR, potassium) for treatment initiation and titration
- Prospective clinical evidence or registry data specifically targeting the malignant renovascular hypertension subtype to upgrade the evidence level beyond L3
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

