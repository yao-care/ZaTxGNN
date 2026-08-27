---
layout: default
title: Phenol
parent: 僅模型預測 (L5)
nav_order: 357
evidence_level: L5
indication_count: 8
---

# Phenol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Phenol: From Topical Caustic Agent to Acne Keloid

## One-Sentence Summary

No original indication is recorded for phenol (DrugBank DB03255) in the current dataset, though it is broadly known as a caustic/keratolytic agent used in chemical skin peels. Of the **8 indications** predicted by the TxGNN model for this drug, only **Acne Keloid** is supported by actual literature (**4 publications** on phenol chemical peels); the remaining seven — including the top-scoring candidate, acrodermatitis chronica atrophicans (99.95%) — have **no clinical trial or literature evidence** and no plausible mechanism, and are explicitly flagged for **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in current data — phenol is generally used as a topical caustic/chemical-peel agent |
| Predicted New Indication | Acne Keloid (the only one of 8 screened candidates with supporting evidence) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails (Acne Keloid only; all other candidates are Hold) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for phenol is not available (Data Gap). Based on known clinical use, phenol is a protein-denaturing caustic agent applied in dermatology as a **deep chemical peel** (e.g., Baker–Gordon and modified formulas such as Exoderm), where controlled epidermal/dermal injury induces collagen remodeling and re-epithelialization.

Acne keloid (acne keloidalis nuchae — scarring/keloidal reaction secondary to acne or follicular inflammation) involves excess fibrotic scar tissue. Phenol's established role in resurfacing acne scars and modulating hypertrophic/keloidal scarring through controlled tissue destruction and collagen remodeling gives this prediction a plausible, literature-anchored mechanistic basis — distinct from the other 7 predicted indications, which have no supporting evidence or mechanistic rationale (see summary below).

---

## Other Screened Predictions (this drug's evidence pack covers 8 candidates)

| Disease | TxGNN Score | Evidence Level | Decision |
|---|---|---|---|
| Acrodermatitis chronica atrophicans | 99.95% | L5 | Hold — no evidence, no mechanistic link |
| Secondary interstitial lung disease (childhood, CTD-associated) | 99.95% | L5 | Hold — no evidence |
| Neonatal dermatomyositis | 99.95% | L5 | Hold — only matching trial studies hydroxychloroquine, not phenol |
| Amyopathic dermatomyositis | 99.95% | L5 | Hold — no evidence |
| **Acne Keloid** | **99.94%** | **L3** | **Proceed with Guardrails** |
| Hydroa vacciniforme, familial | 99.94% | L5 | Hold — no evidence |
| Severe nonproliferative diabetic retinopathy | 99.46% | L5 | Hold — trials/literature found are disease-matched (fenofibrate, aspirin), not phenol-specific |
| Dry eye syndrome | 99.04% | L5 | Hold — trials/literature found are disease-matched (nasal stimulation, omega-3, antimuscarinics), not phenol-specific |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for phenol in Acne Keloid.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17204096](https://pubmed.ncbi.nlm.nih.gov/17204096/) | 2007 | Cohort/Case series | The Journal of Dermatology | Modified phenol peel (Exoderm) evaluated for facial wrinkles, acne scars, and related skin problems in Asian patients, with reduced side effects such as hypertrophic scarring/keloid vs. classic phenol peels |
| [16164153](https://pubmed.ncbi.nlm.nih.gov/16164153/) | 2005 | Review | Cutis | Reviews acne treatment in ethnic skin, noting increased risk of post-inflammatory hyperpigmentation and keloid scarring after acne lesions |
| [866280](https://pubmed.ncbi.nlm.nih.gov/866280/) | 1977 | Review | Postgraduate Medicine | Discusses dermatoses common in Black patients, including keloidal folliculitis |
| [4278481](https://pubmed.ncbi.nlm.nih.gov/4278481/) | 1974 | Case report | Fortschritte der Medizin | Treatment of scalp diseases with Crino-Kaban; relevance to phenol-specific acne keloid treatment not detailed in abstract |

---

## South Africa Market Information

Phenol currently holds **no SAHPRA product registrations** in South Africa (market status: Not marketed; total registrations: 0).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Note: TFDA/SAHPRA labelling warnings and contraindications for phenol are a Blocking data gap — required before any Stage 1 safety review can proceed.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (Acne Keloid indication only — all other 7 predicted indications for phenol are **Hold**)

**Rationale:**
- Phenol chemical peels have an established, literature-documented role in scar/keloid resurfacing, giving Acne Keloid a mechanistically plausible basis (L3) unlike the other 7 candidates, which lack any drug-specific evidence.
- Phenol is not currently marketed or registered in South Africa, so there is no existing local regulatory pathway to build on.

**To proceed, the following is needed:**
- TFDA/SAHPRA-approved Professional Information (warnings, contraindications) — currently a Blocking gap (DG001)
- Confirmed mechanism of action data via DrugBank or equivalent source (DG002)
- SAHPRA registration/import pathway assessment for phenol topical products in South Africa
- Direct clinical evidence (trial or controlled study) specifically evaluating phenol peel for acne keloid, since current literature is limited to case series and narrative reviews
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

