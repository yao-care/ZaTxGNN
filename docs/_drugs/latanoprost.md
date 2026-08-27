---
layout: default
title: Latanoprost
parent: 僅模型預測 (L5)
nav_order: 280
evidence_level: L5
indication_count: 10
---

# Latanoprost
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Latanoprost: Original Indication Not Documented — Predicted New Indication: Primary Hereditary Glaucoma

## One-Sentence Summary

> Latanoprost's originally approved indication is not documented in the current evidence pack (flagged as a data gap).
> The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**,
> supported by **1 completed Phase 2 clinical trial** and **0 publications** currently identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current dataset — no SAHPRA license record and no `original_indications` entry provided |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 (1 completed Phase 2 RCT, no supporting literature) |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

The structured mechanism-of-action field for this drug is itself flagged as a data gap (DG002, High severity — pending confirmation via the DrugBank API). However, the evidence pack's repurposing rationale for this candidate describes Latanoprost as a prostaglandin F2α (PGF2α) analogue acting as an FP-receptor agonist. It increases aqueous humor outflow through the uveoscleral pathway, thereby lowering intraocular pressure — a well-established pharmacological mechanism underlying glaucoma and ocular hypertension treatment.

The predicted new indication, Primary Hereditary Glaucoma, is a genetically-linked subtype within the broader glaucoma disease spectrum. Because the FP-receptor/uveoscleral-outflow mechanism is not specific to a particular glaucoma etiology, it is mechanistically plausible that Latanoprost would also lower intraocular pressure in this hereditary subpopulation. That said, it remains to be confirmed whether hereditary glaucoma already falls within the drug's existing approved indication scope (in which case this would represent a population-level extension rather than a genuinely novel indication) — this cannot be determined without the missing original indication and MOA data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | Completed | 37 | Evaluated the ocular hypotensive effect and safety of latanoprost combined with dorzolamide in pediatric primary hereditary glaucoma refractory to surgical treatment (protocol later amended to a 68-eye target). Directly matches the drug class and target population, rated relevance grade A, but remains a single small trial. |

No SANCTR or PACTR-registered trials were identified for this indication in the current evidence pack.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Latanoprost currently has **no active SAHPRA registration** (`total_licenses: 0`), and no license records were returned in the evidence pack. The product should be treated as **not marketed in South Africa** for purposes of this evaluation until registration status is independently verified with SAHPRA.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Note: the evidence pack flags the absence of TFDA/SAHPRA product-label warnings and contraindications as a **Blocking** data gap (DG001) — this specifically prevents the drug from proceeding into the safety pre-screen stage (S1) until resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A Blocking data gap (DG001 — missing approved product labeling/warnings) prevents this candidate from entering the safety pre-screening stage.
- The drug has no current SAHPRA market registration in South Africa, and evidence is limited to a single completed Phase 2 trial (L2) with no corroborating literature.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI) — warnings, contraindications, and drug interaction data (resolves DG001)
- Confirmed mechanism of action via DrugBank API (resolves DG002)
- Confirmation of the drug's originally approved indication(s), currently missing from this record
- Verification of South African market/registration status
- Additional trials or literature to raise the evidence level above L2 before reconsideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

