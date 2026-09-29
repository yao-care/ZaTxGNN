---
layout: default
title: Brimonidine
parent: Model Prediction Only (L5)
nav_order: 75
evidence_level: L5
indication_count: 10
---

# Brimonidine
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

# Brimonidine: From Glaucoma to Papillary Conjunctivitis

## One-Sentence Summary

Brimonidine is an alpha-2 adrenergic agonist eye drop, generally known for lowering eye pressure in glaucoma and ocular hypertension. The registration data supplied here does not state this indication.
The TxGNN model predicts it for **papillary conjunctivitis**, but the **0 clinical trials** and **3 publications** found all describe brimonidine as a *cause* of conjunctivitis, not a treatment.
This prediction most likely reflects an adverse-effect association in the knowledge graph rather than a real repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied SAHPRA data (glaucoma and ocular hypertension are the generally known uses) |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 98.49% |
| Evidence Level | L4 (case reports and a case series only; the literature is adverse-event evidence, not therapeutic) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Brimonidine is generally known to be an alpha-2 adrenergic agonist. It lowers intraocular pressure by reducing aqueous humour production and increasing uveoscleral outflow. This mechanism is coherent with glaucoma. It does not address the inflammation or papillary changes of conjunctivitis.

All three retrieved papers report that long-term topical brimonidine can *induce* allergic, follicular or papillary conjunctivitis, and in one case anterior uveitis. The high TxGNN score therefore most likely reflects a drug-disease link that is harmful rather than therapeutic. No supporting therapeutic mechanism was identified.

The other nine predictions in the pack are also not supported for repurposing:
- **Primary hereditary glaucoma** is probably an on-label use, not repurposing.
- **Lichen planus-type diseases** (three subtypes plus "lichen disease") are supported only by reports of brimonidine *inducing* lichenoid reactions.
- **Rosacea conjunctivitis** has only an indirect link, from topical brimonidine reducing facial redness in cutaneous rosacea.
- **Hair and skin disorders** have no evidence and no mechanistic link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18303383](https://pubmed.ncbi.nlm.nih.gov/18303383/) | 2008 | Case series (adverse event) | Journal of Glaucoma | Bilateral anterior uveitis and granulomatous papillary conjunctivitis in a 78-year-old man after 2 years of brimonidine. The report also describes histologic features. |
| [38992579](https://pubmed.ncbi.nlm.nih.gov/38992579/) | 2024 | Retrospective cohort | BMC Ophthalmology | Compared ocular allergy prevalence in glaucoma patients using a brinzolamide 1.0%/brimonidine 0.2% fixed combination, with and without a concurrent β-blocker. Study design is not fully confirmed and the supplied abstract gives no results. |
| [37352771](https://pubmed.ncbi.nlm.nih.gov/37352771/) | 2023 | Case report (adverse event) | International Journal of Surgery Case Reports | Atypical salmon patch-like conjunctival lesion after long-term topical brimonidine. The report notes that allergic follicular or papillary conjunctivitis is a well-known side effect. |

---

## South Africa Market Information

All five products are eye drops. The supplied data does not include the approved indication text, manufacturer or Essential Medicines List (EML) status.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 47/15.4/0706 | Agobrim Eye Drops | Drops |
| Reg. No. 45/15.4/0688 | Brimoct 5ml | Drops |
| Reg. No. 49/15.4/1079 | Brimoct Co | Drops |
| Reg. No. 50/15.4/0358 | Simbrinza | Drops |
| Reg. No. A39/15.4/0464 | Combigan 2mg/5mg 5ml | Drops |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The retrieved literature also reports these adverse reactions to topical brimonidine:
- Allergic, follicular or granulomatous papillary conjunctivitis
- Anterior uveitis
- Conjunctival lesions
- Periorbital contact dermatitis
- Lichen planus (ocular and nail)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Papillary conjunctivitis is a documented adverse effect of brimonidine, so the model's high score most likely reflects harm rather than benefit. Using the drug for this condition could worsen it.
- No clinical trials exist and no therapeutic mechanism is supported.

**To proceed, the following is needed:**
- The SAHPRA Professional Information (warnings, contraindications and approved indications), which is a blocking gap for safety screening.
- Mechanism of action data from DrugBank.
- Populated original indications, to reclassify "primary hereditary glaucoma" as an on-label use.
- A check of whether the TxGNN drug-disease links for conjunctivitis and lichen planus come from adverse-event records, so that harm associations can be filtered out.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

