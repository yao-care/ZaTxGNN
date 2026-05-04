---
layout: default
title: Carvedilol
parent: 僅模型預測 (L5)
nav_order: 100
evidence_level: L5
indication_count: 5
---

# Carvedilol
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

# Carvedilol: From Heart Failure / Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Carvedilol is a third-generation, non-selective β1/β2 and α1 adrenergic receptor blocker with established use in heart failure, hypertension, and left ventricular dysfunction following myocardial infarction. The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension** (TxGNN score 99.55%), drawing on its multi-target haemodynamic and antioxidant mechanisms. However, **no dedicated clinical trials or publications** currently exist for this specific indication, placing this prediction at an early mechanistic (L4) evidence level.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Heart failure; hypertension; left ventricular dysfunction post-myocardial infarction (established class use; no SAHPRA registration data on file) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L4 (mechanistic / preclinical rationale only) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Carvedilol's pharmacological profile is unusually broad for an antihypertensive agent. Unlike conventional beta-blockers, it simultaneously blocks β1 adrenergic receptors (reducing cardiac output and heart rate), β2 adrenergic receptors (non-selective), and α1 adrenergic receptors (relaxing peripheral arterial smooth muscle and reducing vascular resistance). This dual-limb mechanism provides a more comprehensive haemodynamic effect than any single class alone. Additionally, Carvedilol possesses well-characterised antioxidant properties — notably the ability to scavenge superoxide and hydroxyl radicals — that are largely independent of its receptor-blocking activity.

Malignant renovascular hypertension arises when renal artery stenosis (or other renovascular pathology) triggers uncontrolled activation of the renin-angiotensin-aldosterone system (RAAS), culminating in a hypertensive emergency with end-organ damage — retinopathy, encephalopathy, and rapidly progressive nephropathy. Carvedilol's β1 blockade directly suppresses renin secretion from juxtaglomerular cells, partially attenuating RAAS overactivation. Its α1-mediated vasodilation may improve renal perfusion pressure distal to the stenotic lesion, while the antioxidant component could protect the renal vascular endothelium from oxidative injury that perpetuates the malignant course.

It is essential to contextualise this prediction appropriately. The recognised first-line pharmacotherapy for renovascular hypertension remains ACE inhibitors or angiotensin receptor blockers, often combined with revascularisation. No dedicated randomised controlled trials have evaluated Carvedilol in this hypertensive subtype. The TxGNN model's high score most likely reflects the shared neurohormonal and haemodynamic pathophysiology with Carvedilol's established indications (heart failure, essential hypertension) rather than direct experimental confirmation in renovascular disease.

> **Note on mechanism of action data:** Detailed MOA data from DrugBank was not retrieved in this Evidence Pack cycle. The mechanistic rationale above is drawn from published pharmacological literature and the repurposing rationale recorded in this candidate's scoring record. Retrieval of the complete DrugBank MOA profile is recommended before advancing this candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Carvedilol in malignant renovascular hypertension.

*(Queries were performed across ClinicalTrials.gov and WHO ICTRP on 26 March 2026 — zero results returned.)*

---

## Literature Evidence

Currently no related literature available specifically for Carvedilol in malignant renovascular hypertension.

*(PubMed search performed on 26 March 2026 — zero results returned for the Carvedilol + malignant renovascular hypertension query pair.)*

---

## South Africa Market Information

Carvedilol is currently **not registered with SAHPRA** and holds no active product licences in South Africa. No Essential Medicines List (EML) status is applicable at this time.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------------------|--------------|-------------|---------------------|
| — | — | — | No SAHPRA registrations on record |

Clinicians wishing to use Carvedilol in South Africa outside of a clinical trial context would need to apply for a **Section 21 authorisation** (unregistered medicine) through SAHPRA before any patient use. Generic formulations of Carvedilol are widely registered in other jurisdictions (USA, EU, UK), providing a potential regulatory reference pathway.

---

## Additional Predicted Indications — Summary

The following table summarises all five TxGNN-predicted indications for this candidate. Only the top-ranked indication is analysed in detail above; the remaining four are presented here for completeness.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision | Key Concern |
|------|----------------------|-------------|----------------|----------|-------------|
| 1 | Malignant renovascular hypertension | 99.55% | L4 | Hold | No clinical evidence; plausible mechanism |
| 2 | Malignant hypertensive renal disease | 99.55% | L4 | Hold | Shares mechanistic rationale with Rank 1; renal parenchymal focus |
| 3 | Pulmonary hypertension (WHO Group 5 — unclear multifactorial) | 99.54% | L3 | Hold | Pilot Phase 1 safety data exists for β-blockers in PAH; heterogeneous population |
| 4 | Pulmonary hypertension owing to lung disease / hypoxia (WHO Group 3) | 99.54% | L4 | **Hold** | **Active safety concern:** non-selective β2 blockade may precipitate bronchoconstriction in COPD/ILD patients |
| 5 | Braddock syndrome | 99.37% | L5 | Hold | Ultra-rare SETBP1 genetic disorder; no known pharmacological link; purely computational |

> ⚠️ **Rank 4 safety flag:** WHO Group 3 pulmonary hypertension is associated with significant obstructive or restrictive airway disease. Carvedilol's non-selective β2 blockade poses a direct bronchospasm risk in this population and may also impair the protective hypoxic pulmonary vasoconstriction reflex. This indication should **not be pursued** without substantial preclinical safety data.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

> Since Carvedilol is not currently registered in South Africa, prescribers should consult the FDA-approved or EMA-approved Summary of Product Characteristics (SmPC) as a reference document, and seek SAHPRA guidance on appropriate reporting pathways. Key class-level considerations for any clinician reviewing this candidate include the non-selective β-blockade profile (contraindicated in asthma/reactive airway disease), hypotension risk from α1 blockade, and the need for gradual dose titration in heart failure.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high computational confidence score (99.55%) to Carvedilol for malignant renovascular hypertension, underpinned by a pharmacologically coherent multi-mechanism rationale (RAAS suppression via renin inhibition, peripheral vasodilatation, antioxidant renoprotection). However, the complete absence of dedicated clinical trial or published literature evidence for this specific indication — combined with the drug's lack of SAHPRA registration in South Africa — means this prediction currently constitutes a hypothesis-generating signal only, insufficient to support clinical application without further investigation.

**To proceed, the following is needed:**

- **Safety data retrieval:** Obtain and review the full Professional Information (PI) / SmPC for Carvedilol, including all contraindications, warnings, and drug interactions (currently a blocking data gap)
- **MOA data retrieval:** Query the DrugBank API for complete mechanism of action, pharmacodynamics, and pharmacokinetics data (currently a high-severity data gap)
- **Expanded literature search:** Broaden PubMed search to include adjacent terms (e.g., "Carvedilol + hypertensive emergency," "beta-blocker + renovascular hypertension," "carvedilol + renal protection") to capture indirect evidence
- **Registry expansion:** Search EU Clinical Trials Register (EUCTR) and ANZCTR for any Carvedilol trials in related renovascular or malignant hypertension populations
- **Mechanistic study design:** If the above searches confirm absence of direct evidence, consider a narrative review or structured expert consultation to establish whether a pilot investigator-initiated study (Phase 2, add-on design) is scientifically justified
- **SAHPRA pathway planning:** Given zero registrations in South Africa, a Section 21 application strategy or clinical trial protocol (aligned with GCP requirements) must be developed before any patient exposure

---

*This report was generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require rigorous clinical validation before therapeutic application. Evidence Pack version: v4 | Data cutoff: 5 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

