---
layout: default
title: Levodopa
parent: 僅模型預測 (L5)
nav_order: 285
evidence_level: L5
indication_count: 10
---

# Levodopa
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

# Levodopa: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

> Levodopa is the dopamine precursor at the core of standard Parkinson's disease therapy, replacing the dopamine lost through nigrostriatal degeneration.
> The TxGNN model's top-ranked prediction in this evidence pack is **Rasmussen Subacute Encephalitis**, with a prediction score of **99.06%**,
> but currently **0 clinical trials** and **0 publications** support this specific pairing — it is a pure model prediction with no mechanistic or clinical corroboration.
>
> **Note:** This evidence pack actually contains 10 ranked predictions for Levodopa. Several lower-ranked candidates (progressive supranuclear palsy-corticobasal syndrome, Lewy body dementia, multiple system atrophy-parkinsonian type) have substantially stronger evidence (L3, multiple trials/literature) than the top-ranked candidate. See "Other Predicted Indications in This Evidence Pack" below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (established clinical use; no SAHPRA registration record available in this dataset to cite directly) |
| Predicted New Indication | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Levodopa in this dataset. Based on known pharmacology, Levodopa is a dopamine precursor that crosses the blood-brain barrier and is converted to dopamine by dopa decarboxylase, restoring dopaminergic neurotransmission depleted in Parkinson's disease. This mechanism is well established for parkinsonian and dopamine-deficiency syndromes.

For the top-ranked prediction, Rasmussen subacute encephalitis, the mechanistic case is weak. Rasmussen encephalitis is an autoimmune epileptic syndrome with no established connection to dopaminergic pathways. There is no clinical trial or published literature evidence linking Levodopa to this condition — the high TxGNN score appears to reflect a graph-based association rather than a supported biological mechanism.

By contrast, several other predictions in this pack (see below) involve parkinsonian or dopamine-responsive syndromes, which are mechanistically consistent with Levodopa's known pharmacology and are backed by clinical trials and literature.

## Clinical Trial Evidence

Currently no related clinical trials registered for Rasmussen Subacute Encephalitis.

## Literature Evidence

Currently no related literature available for Rasmussen Subacute Encephalitis.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Other Predicted Indications in This Evidence Pack

This evidence pack scored 10 candidate indications for Levodopa. For completeness and to support informed decision-making, all are summarized below (ranked by TxGNN score):

| Rank | Disease | TxGNN Score | Evidence Level | Decision | Basis |
|------|---------|-------------|-----------------|----------|-------|
| 1 | Rasmussen subacute encephalitis | 99.06% | L5 | Hold | No mechanistic link, no trials/literature |
| 2 | PLA2G6-associated neurodegeneration | 98.75% | L4 | Research Question | 20 literature items; some patients show partial/waning Levodopa response (rare disease, no controlled trials) |
| 3 | Myelitis | 98.47% | L5 | Hold | Literature only case reports of secondary parkinsonism after myelitis, not myelitis treatment itself |
| 4 | Transaldolase deficiency | 98.20% | L5 | Hold | No known mechanistic link, no evidence |
| 5 | Paralysis agitans, juvenile, of Hunt | 98.03% | L4 | Research Question | Historical synonym for juvenile parkinsonism; mechanistically direct, but no trials/literature captured — possible vocabulary-mapping gap requiring manual review |
| 6 | Fructose-1,6-bisphosphatase deficiency | 97.81% | L5 | Hold | Metabolic disorder unrelated to dopamine pathways |
| 7 | Progressive supranuclear palsy-corticobasal syndrome | 97.58% | L3 | **Proceed with Guardrails** | 6 trials, 3 literature; Levodopa challenge test is standard diagnostic/therapeutic tool, partial response documented |
| 8 | Lewy body dementia | 97.25% | L3 | **Proceed with Guardrails** | 5 trials, 19 literature (incl. DLB Consortium guidance); Levodopa used cautiously for parkinsonian features |
| 9 | Multiple system atrophy, parkinsonian type | 97.02% | L3 | **Proceed with Guardrails** | 5 trials, 20 literature; dopamine-responsive MSA-P documented in multiple case series |
| 10 | X-linked intellectual disability-ataxia-apraxia syndrome | 96.46% | L4 | Research Question | 4 literature items; direct case reports of Levodopa/carbidopa response in MCT8 deficiency (Allan-Herndon-Dudley syndrome) |

**Clinical takeaway:** Ranks 7–9 (PSP-corticobasal syndrome, Lewy body dementia, MSA-parkinsonian type) represent the most actionable candidates in this pack — all are parkinsonism-spectrum disorders with documented, if often partial or waning, Levodopa responsiveness, and each has L3 evidence with multiple trials and literature. If a single indication is to be prioritized for further development, one of these three is a stronger candidate than the top TxGNN-ranked Rasmussen encephalitis prediction.

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, Rasmussen Subacute Encephalitis)

**Rationale:**
The top-ranked prediction has no supporting clinical trials, no literature, and no plausible mechanistic link to Levodopa's known pharmacology — it does not meet the threshold to advance past S0.

**To proceed, the following is needed:**
- Levodopa mechanism of action (MOA) documentation (currently a Blocking data gap per DG002/DG001)
- SAHPRA-approved Professional Information (PI) covering warnings, contraindications, and interactions (Blocking data gap, DG001)
- If pursuing repurposing work for this drug, redirect evaluation toward ranks 7–9 (PSP-corticobasal syndrome, Lewy body dementia, MSA-parkinsonian type), which already carry L3 evidence and a "Proceed with Guardrails" recommendation
- Manual literature/trial review for rank 5 (juvenile parkinsonism of Hunt) to confirm whether the absence of evidence is a genuine gap or a vocabulary-mapping artifact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

