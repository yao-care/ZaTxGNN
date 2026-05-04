---
layout: default
title: Clotrimazole
parent: 僅模型預測 (L5)
nav_order: 136
evidence_level: L5
indication_count: 10
---

# Clotrimazole
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

# Clotrimazole: From Superficial Fungal Infections to Acne

## One-Sentence Summary

Clotrimazole is a broad-spectrum imidazole antifungal, globally established for the topical treatment of superficial fungal infections including tinea pedis, vulvovaginal candidiasis, and oropharyngeal candidiasis, though it currently holds no SAHPRA registration in South Africa.
The TxGNN model ranks **Acne** as its #1 predicted new indication with a score of **99.86%**; however, this is currently supported by only **1 suspended Phase 2/3 combination trial** and **no published literature**, making this a highly speculative repurposing path at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Superficial fungal infections (globally established; no SAHPRA-registered indication) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 — Preclinical / mechanistic studies only |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data was not retrieved in this Evidence Pack. Based on well-established pharmacological knowledge, clotrimazole is a synthetic imidazole antifungal belonging to the azole class. It inhibits fungal CYP51 (lanosterol 14α-demethylase), which depletes ergosterol and disrupts fungal cell membrane integrity — producing fungistatic activity and, at higher concentrations, fungicidal effects against *Candida* species and dermatophytes. This mechanism has been extensively confirmed across multiple indications including vulvovaginal candidiasis and superficial dermatomycoses.

Acne vulgaris involves a distinct pathophysiology: *Cutibacterium acnes* (formerly *Propionibacterium acnes*) colonisation, sebaceous gland hyperactivity, follicular hyperkeratosis, and localised inflammation. Clotrimazole has no established direct antibacterial activity against *C. acnes*, meaning there is no straightforward mechanistic link to conventional acne pathophysiology. A plausible indirect connection exists via ***Malassezia* folliculitis** (pityrosporum folliculitis) — a condition caused by *Malassezia* spp. yeasts that is susceptible to azole antifungals and can closely mimic the clinical appearance of acne. In this subtype, clotrimazole would be mechanistically appropriate.

The TxGNN model's high ranking score most likely reflects broad biological associations between fungal/follicular pathways in the knowledge graph, rather than a validated direct mechanism for acne vulgaris. Importantly, the only identified clinical trial was a multi-agent combination study (beclomethasone + gentamicin + clotrimazole) that was subsequently suspended, making it impossible to isolate any contribution from clotrimazole alone.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | **Suspended** | 80 | Evaluated comparative efficacy of a triple combination cream (beclomethasone 0.025% + gentamicin 0.1% + clotrimazole 1%) in patients with contaminated dermatosis presenting with bilateral symmetrical acne-like lesions. The trial was suspended with no reported reason; the independent contribution of clotrimazole cannot be isolated from the combination. Evidence value for clotrimazole monotherapy in acne is negligible. |

---

## Literature Evidence

Currently no related literature available for clotrimazole specifically in acne.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

> **Note:** Clotrimazole is not currently registered with SAHPRA (0 registrations found). Until local registration is established, healthcare professionals should consult internationally recognised prescribing information (e.g., US FDA, EMA, or UK MHRA) and apply appropriate clinical judgement.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN model score, the evidence base for clotrimazole in acne is insufficient to justify advancing this repurposing pathway: the sole identified clinical trial was a multi-component combination study that was suspended before completion, and no monotherapy literature exists for this indication. The mechanistic connection to conventional acne vulgaris is indirect and requires further characterisation before investment in clinical development.

**To proceed, the following is needed:**
- Preclinical evidence establishing clotrimazole's relevance to acne pathophysiology — for example, anti-*Malassezia* efficacy in folliculitis models or characterisation of any anti-inflammatory effects
- Patient subgroup clarification: distinguish acne vulgaris from *Malassezia* folliculitis (pityrosporum folliculitis), where the mechanistic rationale is substantially stronger
- A dedicated Phase 2 RCT evaluating clotrimazole monotherapy versus standard acne care
- A SAHPRA registration strategy — noting that clotrimazole currently has **0 South African registrations**, which must be addressed before any local clinical use regardless of indication

> **Strategic Note for South African Decision-Makers:** While acne is the #1 TxGNN-ranked prediction, two other predicted indications carry substantially stronger and more immediately actionable evidence in this dataset: **vulvovaginal candidiasis (Rank 2: L1 evidence, Proceed with Guardrails)** and **superficial mycosis (Rank 9: L1 evidence, Proceed with Guardrails)**. Both indications have multiple completed Phase 3 RCTs directly evaluating clotrimazole. Given that clotrimazole is not currently registered with SAHPRA despite being a globally recognised first-line antifungal, prioritising a registration submission for vulvovaginal candidiasis or superficial mycosis is likely to yield faster and more clinically impactful results for South African patients than pursuing the acne indication at this stage.

---

*This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. All adverse events should be reported to SAHPRA.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

