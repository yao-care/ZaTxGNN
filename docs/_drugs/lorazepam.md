---
layout: default
title: Lorazepam
parent: 僅模型預測 (L5)
nav_order: 294
evidence_level: L5
indication_count: 10
---

# Lorazepam
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

# Lorazepam: From Anxiolytic/Sedative Use to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Lorazepam is a benzodiazepine (GABA-A receptor modulator) that is **not currently marketed in South Africa**, and a formal original-indication record is not available in this evidence pack. The TxGNN model's top-ranked prediction is **Trigeminal Nerve Neoplasm** (score 99.87%), but this candidate currently has **zero clinical trials and zero published literature**, and the evidence pack's own mechanistic analysis flags it as a likely false-positive knowledge-graph artifact rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (formal SAHPRA indication text unavailable); internationally established as a sedative/anxiolytic/anticonvulsant (benzodiazepine class) |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.87% (rank 1024) |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed formal mechanism-of-action documentation for lorazepam is not available in this evidence pack. Based on its established pharmacological class, lorazepam is a benzodiazepine that acts as a positive allosteric modulator of the GABA-A receptor, producing sedative, anxiolytic, and anticonvulsant effects.

There is no identifiable mechanistic pathway connecting GABA-A receptor modulation to trigeminal nerve neoplasm pathophysiology (tumourigenesis or nerve-sheath tumour biology). The model's high prediction score most likely reflects a knowledge-graph proximity effect — trigeminal neuralgia and epilepsy frequently co-occur with, or are discussed alongside, trigeminal nerve neoplasm in the underlying knowledge graph — rather than a true causal or therapeutic relationship to lorazepam.

Because no clinical trials, no literature, and no mechanistic rationale support this specific prediction, it should be treated as a hypothesis-generation artifact of the model rather than an evidence-based repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Lorazepam has no SAHPRA product registrations on record and is not currently marketed in South Africa (0 licences found in this evidence pack).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction has no supporting clinical trials, no published literature, and no plausible mechanistic link to trigeminal nerve neoplasm — the evidence pack itself identifies it as a probable knowledge-graph false positive. Combined with the drug's non-marketed status in South Africa, there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (warnings/contraindications) — currently a blocking data gap
- Formal mechanism-of-action data from DrugBank
- Dedicated preclinical/mechanistic evidence linking GABA-A modulation to trigeminal nerve tumour biology, if this hypothesis is to be pursued further
- Note: this evidence pack's other TxGNN predictions include **insomnia** (score 99.80%, L2 evidence, "Proceed with Guardrails" recommendation, supported by ~23 clinical trials and ~18 publications) — if the goal is to identify a viable lorazepam repurposing pathway, that candidate warrants a separate, dedicated evaluation report rather than this top-ranked but unsupported prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

