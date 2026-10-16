---
layout: default
title: Benserazide
parent: Model Prediction Only (L5)
nav_order: 61
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Benserazide: predicted new indication Congenital hypotrichosis milia (evidence level L5). Approved use: Not stated in the SAHPRA registration data compiled for this report (…"
---

# Benserazide
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

# Benserazide: From Parkinsonism (Registered Combination Product) to Congenital Hypotrichosis Milia

## One-Sentence Summary

Benserazide is a peripheral aromatic L-amino acid decarboxylase (AADC) inhibitor. In South Africa it is registered as part of a combination capsule (Madopar HBS), which is used with levodopa for Parkinsonism.
The TxGNN model predicts it may be effective for **congenital hypotrichosis milia** (score 98.4%), but there are **no clinical trials and no publications** supporting this prediction. It is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data compiled for this report (the registered product is Madopar HBS 100 mg/25 mg) |
| Predicted New Indication | Congenital hypotrichosis milia |
| TxGNN Prediction Score | 98.44% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Benserazide inhibits AADC (the DDC gene product) outside the brain. This stops levodopa being converted to dopamine in the periphery. Pharmacology data also list cystathionine β-synthase (CBS) as a target. Detailed mechanism of action data are not otherwise available in the data compiled for this report.

**No mechanistic link can be established between AADC inhibition and this condition.** Nothing in the available data connects AADC or CBS inhibition to hair follicle development or to congenital hypotrichosis milia. The score of 0.984 comes from the knowledge-graph model alone, and no clinical or published evidence backs it. The prediction should be treated as a hypothesis-generating signal only.

Other top-ranked predictions are similar: hypotrichosis simplex of the scalp (98.4%), diffuse alopecia areata (98.1%) and alopecia (97.8%). They also have no supporting clinical evidence. Alopecia areata is autoimmune, and no rationale is given for how an AADC inhibitor would act on it. The cluster of hair-related predictions may reflect shared graph neighbours rather than real biology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for congenital hypotrichosis milia.

For the related prediction **alopecia**, one paper was retrieved: [34900390](https://pubmed.ncbi.nlm.nih.gov/34900390/) (2021, Review/Commentary, *Tremor and Other Hyperkinetic Movements*). It describes alopecia areata as a rare adverse effect of tremor drugs. It does not show a benefit of benserazide and appears to be tangential.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 31/5.4.1/0194 | Madopar HBS 100 mg/25 mg | Capsule (oral) | Not stated in the registration data compiled for this report |

Essential Medicines List (EML) status is not stated in the data compiled for this report.

---

## Safety Considerations

- **Drug interactions (pharmacology targets):** Benserazide acts on L-aromatic amino acid decarboxylase (DDC) and also on cystathionine β-synthase (CBS). No drug-drug interaction severity levels were reported.
- **Possible adverse signal:** A 1979 clinical observation ([PMID 554794](https://pubmed.ncbi.nlm.nih.gov/554794/)) reported that benserazide (125 mg orally) induced typical migraine attacks in 4 migrainous women. This is preliminary, but it is a caution.

No warnings or contraindications are available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials, no supporting literature and no plausible mechanistic link between AADC inhibition and congenital hypotrichosis milia. Safety data from the SAHPRA PI are also missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- The SAHPRA package insert (PI), parsed for warnings, contraindications and the approved indication text
- Detailed mechanism of action data (for example from DrugBank)
- A biological rationale linking AADC or CBS inhibition to hair follicle development
- Preclinical or mechanistic studies, since no clinical evidence exists
- Review of the migraine-induction signal and of whether a topical or other route would be needed (route compatibility is not yet assessed)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

