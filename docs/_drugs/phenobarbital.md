---
layout: default
title: Phenobarbital
parent: 僅模型預測 (L5)
nav_order: 356
evidence_level: L5
indication_count: 10
---

# Phenobarbital
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

# Phenobarbital: From Seizure Disorders to Trigeminal Nerve Neoplasm (Low-Confidence Signal)

## One-Sentence Summary

> Phenobarbital is a long-established GABA-A receptor modulator whose registered original indication is not documented in this evidence pack (the drug is currently unregistered/not marketed in South Africa); its clinically established international use is in seizure/epilepsy management, as referenced in the underlying analysis notes.
> The TxGNN model's top-ranked prediction is **Trigeminal Nerve Neoplasm**, but this is supported by **0 clinical trials** and only **1 tangentially related publication**, and the evidence pack's own analysis explicitly flags this top prediction as likely **model noise** rather than a genuine signal.
> Evidence strength is minimal (**L5**), and the recommended decision is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the local regulatory record (no licenses on file); established international use is seizure/epilepsy management |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for phenobarbital in this evidence pack. Based on the analysis notes accompanying the predictions, phenobarbital is a broad-spectrum positive allosteric modulator of the GABA-A chloride channel, with clinically established use across multiple seizure types. It has no known antineoplastic mechanism.

For the top-ranked candidate — trigeminal nerve neoplasm — the pack's own repurposing rationale states this prediction is very likely a **comorbidity-driven artifact**: the single supporting publication is a 1997 case series on Sturge-Weber syndrome, in which phenobarbital was used to control the patient's seizures, not to treat any tumour. There is no mechanistic pathway linking GABA-A modulation to tumour biology, and no oncology-specific trial or literature evidence exists for this pairing.

By contrast, several lower-ranked candidates in this same evidence pack (e.g., rank 2 "thinking/reflex seizures," rank 3 "startle epilepsy," and rank 9 "trigeminal neuralgia") have a mechanistically coherent rationale rooted in phenobarbital's genuine anticonvulsant/GABAergic activity and carry somewhat stronger (though still limited) literature support (L3–L4). These would be more defensible starting points than the rank-1 signal if this drug's repurposing potential is pursued further.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case Series | Anales españoles de pediatría | Review of 14 Sturge-Weber syndrome cases; phenobarbital was used to manage the patients' co-occurring seizures, not to treat the associated vascular/neural lesions — not direct evidence for a tumour indication |

---

## South Africa Market Information

Phenobarbital currently has **no SAHPRA registrations on file** (0 licenses; market status: Not Marketed). No product, dosage form, or approved indication text is available to summarize.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*Note: the underlying evidence pack flags TFDA label warnings/contraindications as a **Blocking**-severity data gap (DG001) — this must be resolved before any safety pre-assessment (S1) can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (trigeminal nerve neoplasm) has L5 evidence — no clinical trials and a single, mechanistically unrelated case report — and is explicitly assessed by the underlying rationale as likely prediction noise from a comorbidity association rather than a real signal.
- The drug is not currently registered or marketed in South Africa, and core safety data (warnings, contraindications, DDI) are entirely unavailable, blocking any safety evaluation.

**To proceed, the following is needed:**
- Obtain the SAHPRA-approved (or TFDA source) Professional Information to resolve the blocking safety data gap (DG001)
- Obtain confirmed mechanism-of-action documentation (DG002)
- If repurposing is still of interest, redirect evaluation toward the mechanistically better-supported candidates in this same evidence pack (e.g., reflex/startle epilepsy subtypes or trigeminal neuralgia, both L3–L4) rather than the rank-1 signal
- Assess the regulatory pathway for local registration, since phenobarbital is currently unmarketed in South Africa
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

