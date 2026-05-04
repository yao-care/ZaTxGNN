---
layout: default
title: Cinchocaine
parent: 僅模型預測 (L5)
nav_order: 119
evidence_level: L5
indication_count: 7
---

# Cinchocaine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Cinchocaine: From Local Anaesthesia to Bronchitis

## One-Sentence Summary

Cinchocaine (also known as dibucaine) is a potent, long-acting amide-type local anaesthetic, historically used in topical formulations for anorectal conditions such as haemorrhoids and anal fissures.
The TxGNN model predicts it may be effective for **Bronchitis**, with **0 clinical trials** and **0 publications** currently supporting this direction.
Evidence for this repurposing direction is therefore at the lowest tier (L5 — model prediction only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Local anaesthesia; topical use for anorectal conditions — no SAHPRA registration on file |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for cinchocaine. Based on known pharmacological class information, cinchocaine is an amide-type local anaesthetic that works by blocking voltage-gated sodium channels, preventing depolarisation and nerve impulse conduction. It is most commonly encountered as a topical anorectal preparation (e.g., haemorrhoid creams); systemic or inhalation use is not established in routine clinical practice.

The mechanistic hypothesis connecting cinchocaine to bronchitis rests on a class-level extrapolation. Other local anaesthetics — most notably lidocaine — have been studied for their ability to suppress airway neurogenic inflammation, inhibit the NF-κB signalling pathway, and reduce bronchial mucosal inflammatory responses. If cinchocaine shares these properties, a role in airway inflammation management is theoretically conceivable. However, this analogy is derived from a structurally related but distinct compound, and there is no published evidence that cinchocaine itself exerts meaningful anti-inflammatory activity in bronchial tissue.

Importantly, cinchocaine has substantially higher lipid solubility and systemic toxicity potential than lidocaine (particularly cardiovascular and central nervous system toxicity). No inhalation, nebulisation, or intravenous safety data are available. These factors make non-topical routes of administration high-risk, and the mechanistic extrapolation from the lidocaine literature to cinchocaine remains speculative at best. The TxGNN prediction may reflect a shared "airway inflammation" node in the knowledge graph rather than a direct pharmacological relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a TxGNN model-only prediction (Evidence Level L5) with no supporting clinical trials, published literature, or established safety data for any non-topical route; the mechanistic link to bronchitis is a speculative class extrapolation from lidocaine, and cinchocaine's systemic toxicity profile significantly elevates the risk of pursuing non-topical repurposing.

**To proceed, the following is needed:**
- Retrieve the SAHPRA-approved Professional Information (PI) to characterise warnings, contraindications, and known adverse effects
- Obtain cinchocaine mechanism of action data via DrugBank (DB00527) and primary pharmacology literature
- Conduct a targeted literature search for any preclinical (in vitro / animal) data demonstrating anti-inflammatory or anti-bronchospasm activity specifically for cinchocaine
- Assess feasibility of a safe delivery route for bronchitis (inhalation, systemic) given cinchocaine's known toxicity window
- Evaluate whether a class-effect assumption from lidocaine to cinchocaine is pharmacologically defensible before committing to further development steps

---

> **Disclaimer:** This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates identified by the TxGNN model require clinical validation before any therapeutic application. All content should be reviewed in conjunction with SAHPRA-approved product information.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

