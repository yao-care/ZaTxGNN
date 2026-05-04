---
layout: default
title: Benazepril
parent: 僅模型預測 (L5)
nav_order: 59
evidence_level: L5
indication_count: 5
---

# Benazepril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# BENAZEPRIL: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Benazepril is an ACE (angiotensin-converting enzyme) inhibitor used to treat hypertension and to provide renal protection in chronic kidney disease by blocking the renin-angiotensin-aldosterone system (RAAS).
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**, with a prediction score of **99.65%** — however, **no supporting clinical trials or direct publications** have been identified for this specific indication.
An important safety caveat governs this prediction: in bilateral renal artery stenosis, ACE inhibitors are contraindicated due to the risk of acute renal failure, making careful patient selection essential before any consideration of use.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension; renal protection in hypertensive nephropathy |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| South Africa Market Status | Not registered (SAHPRA) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Benazepril is an ACE inhibitor that blocks the conversion of angiotensin I to angiotensin II, reducing peripheral vascular resistance and lowering blood pressure. It also inhibits bradykinin degradation, contributing further to vasodilation. Its renal protective effects are achieved by reducing intraglomerular pressure and attenuating TGF-β-driven interstitial fibrosis — mechanisms relevant to any condition of pathological RAAS overactivation.

The mechanistic link to malignant renovascular hypertension is direct: this condition arises from renal artery stenosis, which triggers excessive RAAS activation as the kidney misinterprets reduced perfusion as systemic hypotension. Because benazepril targets this exact pathway, the TxGNN knowledge graph model assigns a high prediction score (99.65%), reflecting strong biological node connectivity between the drug and disease in the underlying knowledge graph. Class-level evidence from landmark ACE inhibitor RCTs — including the AASK trial (African American Study of Kidney Disease and Hypertension) and BENEDICT trial — further supports the plausibility of RAAS blockade in hypertensive renal conditions, even though direct benazepril-specific data for malignant renovascular hypertension is absent from the current evidence pack.

**Critical safety caveat:** In patients with **bilateral renal artery stenosis** (or stenosis in a solitary functioning kidney), ACE inhibitors are **contraindicated**. Efferent arteriolar dilation from ACE inhibition causes a precipitous drop in glomerular filtration pressure, potentially triggering acute renal failure. This contraindication is not a barrier to the prediction's biological logic, but it is a major clinical constraint requiring imaging workup and careful patient selection before any use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Benazepril in malignant renovascular hypertension.

---

## Literature Evidence

Currently no related literature available specifically addressing Benazepril in malignant renovascular hypertension.

> **Note on retrieved literature for a related prediction:** For the third-ranked TxGNN prediction — pulmonary hypertension due to lung disease/hypoxia — 20 publications were retrieved. Upon review, all 20 are general basic-science papers on hypoxia biology (HIF-1α signalling, tumour hypoxia, neurological effects of oxygen deprivation) and contain **no data on benazepril or ACE inhibitors in pulmonary hypertension**. These results confirm that the PubMed query retrieved false-positive matches on the keyword "hypoxia" rather than clinically relevant evidence, and they do not support a change in the evidence level rating (L5/Hold) for that indication.

---

## South Africa Market Information

Benazepril is currently **not registered with SAHPRA**. No product licences are on record.

> Several other ACE inhibitors **are** SAHPRA-registered and widely available in South Africa, including enalapril, lisinopril, perindopril, quinapril, and ramipril. These agents share the same pharmacological class mechanism and may serve as practical alternatives for managing RAAS-driven hypertensive conditions while benazepril-specific evidence is pending. Clinicians wishing to use benazepril specifically would need to apply for **Section 21 unregistered medicine authorisation** through SAHPRA. Availability on the **Essential Medicines List (EML)** should be verified for public sector procurement.

---

## Safety Considerations

As benazepril is not registered with SAHPRA, no local Professional Information (PI) is available. The following safety information is derived from known ACE inhibitor class pharmacology and the mechanistic analysis provided in the evidence pack.

**Critical Contraindication:**
- **Bilateral renal artery stenosis** or stenosis of the artery to a solitary functioning kidney: ACE inhibitor use is contraindicated; risk of acute renal failure is high.
- **Pregnancy (second and third trimesters):** ACE inhibitors cause foetal renal dysgenesis, oligohydramnios, and neonatal renal failure. Contraindicated.
- **History of ACE inhibitor-associated angioedema:** Rechallenge is contraindicated.

**Key Warnings (ACE Inhibitor class):**
- **Angioedema:** Can be life-threatening; statistically higher incidence in Black patients — an important consideration for the South African population.
- **First-dose hypotension:** Particularly in volume-depleted patients, those on diuretics, or patients with high-renin states (e.g., renovascular hypertension itself).
- **Hyperkalaemia:** Risk increases with concurrent use of potassium-sparing diuretics, NSAIDs, or potassium supplements.
- **Renal function deterioration:** Serum creatinine and eGFR must be monitored at baseline, and again at 1–2 weeks after initiation or dose increase.
- **Dry cough:** Common class effect (mediated by bradykinin accumulation); may require switching to an ARB.

For complete prescribing information, refer to the PI of a SAHPRA-registered ACE inhibitor and the **South African Medicines Formulary (SAMF)**. Report suspected adverse drug reactions to SAHPRA via the **MedWatch** online reporting system.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the pharmacological logic for benazepril in malignant renovascular hypertension is sound — ACE inhibitors directly counteract the pathological RAAS overactivation that drives this condition — the evidence base is currently at Level 5 (model prediction only, with no supporting clinical trials or publications), benazepril is not registered with SAHPRA, and the bilateral renal artery stenosis contraindication introduces a patient-safety barrier requiring mandatory pre-treatment imaging. SAHPRA-registered ACE inhibitors with established local evidence are already accessible for related indications and should be prioritised.

**To proceed, the following is needed:**

- **Imaging workup:** Duplex renal ultrasound or CT/MR angiography to exclude bilateral renal artery stenosis before initiating any ACE inhibitor in patients with suspected renovascular hypertension.
- **Class-level evidence review:** Conduct a formal systematic review of ACE inhibitor class evidence (enalapril, ramipril, lisinopril, etc.) in malignant renovascular hypertension to determine whether class-level data can support an extrapolation to benazepril.
- **SAHPRA registration pathway:** If benazepril offers a specific advantage over registered alternatives (e.g., tolerability, dosing), initiate a Section 21 application or full registration dossier with SAHPRA.
- **Mechanism of action (MOA) data:** Retrieve benazepril's full DrugBank entry to complete the mechanistic analysis and resolve the current data gap (DG002).
- **Renal and electrolyte monitoring plan:** Define a structured monitoring protocol (baseline eGFR, serum creatinine, potassium at 0, 2, 4, and 12 weeks) for any future prospective use.
- **Population-specific safety data:** Assess angioedema risk data specific to Black African patients, given the known elevated class risk in this population.

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. This report should be interpreted in conjunction with SAHPRA-approved prescribing information for registered ACE inhibitors. Adverse drug reactions should be reported to SAHPRA.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

