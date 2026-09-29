---
layout: default
title: Oxytetracycline
parent: Model Prediction Only (L5)
nav_order: 358
evidence_level: L5
indication_count: 10
---

# Oxytetracycline
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

# Oxytetracycline: From Tetracycline Antibiotic Use to Chronic Rhinosinusitis

## One-Sentence Summary

Oxytetracycline is a tetracycline-class antibiotic, but no approved indication text is recorded in the supplied SAHPRA data.
The TxGNN model predicts it may be effective for **Chronic Rhinosinusitis**.
There are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Chronic rhinosinusitis |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for oxytetracycline. Based on known information, it belongs to the tetracycline class. Tetracyclines have antibacterial activity and some anti-inflammatory activity, such as matrix metalloproteinase (MMP) inhibition.

Chronic rhinosinusitis involves persistent inflammation of the sinus mucosa, often with bacterial colonisation. An antibacterial and anti-inflammatory agent could therefore plausibly help. This is a general class-level rationale. No oxytetracycline-specific trial or publication was supplied.

The model also ranks the related term **chronic ethmoidal sinusitis** at 99.61%, a subtype of the same disease. This follows the same rationale and is not independent evidence. The model ranks **paranasal sinus neoplasm** at 99.58%, but no antineoplastic mechanism links it to oxytetracycline. It is probably a graph-proximity artefact.

## Clinical Trial Evidence

Currently no related clinical trials registered for chronic rhinosinusitis. No SANCTR or PACTR entries were supplied.

## Literature Evidence

Currently no related literature available for chronic rhinosinusitis.

### Other predicted indications that do have evidence

The only predicted indication with meaningful evidence is **otitis externa** (TxGNN 99.27%, Evidence Level L2). It is ranked 10th, not first. All studies below are topical combination products or comparators. Oxytetracycline's independent contribution cannot be separated, and this may already be an established topical use rather than true repurposing.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2415098](https://pubmed.ncbi.nlm.nih.gov/2415098/) | 1985 | RCT | Arch Otorhinolaryngol | In 55 patients with acute external otitis, oxytetracycline/hydrocortisone/polymyxin B ear drops did not differ significantly from framycitin/gramicidin; 78% were cured |
| [8222746](https://pubmed.ncbi.nlm.nih.gov/8222746/) | 1993 | Randomized comparison | Curr Med Res Opin | 30 patients, ciprofloxacin drops vs oxytetracycline/polymyxin B/hydrocortisone drops for 7 days |
| [2156538](https://pubmed.ncbi.nlm.nih.gov/2156538/) | 1990 | Randomized, single-blind | Eur Arch Otorhinolaryngol | 46 patients, oxytetracycline/hydrocortisone/polymyxin B vs hydrocortisone butyrate; overall cure rate 80% |
| [15949095](https://pubmed.ncbi.nlm.nih.gov/15949095/) | 2005 | Randomized, open-label | J Laryngol Otol | 51 patients, betamethasone dipropionate alone vs hydrocortisone/oxytetracycline/polymyxin B; suggests a steroid alone may suffice |

For **post-bacterial disorder**, the only trial is [NCT02099240](https://clinicaltrials.gov/study/NCT02099240). It is an Early Phase 1 osteomyelitis study (IV antibiotics vs early oral switch), terminated with 11 participants. Oxytetracycline's role is unconfirmed and the link to this disease label is weak.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. G/20.1.1/147 | Inoxtet | Capsule (oral) |
| Reg. No. G2401 (ACT 101/1965) | Terramycin Topical Ointment | Ointment (topical) |
| Reg. No. G1625 (OLD MEDICINE) | Terracortril | Ointment (topical) |

The registered forms are oral capsules and topical ointments. Route compatibility with sinus disease has not been assessed. An ear or eye indication would need a suitable topical formulation.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA. No drug interaction records were found in the queried source.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The chronic rhinosinusitis prediction is supported only by a model score (Evidence Level L5). There are no trials or publications, and mechanism and safety data are missing. The available evidence points instead to otitis externa, and that may be an existing topical use.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data, for example from DrugBank
- A targeted literature search for oxytetracycline in chronic rhinosinusitis
- Confirmation of the registered indications for Terracortril and the other products, to establish whether otitis externa is already an approved use
- Assessment of route and formulation suitability for the target site (sinus, ear or eye)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

