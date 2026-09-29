---
layout: default
title: Phenobarbital
parent: Model Prediction Only (L5)
nav_order: 364
evidence_level: L5
indication_count: 10
---

# Phenobarbital
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

# Phenobarbital: From Antiseizure Therapy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Phenobarbital is a barbiturate widely known as an antiseizure and sedative medicine. The TxGNN model ranks **trigeminal nerve neoplasm** as its top predicted new indication. This prediction has **0 clinical trials** and **1 publication** behind it, and that publication does not address tumours, so the evidence is model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA licence data (phenobarbital is an established antiseizure drug) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Phenobarbital is generally understood to enhance GABA-A receptor-mediated inhibition, which underlies its antiseizure and sedative effects. It has no known antineoplastic activity.

**The link to trigeminal nerve neoplasm is not plausible on mechanistic grounds.** The very high score (99.96%) most likely reflects proximity in the knowledge graph through trigeminal- or seizure-related nodes, not a therapeutic relationship. The only paper retrieved concerns Sturge-Weber syndrome, where phenobarbital is used to control seizures, not to treat a tumour.

Other predictions for this drug have a more coherent biological rationale, although the evidence is still indirect:

- Reflex or trigger-specific seizure types, namely thinking, startle, audiogenic, eating, micturition-induced, orgasm-induced and reading seizures. GABA-A potentiation is a plausible class-level rationale.
- Trigeminal neuralgia. Anticonvulsants are standard therapy, but carbamazepine leads. Phenobarbital appears mainly as an enzyme inducer that lowers carbamazepine levels, not as an effective treatment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for trigeminal nerve neoplasm (ClinicalTrials.gov, ICTRP; no SANCTR or PACTR entries were retrieved).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | Anales espanoles de pediatria | Review of 14 Sturge-Weber syndrome cases over 25 years covering clinical features, evolution and treatment response. It does not evaluate phenobarbital for any tumour. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| B1233 (OM) | Propain forte | Tablet (oral) | Not stated in the retrieved record |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction rests on a model score alone (L5). There is no mechanistic plausibility, no clinical trials, and no supporting literature. The single publication is about seizure control in Sturge-Weber syndrome. The local safety data needed for screening are also missing.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings and contraindications). This is a blocking gap.
- Mechanism of action data from DrugBank.
- The approved indication text for the local registration (Propain forte).
- Confirmation of whether the product is single-ingredient phenobarbital or a combination product.
- A review of the lower-ranked seizure-related predictions as research questions. Reading seizures, micturition-induced seizures, thinking seizures, startle epilepsy and trigeminal neuralgia reached L4 evidence, but the retrieved evidence is indirect. No trials test phenobarbital in these specific conditions.

*These results are for research reference only and do not constitute medical advice. Any repurposing candidate requires clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

