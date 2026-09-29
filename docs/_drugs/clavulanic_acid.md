---
layout: default
title: Clavulanic Acid
parent: Model Prediction Only (L5)
nav_order: 128
evidence_level: L5
indication_count: 10
---

# Clavulanic Acid
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

# Clavulanic Acid: From Beta-Lactamase Inhibition in Bacterial Infections to Ureaplasma Urethritis

## One-Sentence Summary

Clavulanic acid is a beta-lactamase inhibitor, usually paired with amoxicillin to treat bacterial infections.
The TxGNN model predicts it may be effective for **Ureaplasma urethritis**, but there are **0 clinical trials** and **0 publications** for this indication, so the prediction rests on the model score alone.
The prediction is also mechanistically implausible, because Ureaplasma has no cell wall.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data provided; known use is as an amoxicillin partner in bacterial infections |
| Predicted New Indication | Ureaplasma urethritis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 14 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, clavulanic acid is a beta-lactamase inhibitor. It protects partner beta-lactam antibiotics, mainly amoxicillin, from being broken down by bacterial enzymes.

This mechanism does not fit Ureaplasma urethritis. Ureaplasma species have no cell wall, so beta-lactam antibiotics have no target to act on, and protecting one from beta-lactamase adds nothing. The high score (99.93%) is therefore not supported by known pharmacology. It probably reflects the drug's close association with many infection-related diseases in the knowledge graph.

The other top predictions show the same pattern. Gonococcal urethritis, uterine inflammatory disease and urogenital tuberculosis have a plausible bacterial or beta-lactamase link. Several others, such as abdominal cystic lymphangioma and celiac trunk compression syndrome, have no plausible link at all and are probably model artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered for Ureaplasma urethritis. No SANCTR or PACTR entries were provided.

## Literature Evidence

Currently no related literature available for Ureaplasma urethritis.

## Other Predicted Indications Reviewed

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Gonococcal urethritis | 99.93% | L5 | Plausible: inhibiting beta-lactamase could restore amoxicillin activity against penicillinase-producing *N. gonorrhoeae*. Resistance patterns and current guidelines limit relevance. Research question |
| 3 | Uterine inflammatory disease | 99.92% | L5 | Plausible: polymicrobial pelvic infections may involve beta-lactamase-producing bacteria. No evidence provided |
| 4 | Xanthogranulomatous pyelonephritis | 99.90% | L5 | Antibacterial use is conceptually plausible, but management is mainly surgical. No evidence provided |
| 5 | Urogenital tuberculosis | 99.89% | L4 | One case report ([PMID 26847806](https://pubmed.ncbi.nlm.nih.gov/26847806/), 2016, BMJ Case Reports) in which amoxicillin/clavulanic acid was given before tuberculous epididymo-orchitis was diagnosed. It appears to describe a diagnostic mimic, not a treatment benefit |
| 6-10 | Abdominal cystic lymphangioma, celiac trunk compression syndrome, abdominal ectopic pregnancy, lymph node palisaded myofibroblastoma, disease of uterine broad ligament | 99.79-99.80% | L5 | No plausible antibacterial mechanism. The one linked trial ([NCT04751500](https://clinicaltrials.gov/study/NCT04751500), hysteroscopic miscarriage management) does not test clavulanic acid and is not supporting evidence |

## South Africa Market Information

The registration data supplied does not include approved-indication text or manufacturers. Essential Medicines List (EML) status was not provided.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 50/20.1.2/0659 | Co-Amoxiclaz S Unimed | Suspension |
| Reg. No. 41/20.1.2/0977 | Gulf amoxy co powder for injection vial | Injection |
| Reg. No. 37/20.1.2/0674 | Augmaxcil vial 20ml | Injection |
| Reg. No. 45/7.1.5/0874 | Raviag | Tablet |
| Reg. No. 36/7.1.3/0114 | Simayla Lisinopril 20 | Tablet |

The last two products, Raviag and Simayla Lisinopril 20, do not look like amoxicillin/clavulanic acid products (the second name refers to lisinopril). These entries need checking against the SAHPRA register before use.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no trials or literature, and it conflicts with known pharmacology because Ureaplasma lacks a cell wall. Safety data from the SAHPRA package insert is also missing, which blocks safety screening.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (download and parse the PI)
- Mechanism of action data from DrugBank (DB00766)
- Verification of the registration entries that do not look like clavulanic acid products
- For a more credible follow-up, prioritise gonococcal urethritis and uterine inflammatory disease. Both need a literature search and a check against current South African treatment guidelines and local resistance data

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

