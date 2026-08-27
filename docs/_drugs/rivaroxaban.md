---
layout: default
title: Rivaroxaban
parent: 僅模型預測 (L5)
nav_order: 394
evidence_level: L5
indication_count: 10
---

# Rivaroxaban
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

# Rivaroxaban: From Thromboembolic Disease Prevention to Rheumatoid Arthritis

## One-Sentence Summary

> Rivaroxaban is a direct oral Factor Xa inhibitor anticoagulant, established for use in thromboembolic conditions (e.g. venous thromboembolism, stroke prevention in atrial fibrillation) — though the specific original indication text and mechanism-of-action data are not present in this evidence pack.
> The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, with a prediction score of **99.57%**,
> but currently **no clinical trials** and only **3 tangentially related publications** support this direction — none of which directly studied rivaroxaban for rheumatoid arthritis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (drug identity DB06228 = Rivaroxaban, a Factor Xa inhibitor anticoagulant class drug; specific approved indication text unavailable) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for Rivaroxaban is not available in this evidence pack. Based on general drug-class knowledge, Rivaroxaban is a direct Factor Xa inhibitor used in the prevention and treatment of thromboembolic disease; its role in that setting is well established, but this evidence pack does not contain the specific approved-indication text or MOA summary needed to assess mechanistic transferability with confidence.

The theoretical link to rheumatoid arthritis (RA) rests on the observation that chronic inflammation in RA is associated with a hypercoagulable state, and that thrombin itself has pro-inflammatory activity via protease-activated receptors (PARs) — raising the hypothesis that Factor Xa inhibition could have an indirect anti-inflammatory effect. However, **none of the three retrieved publications actually studied rivaroxaban's efficacy in RA**: one is a review of lower-extremity venous thromboembolism management, one is a mechanistic study of thrombin generation assays in autoimmune disease, and one is a cohort study comparing medication adherence between rivaroxaban and apixaban in atrial fibrillation. This places the prediction at the level of a mechanistic hypothesis with no direct or indirect clinical validation.

Given the absence of any clinical trial evidence and the indirect nature of the available literature, this prediction should be treated as an early-stage signal from the TxGNN model requiring further mechanistic and clinical investigation before any confidence can be placed in it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | Review of diagnosis and treatment of lower-extremity venous thromboembolism; does not address RA. |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Basic/Mechanistic | La Revue de médecine interne | Thrombin generation assay used to evaluate hypercoagulability in autoimmune disease (e.g. antiphospholipid syndrome); does not evaluate rivaroxaban treatment of RA. |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohort | PLoS One | Compares medication adherence between rivaroxaban and apixaban in non-valvular atrial fibrillation; unrelated to RA. |

---

## South Africa Market Information

Currently no SAHPRA registration records available. Per the evidence pack, Rivaroxaban is not marketed in South Africa (0 registered licenses).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5 — the prediction is supported only by a plausible inflammation/coagulation mechanistic hypothesis, with no clinical trials and no literature directly evaluating rivaroxaban in rheumatoid arthritis. The drug is also not currently marketed in South Africa (0 SAHPRA registrations), and core safety/MOA data are missing from the evidence pack, so this candidate does not meet the bar to proceed.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action and original-indication data for Rivaroxaban (currently flagged as a High-severity data gap)
- SAHPRA-approved Professional Information — warnings, contraindications, and drug interactions (currently flagged as a Blocking data gap)
- Preclinical or translational studies directly testing Factor Xa inhibition in RA disease models
- If mechanistic signal strengthens, an early-phase clinical study or observational cohort in RA patients with comorbid cardiovascular risk

*Note: Of the 10 TxGNN-predicted indications reviewed for this candidate, the remaining 9 (gout, HIV infection, and several rare genetic syndromes) showed weaker or no mechanistic rationale and were assessed as likely knowledge-graph noise or drug-drug-interaction-driven false signals rather than genuine repurposing candidates.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

