---
layout: default
title: Dihydrocodeine
parent: 僅模型預測 (L5)
nav_order: 174
evidence_level: L5
indication_count: 10
---

# Dihydrocodeine
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

Using the report structure specified in the task prompt (no additional skill applies — this is a direct content-generation task from a supplied Evidence Pack). Below is the generated report.

---

# Dihydrocodeine: From Analgesic/Antitussive Use to Nasal Cavity Disease

## One-Sentence Summary

> Dihydrocodeine is an opioid analgesic and antitussive (μ‑opioid receptor agonist) with no SAHPRA registration currently on file for the South African market.
> The TxGNN model's top-ranked prediction is **Nasal Cavity Disease**, but this is supported by **0 clinical trials** and **0 publications**, and the evidence pack itself characterizes the proposed mechanistic link as indirect, non-specific, and weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in structured registry data (no SAHPRA/TFDA indication text on file). Known pharmacologically as an opioid analgesic / antitussive (μ‑opioid receptor agonist), per the repurposing rationale notes in this evidence pack |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.99% (0.99991), model rank 120 |
| Evidence Level | L5 (model prediction only — no clinical trials, no literature) |
| South Africa Market Status | Not marketed (未上市) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug (flagged in the evidence pack as a High-severity data gap, DG002). Based on the information that is available, Dihydrocodeine is a μ‑opioid receptor agonist with established analgesic and antitussive (cough-suppressant) pharmacology.

The evidence pack's own repurposing rationale for Nasal Cavity Disease states that there is "no known direct pathological mechanistic connection between nasal cavity disease (structural/inflammatory) and the opioid receptor pathway"; the only plausible link is that Dihydrocodeine's antitussive action might indirectly relieve cough associated with post-nasal drip in some nasal conditions. This is explicitly described as an "extremely indirect, non-specific connection with weak evidence."

In short, this prediction rests on graph-based pattern similarity from TxGNN rather than a validated pharmacological hypothesis. No clinical trials or peer-reviewed literature currently support treating nasal cavity disease with Dihydrocodeine, and the mechanistic story is speculative at best.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Dihydrocodeine currently has **no SAHPRA registrations on file** (total_licenses = 0; market_status = Not marketed). No product registration number, brand name, dosage form, or approved indication text is available from the source data used to build this evidence pack.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Important context from this evidence pack:**
- **Blocking data gap:** TFDA/SAHPRA package-insert warnings and contraindications are not yet available (DG001, severity: Blocking). Per the evidence pack, this means the candidate **cannot proceed to an initial safety (S1) assessment** until package-insert data is obtained.
- **Class-level caution (opioid):** Dihydrocodeine is a μ‑opioid receptor agonist. Standard opioid-class concerns — respiratory depression, dependence/abuse potential, and constipation — apply generally to this class, though drug-specific data was not available in this pack. One retrieved publication (PMID 11915306, on a related dihydrocodeine-containing cough syrup) documents abuse and dependence associated with dihydrocodeine-containing products.

---

## Other TxGNN Candidates Reviewed (Screening Context)

This evidence pack scored 10 candidate indications for Dihydrocodeine; all currently sit at decision stage S0 with a "Hold" recommendation. Several are worth flagging explicitly because the underlying mechanistic rationale is a **safety caution, not a treatment opportunity**:

| Rank | Disease | Score | Note |
|------|---------|-------|------|
| 3 | Allergic urticaria | 99.92% | The rationale flags that opioids (incl. Dihydrocodeine) can trigger non-receptor-mediated mast cell degranulation and histamine release — this may **worsen**, not treat, urticaria. TxGNN's high score likely reflects graph proximity to an adverse-effect node, not therapeutic potential. |
| 8 | Cold urticaria | 99.21% | Same histamine-release concern as above. |
| 10 | Atopic conjunctivitis | 98.78% | IgE-mediated allergic condition; same histamine-release caution applies. |
| 6 | Cervical disc degenerative disorder | 99.32% | Mechanistically plausible as non-specific analgesia (opioid for musculoskeletal/neuropathic pain), but no trials or literature exist for this specific indication. |
| 7 | Headache disorder | 99.26% | 2 supporting publications retrieved (evidence level L4), but neither supports efficacy — one is an abuse case series, the other an unrelated Cochrane index. Major headache guidelines (e.g., AHS/AAN) explicitly **recommend against** opioids for headache due to medication-overuse-headache and dependence risk. |
| 1, 2, 4, 5, 9 | Nasal cavity disease, acute laryngopharyngitis, papillary conjunctivitis, faucial diphtheria, trigeminal autonomic cephalalgia | 98.79%–99.99% | No clinical trials or literature; mechanistic links range from weak/non-specific (symptomatic cough/pain relief) to absent. |

No candidate in this set has clinical trial or robust literature support. Several of the highest-scoring predictions appear to reflect the model's proximity to adverse-effect/safety nodes rather than genuine therapeutic signal — this should be communicated clearly to any reviewer relying on the raw TxGNN score alone.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (Nasal Cavity Disease) has no clinical trial or literature support and rests on a mechanistic link the evidence pack itself describes as weak and indirect (Evidence Level L5).
- A Blocking data gap (missing TFDA/SAHPRA Professional Information) means this candidate cannot yet undergo a basic safety assessment, independent of the efficacy question.

**To proceed, the following is needed:**
- SAHPRA/TFDA-approved Professional Information (warnings, contraindications, drug interactions) to resolve the Blocking data gap (DG001)
- Detailed mechanism of action (MOA) data from DrugBank to properly evaluate the mechanistic rationale (DG002)
- Any preclinical or mechanistic literature specifically addressing Dihydrocodeine in nasal cavity disease, if it exists, to move beyond L5
- Given the histamine-release safety signal identified for the urticaria/conjunctivitis candidates, an explicit pharmacovigilance review before considering those candidates further, since the mechanistic link there points toward risk rather than benefit
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

