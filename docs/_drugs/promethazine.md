---
layout: default
title: Promethazine
parent: 僅模型預測 (L5)
nav_order: 381
evidence_level: L5
indication_count: 10
---

# Promethazine
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

# Promethazine: From Allergic Conditions to Rosacea Conjunctivitis

## One-Sentence Summary

Promethazine is a first-generation phenothiazine antihistamine long used for allergic conditions, nausea/vomiting, and sedation. The TxGNN model's top-ranked prediction for this drug is **Rosacea Conjunctivitis**, with the highest prediction score of any candidate in this evidence pack (**98.94%**), but currently **no clinical trials and no published literature** support this specific link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic conditions (e.g. urticaria, rhinitis), nausea/vomiting, and sedation — classic first-generation H1-antihistamine uses (structured regulatory indication text is not available in this evidence pack) |
| Predicted New Indication | Rosacea Conjunctivitis |
| TxGNN Prediction Score | 98.94% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Promethazine is not available in this evidence pack (flagged as a Blocking-severity data gap, DG002). Based on the literature evidence associated with this drug (e.g. PMID 22130869, PMID 24791618), Promethazine is a first-generation phenothiazine H1-histamine receptor antagonist with pronounced anticholinergic and CNS-sedative properties, historically used for allergic conditions, nausea/vomiting, and preoperative sedation.

Rosacea conjunctivitis is primarily driven by meibomian gland dysfunction and vascular/inflammatory dysregulation rather than a classic IgE/histamine-mediated allergic process. The model's own rationale for this candidate states that Promethazine's H1-antagonism is only indirectly related to this pathology, and explicitly notes a lack of mechanistic support evidence.

This means the high TxGNN score reflects a strong association within the model's knowledge graph, but does not correspond to an established or mechanistically direct pharmacological rationale. With no supporting clinical trials or literature specific to this drug–disease pair, the prediction should currently be treated as a hypothesis-generating signal only, not a clinically actionable repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Promethazine is not currently registered with SAHPRA in South Africa (0 active licenses on record).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite the highest TxGNN prediction score in this evidence pack, Rosacea Conjunctivitis has no supporting clinical trials or literature, and the mechanistic link is explicitly flagged as weak/indirect. A Blocking-severity data gap (missing SAHPRA/PI safety warnings and contraindications) also prevents even a preliminary safety review (S1) at this time.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI) — warnings, contraindications (Blocking gap, DG001)
- Mechanism of action data from DrugBank (High-priority gap, DG002)
- Preclinical or case-level evidence directly linking Promethazine to rosacea conjunctivitis
- Note: among the 10 TxGNN-predicted candidates for Promethazine in this evidence pack, **allergic urticaria** (L4, "Research Question") and especially **rhinitis** (L3, "Proceed with Guardrails," supported by 7 clinical trials and 20 publications) show substantially stronger evidence and may warrant separate, higher-priority evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

