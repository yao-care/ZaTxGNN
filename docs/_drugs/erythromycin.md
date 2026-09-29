---
layout: default
title: Erythromycin
parent: Model Prediction Only (L5)
nav_order: 214
evidence_level: L5
indication_count: 10
---

# Erythromycin
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

# Erythromycin: From Antibacterial Use to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Erythromycin is a macrolide antibiotic. The SAHPRA data supplied for it do not state its approved indications.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but **0 clinical trials** and **0 publications** support this specific prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied SAHPRA data (all four registrations lack indication text). Erythromycin is a macrolide antibiotic. |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, erythromycin belongs to the macrolide antibiotic class. Its antibacterial activity is well established, and topical erythromycin is plausible for bacterial infection of the ocular surface.

The link to the predicted indication is weak. Punctate epithelial keratoconjunctivitis is often viral or inflammatory rather than bacterial, so an antibacterial mechanism may not apply. No trials or literature were supplied to test the prediction. The high score (99.89%) should be read as a model signal, not clinical support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this indication. No SANCTR or PACTR entries were supplied.

---

## Literature Evidence

Currently no related literature available for this indication.

---

## Other Predicted Indications (for Context)

The pack also contains evidence for lower-ranked predictions. None of it changes the decision above, but two items are worth noting:

| Predicted Indication | Score | Evidence Level | What the Evidence Shows |
|------|------|------|------|
| Lymphogranuloma venereum | 99.05% | L4 | About 20 publications, mostly reviews and case reports. Macrolides are active against *C. trachomatis*, and erythromycin has been used as an alternative to doxycycline. The azithromycin reports do not apply to erythromycin. There are no trials and no erythromycin-specific comparative data. |
| Necrotizing ulcerative gingivitis | 99.00% | L4 | Historical reports only (1953, 1969) and narrative reviews. Penicillin is preferred and erythromycin is second choice. |

Other predictions have no supporting evidence (L5). Some, such as hyperamylasemia and polyclonal hyperviscosity syndrome, appear to be knowledge-graph artefacts. The two broad categories, "post-bacterial disorder" and "post-infectious syndrome" (L4), are supported mainly by trials of azithromycin or other antibiotics. They show no erythromycin-specific benefit.

The high scores for conjunctivitis-type conditions may partly reflect labelled uses that the supplied data did not capture.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. A/20.1.1/0117 | Ilosone 125P | Suspension |
| Reg. No. V/20.1.1/6 | Adco-erythromycin | Capsule |
| Reg. No. 27/20.1.1/0329 | Dyna-Erythromycin 125Mg | Powder |
| Reg. No. X/13.12/275 | Stiemycin | Lotion |

Approved indication text and Essential Medicines List status were not supplied. None of the four registered forms is an ophthalmic preparation, so route compatibility with an eye indication is unconfirmed.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials or literature for this indication. The antibacterial mechanism fits poorly with a condition that is often viral or inflammatory. No ophthalmic erythromycin product is registered in the supplied SAHPRA data.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications, approved indications). This is currently a blocking gap for safety screening.
- Mechanism of action data from DrugBank.
- A literature and trial search specific to erythromycin in punctate epithelial keratoconjunctivitis.
- Confirmation of whether an ophthalmic erythromycin formulation is registered or accessible in South Africa.
- If a repurposing question is pursued, lymphogranuloma venereum is the better-supported lead (L4). It would need erythromycin-specific comparative data first.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

