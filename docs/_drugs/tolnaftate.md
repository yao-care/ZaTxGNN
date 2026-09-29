---
layout: default
title: Tolnaftate
parent: Model Prediction Only (L5)
nav_order: 449
evidence_level: L5
indication_count: 10
---

# Tolnaftate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Tolnaftate: From Superficial Fungal Infections to Majocchi Granuloma

## One-Sentence Summary

Tolnaftate is a topical antifungal used against superficial skin fungal infections (dermatophytosis). The TxGNN model predicts it may be effective for **Majocchi granuloma**, a deep follicular dermatophyte infection. Currently **0 clinical trials** and **0 publications** support this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration record; classically superficial dermatophyte infections such as tinea pedis |
| Predicted New Indication | Majocchi granuloma |
| TxGNN Prediction Score | 98.59% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the drug record. The mechanistic assessment attached to this prediction says tolnaftate inhibits fungal squalene epoxidase and is active against dermatophytes such as *Trichophyton* species. Majocchi granuloma is caused by these same organisms, so the target organism is plausible.

The weakness is site of infection. Majocchi granuloma is a deep follicular and perifollicular infection that topical agents penetrate poorly, and systemic antifungals are generally required. The high score (0.986) appears to reflect the graph proximity of tolnaftate to other dermatophyte-related nodes, not clinical data. Two related predictions, endothrix and ectothrix infections (hair-shaft dermatophytosis), share the same penetration limitation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| G2331 (ACT 101/1965) | Quadriderm | Cream | Not listed in the retrieved record |

Only a topical cream is registered, and no oral or systemic tolnaftate product is registered in the retrieved record. A topical cream is unlikely to suit a deep follicular infection.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No trials or literature support tolnaftate for Majocchi granuloma. The organism fit is plausible, but a topical cream is unlikely to reach a deep follicular infection, where systemic antifungals are the usual approach. The score alone is not enough to justify progression.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications, approved indications), which is currently a blocking gap
- Mechanism of action data confirmed from DrugBank
- Any clinical evidence of tolnaftate in follicular or deep dermatophytosis, or a rationale for a suitable route and formulation

**Other predictions worth noting:**
- **Superficial mycosis** (rank 5) has the strongest evidence in this pack (L3, Proceed with Guardrails). It includes titles suggesting double-blind comparisons (PMIDs 1090684 and 4619464) and a systematic review (PMID 10398626). It is most likely an existing labelled use rather than true repurposing, and full-text review of these papers could support an upgrade.
- **Cutaneous candidiasis** (rank 3) has weak mechanism-to-organism fit and only indirect literature, so it remains on Hold.
- **Ophthalmic herpes zoster, orbital cellulitis and infectious mononucleosis** have no plausible mechanistic link and are likely graph artifacts.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

