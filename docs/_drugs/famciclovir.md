---
layout: default
title: Famciclovir
parent: Model Prediction Only (L5)
nav_order: 223
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Famciclovir: predicted new indication Post-infectious neuralgia (evidence level L5). Approved use: Herpes zoster"
---

# Famciclovir
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

# Famciclovir: From Herpes Zoster to Post-Infectious Neuralgia

## One-Sentence Summary

Famciclovir is an oral antiviral originally used to treat herpes zoster (shingles).
The TxGNN model predicts it may be useful for **post-infectious neuralgia**, which in this context is closest to postherpetic neuralgia, the nerve pain that can follow shingles.
The evidence is thin: **1 registered clinical trial** is linked to this prediction, and it tests oxycodone rather than famciclovir. **No publications** were identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Herpes zoster (from the knowledge graph; the SAHPRA registration data compiled for this report contain no indication text) |
| Predicted New Indication | Post-infectious neuralgia |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 (model prediction only; no study directly tests famciclovir for this condition) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Famciclovir is a prodrug of penciclovir. After activation by viral thymidine kinase, penciclovir inhibits herpesvirus DNA polymerase. Detailed mechanism-of-action data were not available for this report, so this description rests on general knowledge of the drug class.

Postherpetic neuralgia is the most common complication of herpes zoster. It is persistent pain or abnormal sensation lasting more than 90 days after the shingles episode has resolved. A plausible indirect link is that treating acute zoster early with an antiviral may reduce the risk or severity of later neuralgia. This would be prevention of a complication, not a new mechanism of action.

This link is a hypothesis, not an established finding. The only trial linked to this prediction studies a different drug, oxycodone, as the preventive strategy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | Not applicable | Unknown | 140 | Tests early oxycodone during acute herpes zoster to prevent postherpetic neuralgia. Famciclovir is not the studied intervention, so this is indirect, contextual evidence only. |

No SANCTR or PACTR identifiers were found in the data compiled for this report.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 45/20.2.8/1157 | Macleods Famciclovir Tablets 125 Mg | Film-coated tablet (Fct) | Not stated in the data compiled |

This is the only registration, and it is a valid single-ingredient product. Essential Medicines List status could not be determined from the data compiled.

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** kidney disease and pyoureter. These come from drug-disease links in the TxGNN knowledge graph, not from the SAHPRA-approved label, so they should be checked against the Professional Information (PI).
- **Drug Interactions:** The interaction check completed and returned **84 potential interactions**, none graded for severity. Examples include calcitriol, doxycycline, metformin, glimepiride, morphine, omeprazole, pantoprazole, prednisone, simvastatin and vancomycin. Each should be reviewed against current interaction references before any use.

The SAHPRA label warnings and contraindications were not available. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but no study tests famciclovir for this indication. The single linked trial evaluates oxycodone, and no literature was found. The mechanistic link, early antiviral treatment lowering the risk of neuralgia, is plausible but unproven.

Among the other TxGNN predictions for famciclovir, only chickenpox has meaningful evidence, including a completed Phase 3 trial of famciclovir versus aciclovir in herpes zoster. That indication overlaps with the approved varicella-zoster use, so it is an adjacent indication rather than a true repurposing.

**To proceed, the following is needed:**
- The SAHPRA Professional Information (PI) for the registered product, covering approved indications, warnings and contraindications
- Direct evidence for famciclovir (or other antivirals) in preventing or treating postherpetic neuralgia, such as a systematic review of existing zoster trials that report neuralgia outcomes
- A prospective study or registry in South African zoster patients if the review supports the idea
- Detailed mechanism-of-action data and a review of the 84 flagged drug interactions, with renal function considerations given the kidney disease flag
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

