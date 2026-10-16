---
layout: default
title: Olopatadine
parent: Model Prediction Only (L5)
nav_order: 354
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Olopatadine: predicted new indication Rosacea conjunctivitis (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, atopic conjunctivitis…"
monitor_inn: "Olopatadine"
predicted_indications: ["rosacea conjunctivitis", "punctate epithelial keratoconjunctivitis", "parasitic conjunctivitis", "conjunctival folliculosis", "chronic follicular conjunctivitis", "serous conjunctivitis except viral", "Angelucci syndrome", "pseudomembranous conjunctivitis", "acute hemorrhagic conjunctivitis", "blepharoconjunctivitis"]
---

# Olopatadine
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

# Olopatadine: From Allergic Rhinitis and Allergic Conjunctivitis to Rosacea Conjunctivitis

## One-Sentence Summary

Olopatadine is an H1 antihistamine and mast cell stabiliser, originally used for allergic rhinitis, vasomotor rhinitis and several forms of allergic conjunctivitis (atopic, papillary and vernal).
The TxGNN model predicts it may be effective for **rosacea conjunctivitis**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. It is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, atopic conjunctivitis, papillary conjunctivitis, vernal conjunctivitis (from the knowledge graph; the SAHPRA record has no indication text) |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, olopatadine is an H1 receptor antagonist with mast cell stabilising activity. Its efficacy in allergic and atopic conjunctivitis is established, and mechanistically it may relieve itching and ocular surface inflammation in other conjunctival conditions.

The link to rosacea conjunctivitis is uncertain. Ocular rosacea is driven mainly by meibomian gland dysfunction, innate immune activation and *Demodex* infestation. Mast cell or histamine involvement is not well established, so any benefit would probably be limited to symptomatic relief of itch or allergic overlap, not treatment of the underlying disease.

The other top-ranked predictions are also conjunctival conditions. Several (serous conjunctivitis, Angelucci syndrome) largely overlap with existing allergic or vernal indications. Others (acute hemorrhagic and pseudomembranous conjunctivitis) have infectious or severe inflammatory causes that olopatadine is unlikely to address.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for rosacea conjunctivitis.

For context, the lower-ranked predictions have only indirect evidence:
- **Punctate epithelial keratoconjunctivitis**: [22606467](https://pubmed.ncbi.nlm.nih.gov/22606467/) (2011, case report, *Case Reports in Ophthalmological Medicine*) describes limbitis secondary to autologous serum eye drops in a patient with atopic keratoconjunctivitis. Olopatadine 0.2% was part of the background regimen, but the report did not test it for this indication.
- **Parasitic conjunctivitis**: [34029500](https://pubmed.ncbi.nlm.nih.gov/34029500/) (2021, preclinical/mechanistic study, *Current Eye Research*) describes allergic conjunctivitis induced by *Acanthamoeba* excretory-secretory protein. It supports a histamine-mediated allergic component, but olopatadine would only be symptomatic and would not treat the infection.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 53/21.5.1/0457 | Ryaltris | Spray | Not available in the data compiled for this report |

Essential Medicines List (EML) status is not available in the data compiled for this report.

---

## Safety Considerations

**Drug Interactions**: The interaction screen returned 100 records. All listed entries have an unclassified severity level, so their clinical significance cannot be graded. Examples include pantoprazole, omeprazole, lansoprazole, cimetidine, metformin, simvastatin, rosuvastatin, prednisone, prednisolone, hydrocortisone, triamcinolone, doxycycline, tetracycline and epinephrine.

**Knowledge-graph contraindication signals** (not label text and not verified): lower respiratory tract disease, paranasal sinus disease, nasal cavity disease and upper respiratory tract disease.

SAHPRA package insert warnings and contraindications were not available. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (L5). There are no clinical trials or publications for rosacea conjunctivitis, and the mechanistic link is weak because the disease is driven mainly by meibomian gland dysfunction and *Demodex* rather than histamine. The only local registration is Ryaltris, a spray whose approved indication text is not available. Ocular route compatibility has not been assessed.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications and approved indications), which is a blocking gap for safety screening
- Detailed mechanism of action data
- Route compatibility assessment: Ryaltris is a spray, and an ophthalmic formulation would be needed for conjunctival indications
- A focused literature search and, if justified, a small pilot study in ocular rosacea with itch or allergic overlap
- Clinical review of the unclassified interaction records
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

