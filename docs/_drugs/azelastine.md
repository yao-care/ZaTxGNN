---
layout: default
title: Azelastine
parent: Model Prediction Only (L5)
nav_order: 55
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Azelastine: predicted new indication Rosacea conjunctivitis (evidence level L5). Approved use: Allergic rhinitis (the registered product has no indication text…"
monitor_inn: "Azelastine"
predicted_indications: ["rosacea conjunctivitis", "allergic urticaria", "acute hemorrhagic conjunctivitis", "pseudomembranous conjunctivitis", "parasitic conjunctivitis", "conjunctival folliculosis", "chronic follicular conjunctivitis", "serous conjunctivitis except viral"]
---

# Azelastine
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

# Azelastine: From Allergic Rhinitis to Rosacea Conjunctivitis

## One-Sentence Summary

Azelastine is an antihistamine nasal spray originally used for allergic rhinitis and related allergic eye conditions.
The TxGNN model predicts it may be effective for **rosacea conjunctivitis** (score 98.6%), but **no clinical trials and no publications** currently support this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis (the registered product has no indication text, so this comes from the drug's known indications: allergic rhinitis, vasomotor rhinitis, atopic, papillary and vernal conjunctivitis) |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 98.6% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, azelastine is an H1-receptor antagonist with mast cell-stabilizing and anti-inflammatory activity. Its efficacy in allergic rhinitis and allergic conjunctivitis is established, and mechanistically it could relieve ocular surface inflammation.

The link to rosacea conjunctivitis is weak, however. Rosacea-related eye disease is driven mainly by meibomian gland dysfunction and inflammation rather than histamine. The high score probably reflects the disease's closeness to other conjunctivitis conditions in the knowledge graph, not a specific biological rationale. The prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 55/21.5.1/0573 | Dymista Nasal Spray | Spray | Not stated in the data compiled for this report |

Only one valid registration exists, and it is a nasal spray. No ophthalmic formulation is registered in the data compiled for this report, which matters for an eye indication.

## Safety Considerations

- **Contraindications flagged in the drug knowledge graph (not from label text):** kidney disease and pyoureter. These should be checked against the approved Professional Information (PI).
- **Drug Interactions:** The interaction screen returned 87 potential interactions, none with a severity grade assigned. Examples include epinephrine, acetylsalicylic acid, metformin, omeprazole, clarithromycin, simvastatin, prednisone and dexamethasone. Clinicians should review these against the PI.

For label-based warnings and contraindications, please refer to the SAHPRA-approved PI. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5), with no trials or publications for rosacea conjunctivitis. The biological link is weak, and no ophthalmic product is registered in South Africa.

**To proceed, the following is needed:**
- Evidence that antihistamine or anti-inflammatory therapy helps rosacea-related ocular disease, such as pilot or comparative studies
- Detailed mechanism of action data
- Label-based safety information from the SAHPRA PI, which is currently missing
- Confirmation of an ophthalmic formulation and its registration status

**Note on other predictions:** Among the other predicted indications, general **conjunctivitis** (score 91.1%) has much stronger support. It has a completed Phase 3 active-controlled trial (NCT06212973), a completed Phase 4 trial (NCT06800274), and several randomized trials of azelastine eye drops. This is largely an existing, on-label use for allergic conjunctivitis. It could be assessed separately, limited to allergic subtypes. Before relying on NCT06212973, check the full record to confirm azelastine's role in the trial (test or comparator arm).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

