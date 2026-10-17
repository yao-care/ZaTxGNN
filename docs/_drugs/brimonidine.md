---
layout: default
title: Brimonidine
parent: Model Prediction Only (L5)
nav_order: 76
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Brimonidine: predicted new indication Papillary conjunctivitis (evidence level L5). Approved use: Open-angle glaucoma, ocular hypertension, rosacea"
monitor_inn: "Brimonidine"
predicted_indications: ["papillary conjunctivitis", "lichen disease", "congenital hypotrichosis milia", "hypotrichosis simplex of the scalp", "diffuse alopecia areata", "annular atrophic lichen planus", "lichen planus pigmentosus", "hypertrophic lichen planus"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Brimonidine: From Open-Angle Glaucoma to Papillary Conjunctivitis

## One-Sentence Summary

Brimonidine is an alpha-2 adrenergic agonist originally used for open-angle glaucoma, ocular hypertension and (topically) facial erythema of rosacea.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**, but the data compiled for this report contain **no clinical trials** and **3 publications**, all of which describe brimonidine as a *cause* of conjunctivitis rather than a treatment. This looks like a false-positive prediction driven by an adverse-effect association.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma, ocular hypertension, rosacea (the SAHPRA registration entries compiled for this report carry no indication text) |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 98.49% |
| Evidence Level | L4 (preclinical/mechanism-level only; the literature consists of adverse-event case reports) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, brimonidine is a selective alpha-2 adrenergic agonist. It lowers intraocular pressure in glaucoma and ocular hypertension, and topically it reduces redness in rosacea through vasoconstriction.

For papillary conjunctivitis, the prediction is **not** mechanistically reasonable. The publications describe brimonidine as a cause of allergic or follicular/papillary conjunctivitis and anterior uveitis. The reaction is likely a hypersensitivity response to the drug or its preservative. The high TxGNN score most likely reflects a drug-disease adverse-effect link in the knowledge graph, not a therapeutic signal.

Other top-ranked predictions show similar problems:
- **Lichen disease and lichen planus variants**: the literature consists of case reports of brimonidine-*induced* lichen planus and dermatological reactions, which argue against benefit.
- **Primary hereditary glaucoma**: biologically plausible as an extension within the glaucoma class, but there is no trial or literature evidence. Alpha-agonists also carry paediatric safety concerns (CNS depression, apnoea in infants), and surgery is usually first-line.
- **Rosacea conjunctivitis (ocular rosacea)**: topical brimonidine is used for facial erythema of rosacea, so an extension is plausible, but ocular rosacea is driven mainly by meibomian gland dysfunction and inflammation, and brimonidine is associated with conjunctival adverse reactions. This is the only prediction flagged as a research question.
- **Hair disorders (hypotrichosis, alopecia areata)**: no mechanistic rationale is evident.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18303383](https://pubmed.ncbi.nlm.nih.gov/18303383/) | 2008 | Case series (adverse event) | Journal of Glaucoma | Bilateral anterior uveitis and granulomatous papillary conjunctivitis in a 78-year-old man after 2 years of brimonidine; brimonidine caused the condition |
| [38992579](https://pubmed.ncbi.nlm.nih.gov/38992579/) | 2024 | Retrospective cohort | BMC Ophthalmology | Compared ocular allergy prevalence with brinzolamide 1.0%/brimonidine 0.2% fixed combination, with and without a β-blocker, in glaucoma patients |
| [37352771](https://pubmed.ncbi.nlm.nih.gov/37352771/) | 2023 | Case report (adverse event) | Int J Surg Case Rep | Atypical salmon patch-like conjunctival lesion after long-term topical brimonidine; allergic follicular or papillary conjunctivitis is a known side effect |

None of these publications supports brimonidine as a treatment for papillary conjunctivitis.

---

## South Africa Market Information

All 5 registrations are valid, single-ingredient or fixed-combination eye drops. Approved indication text and Essential Medicines List (EML) status were not available in the data compiled for this report.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 47/15.4/0706 | Agobrim Eye Drops | Drops | Not available |
| Reg. No. 45/15.4/0688 | Brimoct 5ml | Drops | Not available |
| Reg. No. 49/15.4/1079 | Brimoct Co | Drops | Not available |
| Reg. No. 50/15.4/0358 | Simbrinza | Drops | Not available |
| Reg. No. A39/15.4/0464 | Combigan 2mg/5mg 5ml | Drops | Not available |

---

## Safety Considerations

**Knowledge-graph contraindication associations** (not taken from label text; verify against the SAHPRA-approved Professional Information):
- Cardiovascular and autonomic: orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy, atrioventricular block, cerebrovascular disorder, Raynaud disease, thromboangiitis obliterans
- Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, hypoglycaemia, hyperthyroidism, Graves disease, thyrotoxicosis
- Neuromuscular: myasthenia gravis (including adult-onset), neuromuscular junction disease
- Respiratory: pulmonary emphysema, bronchial disease
- Psychiatric: anxiety disorder, neurotic disorder, dysthymic disorder
- Immunological: anaphylaxis

**Drug interactions:** The interaction query returned 100 records (for example calcitriol, phentermine, pantoprazole, glimepiride, metformin, omeprazole, atropine, prednisone, simvastatin). The severity level for all of these is recorded as "Unknown", so no clinical significance can be assigned.

**Reported adverse effects relevant to this prediction:** allergic follicular or papillary conjunctivitis, granulomatous anterior uveitis, conjunctival lesions, ocular lichen planus, and periorbital contact dermatitis.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and formal contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (papillary conjunctivitis) is a known adverse effect of brimonidine, not a therapeutic target. The high TxGNN score reflects a knowledge-graph adverse-effect association, so this is a repurposing false positive. The other top-ranked predictions have no clinical evidence, and several are also adverse-effect associations (lichen planus variants).

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking data gap for safety screening)
- Detailed mechanism of action data
- For **rosacea conjunctivitis** (the only research-question candidate): a focused literature review of ocular rosacea and brimonidine, including conjunctival safety
- For **primary hereditary glaucoma**: paediatric safety data and evidence from trials or literature before any further consideration
- Exclusion of papillary conjunctivitis and the lichen planus variants as repurposing candidates, with adverse-effect-driven predictions screened out of future model outputs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

