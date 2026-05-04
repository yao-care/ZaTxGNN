---
layout: default
title: Diphenhydramine
parent: 僅模型預測 (L5)
nav_order: 170
evidence_level: L5
indication_count: 10
---

# Diphenhydramine
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

# Diphenhydramine: From Allergic Reactions to Rosacea Conjunctivitis

## One-Sentence Summary

Diphenhydramine is a first-generation H1 antihistamine globally established for treating allergic reactions, urticaria, and allergic rhinitis, but is currently not registered with SAHPRA in South Africa.
The TxGNN model ranks **Rosacea Conjunctivitis** as its highest-scoring predicted new indication (99.20%), though the mechanistic case for this link is limited.
This top-ranked prediction carries **Evidence Level L5** — with **no clinical trials and no published literature** supporting this specific use — and a **Hold** recommendation is issued; however, lower-ranked predictions such as rhinitis and allergic urticaria carry L1 evidence and a "Proceed with Guardrails" recommendation that warrants separate clinical consideration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic rhinitis, urticaria, allergic reactions (internationally established; not SAHPRA-registered) |
| Predicted New Indication | Rosacea Conjunctivitis |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on established international pharmacology, diphenhydramine is a first-generation H1 histamine receptor antagonist. It competitively blocks histamine at peripheral H1 receptors, thereby reducing vasodilation, increased vascular permeability, and smooth muscle contraction associated with allergic and inflammatory responses. Its significant anticholinergic properties additionally reduce glandular secretion — an effect with complex implications for ocular conditions.

Rosacea conjunctivitis is an inflammatory ocular condition associated with rosacea, characterised by lid margin inflammation, meibomian gland dysfunction, and in some cases, Demodex mite colonisation of eyelid follicles. While histamine may contribute to inflammatory flares in rosacea, the core pathophysiological mechanisms — innate immune dysregulation, Demodex-related inflammation, and neurovascular dysregulation — are not primarily driven by the histamine H1 pathway.

The mechanistic link between diphenhydramine and rosacea conjunctivitis is considered **weak**. Of particular clinical concern, diphenhydramine's pronounced anticholinergic effects — including reduced lacrimal gland secretion and decreased aqueous tear production — may **exacerbate** dry eye symptoms and ocular surface discomfort in patients with rosacea conjunctivitis, rather than relieve them. The high TxGNN mathematical score (99.20%) most likely reflects structural patterns in the underlying knowledge graph rather than a clinically meaningful therapeutic connection.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for diphenhydramine in rosacea conjunctivitis.

---

## Literature Evidence

Currently no related literature available for diphenhydramine in rosacea conjunctivitis.

---

## South Africa Market Information

Diphenhydramine is **not currently registered with SAHPRA** and has no active product licences in South Africa. Healthcare professionals wishing to access this medicine for a patient would need to apply for a **Section 21 (unregistered medicine) authorisation** from SAHPRA on a named-patient basis.

For contextual reference, diphenhydramine is marketed internationally (e.g., as Benadryl®) and is available over the counter in many countries including the United States and United Kingdom, where it is approved for allergic rhinitis, urticaria, and short-term sleep aid.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. As diphenhydramine is not registered in South Africa, consult international prescribing information (e.g., the US FDA label or UK SmPC) for guidance on warnings, contraindications, and drug interactions. Report any adverse drug reactions to SAHPRA via the MedSafety application or directly through the SAHPRA pharmacovigilance portal.

---

## Additional TxGNN Predictions Summary

The TxGNN model generated 10 candidate indications for diphenhydramine across this evaluation run. The table below summarises all predictions by evidence strength, to assist clinicians in prioritising which indications are most actionable:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|----------------|----------------|
| 1 | Rosacea Conjunctivitis | 99.20% | L5 | Hold |
| 2 | Rhinitis | 98.35% | L1 | Proceed with Guardrails |
| 3 | Allergic Urticaria | 98.24% | L1 | Proceed with Guardrails |
| 4 | Cold Urticaria | 95.92% | L3 | Proceed with Guardrails |
| 5 | Cauda Equina Syndrome | 95.57% | L5 | Hold |
| 6 | Nasopharyngitis | 94.96% | L4 | Hold |
| 7 | Viral Conjunctivitis | 93.97% | L5 | Hold |
| 8 | Neuralgia | 92.30% | L4 | Research Question |
| 9 | Trigeminal Autonomic Cephalalgia | 92.25% | L3 | Research Question |
| 10 | Glossodynia | 92.08% | L5 | Hold |

**Key observations for clinicians:**

- **Rhinitis (Rank 2, L1)**: 7 clinical trials including a completed Phase 4 RCT (NCT00648973, n=1,021) directly comparing diphenhydramine 25 mg and 50 mg against placebo for nasal congestion in seasonal allergic rhinitis. Multiple published RCTs confirm efficacy. The H1 mechanism directly addresses histamine-mediated nasal vasodilation and hypersecretion. *This is the most evidence-supported prediction in this pack.*

- **Allergic Urticaria (Rank 3, L1)**: A completed Phase 3 pilot trial (NCT02023164, n=36) used intravenous diphenhydramine as the active comparator benchmark for urticaria treatment, confirming its established role. Multiple reviews and position statements support its use. The H1 mechanism — blocking histamine released by mast cell degranulation — is directly applicable.

- **Cold Urticaria (Rank 4, L3)**: No clinical trials identified, but 8 publications including clinical series and a 1949 historical observation of Benadryl suppressing cold hypersensitivity symptoms. The shared H1-mediated mast cell mechanism with allergic urticaria supports biological plausibility.

---

## Conclusion and Next Steps

**Decision: Hold** *(for Rosacea Conjunctivitis — the top TxGNN-ranked indication)*

**Rationale:**
There is currently no clinical trial evidence or published literature specifically supporting diphenhydramine in rosacea conjunctivitis. The mechanistic link is weak, and diphenhydramine's anticholinergic properties risk worsening ocular surface symptoms in this condition. The high TxGNN score reflects computational graph topology rather than clinical evidence.

**To proceed with Rosacea Conjunctivitis, the following is needed:**
- Preclinical studies establishing whether histamine H1 signalling plays a meaningful role in rosacea conjunctivitis pathogenesis
- Safety characterisation of anticholinergic effects on the ocular surface and tear film in this patient population
- A Phase 2 proof-of-concept clinical trial, preferably using a topical ophthalmic formulation (to limit systemic anticholinergic exposure) rather than systemic administration
- Head-to-head comparison against established rosacea conjunctivitis treatments (e.g., ivermectin, azithromycin, omega-3 supplementation, lid hygiene protocols)

> **Clinical note:** While the highest-scored TxGNN prediction (rosacea conjunctivitis) requires further foundational research before clinical consideration, **rhinitis (Rank 2, L1)** and **allergic urticaria (Rank 3, L1)** carry robust, multicentre clinical trial support and are recommended as **Proceed with Guardrails**. These represent more immediately actionable opportunities for South African patients — subject to SAHPRA Section 21 authorisation, appropriate patient selection, and monitoring for first-generation antihistamine side effects (sedation, anticholinergic effects, psychomotor impairment).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

