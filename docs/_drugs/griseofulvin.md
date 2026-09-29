---
layout: default
title: Griseofulvin
parent: Model Prediction Only (L5)
nav_order: 247
evidence_level: L5
indication_count: 10
---

# Griseofulvin
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

# Griseofulvin: From Fungal Skin Infections to Myiasis

## One-Sentence Summary

Griseofulvin is an oral antifungal drug, and its established use is in dermatophyte infections of the skin, hair and nails.
The TxGNN model predicts it may be effective for **Myiasis**, but this prediction is supported by **0 clinical trials** and only **1 publication**, a 1970 veterinary review that gives no evidence for griseofulvin in myiasis.
The prediction is most likely a knowledge-graph artefact, so it should not be pursued.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data (dermatophyte infections are the established use, but the record is blank) |
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. From general pharmacology, griseofulvin binds fungal tubulin and disrupts the mitotic spindle. It also deposits in keratin precursor cells, which explains its activity against dermatophytes (Trichophyton, Microsporum, Epidermophyton).

Myiasis is an infestation by fly larvae, so the fungal target is not present. The evidence review found no plausible link between griseofulvin's mechanism and this condition. The high score of 0.994 is probably a graph-proximity artefact, because the parasitic and skin-disease neighbourhood in the knowledge graph is shared.

The same holds for the related predictions ranked 2 to 4 (furuncular, wound and creeping myiasis). Each has no mechanistic rationale, no trials and no literature. Management of these conditions relies on mechanical debridement and antiparasitic or antimicrobial care, not antifungals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered. No SANCTR or PACTR records were identified in the Evidence Pack.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4098614](https://pubmed.ncbi.nlm.nih.gov/4098614/) | 1970 | Review | The Veterinary Record | Overview of parasitic skin diseases in dogs and cats. Veterinary, no abstract, and no griseofulvin data in human myiasis |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. K/20.1.7/0718 | Microcidal | Tablet (oral) | Not recorded in the source data |

The Essential Medicines List (EML) status is not available in the Evidence Pack.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There is no trial evidence, no supporting literature and no plausible mechanism, since myiasis is a fly-larvae infestation and griseofulvin acts only on fungi. Other predicted indications also lack support: echinococcosis, toxoplasmosis and Bacteroidaceae infection have no evidence at all. Cutaneous candidiasis and blastomycosis have only general antifungal reviews (L4), and griseofulvin is not generally active against Candida or deep systemic mycoses.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for any safety screening)
- Mechanism of action data from DrugBank
- Any griseofulvin-specific clinical or in vitro data in myiasis, which is not expected given the biology
- Recommendation: redirect effort to griseofulvin's established dermatophyte indications rather than this prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

