---
layout: default
title: Griseofulvin
parent: 僅模型預測 (L5)
nav_order: 242
evidence_level: L5
indication_count: 10
---

# Griseofulvin
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

# Griseofulvin: From Dermatophyte Infections to Myiasis

## One-Sentence Summary

Griseofulvin is a systemic antifungal historically used to treat dermatophyte (fungal) infections of the skin, hair, and nails, such as tinea capitis. The TxGNN model's top prediction for this drug is **Myiasis** (fly-larvae skin infestation), but this is supported by only **0 clinical trials** and **1 tangentially related publication**, and the model's own rationale flags the mechanism as biologically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatophyte (fungal) infections of skin, hair, and nails (e.g., tinea capitis) — based on established pharmacology; no SAHPRA-registered product record is present in this evidence pack |
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data was not retrievable in this evidence pack (data gap DG002). Based on well-established pharmacology captured elsewhere in this evidence pack (see the *cutaneous candidiasis* candidate rationale), griseofulvin works by binding fungal tubulin and disrupting the mitotic spindle of dermatophyte fungi, and it deposits in keratin-precursor cells of skin, hair, and nails. This gives it a narrow, fungus-specific spectrum limited to dermatophytes (*Trichophyton*, *Microsporum*, *Epidermophyton*) — it is not active against yeasts, protozoa, helminths, or arthropods.

**Myiasis is caused by fly larvae (maggot) infestation of tissue** — an entirely different biological process from a fungal infection. Griseofulvin has no known antiparasitic or insecticidal activity, so there is no mechanistic pathway connecting its known pharmacology to this indication. The evidence pack's own repurposing rationale for this candidate states this explicitly: "griseofulvin has no antiparasitic/insecticidal activity; the mechanism is entirely unrelated," and notes the single supporting citation is a 1970 veterinary review of parasitic skin diseases in dogs and cats that does not actually evaluate griseofulvin for myiasis treatment.

This pattern is not isolated to the top-ranked candidate: of the 10 TxGNN-predicted indications reviewed for griseofulvin in this evidence pack (myiasis variants, echinococcosis, toxoplasmosis, cutaneous candidiasis, blastomycosis, Bacteroidaceae infection), every single one was scored **Hold**, and the accompanying rationales consistently note either a complete mechanistic mismatch (parasitic/protozoal/bacterial diseases vs. an antifungal) or a pharmacological mismatch even within fungal disease (e.g., *Candida* is intrinsically resistant to griseofulvin; deep/systemic mycoses like blastomycosis require tissue penetration griseofulvin does not achieve). This suggests the high TxGNN similarity scores in this candidate set likely reflect graph-adjacency effects (e.g., proximity to other anti-infective drug nodes) rather than genuine mechanistic plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4098614](https://pubmed.ncbi.nlm.nih.gov/4098614/) | 1970 | Review | The Veterinary Record | General review of parasitic skin diseases in dogs and cats (Baker KP); does not evaluate griseofulvin as a treatment for myiasis — surfaced by topical overlap only |

---

## South Africa Market Information

Griseofulvin is **not currently marketed in South Africa** — no SAHPRA registrations are on record in this evidence pack (0 licenses). No SAHPRA-approved Professional Information is available to reference for this product.

---

## Safety Considerations

SAHPRA-approved Professional Information (PI) warnings and contraindications for griseofulvin could not be retrieved in this evidence pack (flagged as a **Blocking** data gap — see Conclusion below). No drug-drug interaction records were found. Until this is resolved, no safety assertions can be made; report suspected adverse drug reactions to SAHPRA in the usual manner.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN-predicted indication (myiasis) has no plausible mechanistic link to griseofulvin's known antifungal pharmacology, no clinical trial support, and only one weakly related historical publication. Every other predicted indication reviewed for this drug in this evidence pack was independently scored Hold for the same reason — mechanistic mismatch or known pharmacological resistance. The drug is also not currently marketed in South Africa, and a Blocking data gap (missing PI warnings/contraindications) prevents even a preliminary safety assessment.

**To proceed, the following is needed:**
- Confirmed DrugBank mechanism-of-action record (currently a data gap, DG002)
- SAHPRA Professional Information / label warnings and contraindications, if griseofulvin is to be considered for any registration pathway (currently a Blocking data gap, DG001)
- A biologically plausible target indication — the current candidate set (myiasis and related parasitic/protozoal/bacterial diseases) does not present one; re-scoring against indications within griseofulvin's known dermatophyte-specific spectrum would be a more productive next step
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

