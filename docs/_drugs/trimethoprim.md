---
layout: default
title: Trimethoprim
parent: Model Prediction Only (L5)
nav_order: 457
evidence_level: L5
indication_count: 10
---

# Trimethoprim
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

# Trimethoprim: From Antibacterial Use to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Trimethoprim is an antibacterial drug that inhibits bacterial dihydrofolate reductase (DHFR). The TxGNN model predicts it may be useful for **punctate epithelial keratoconjunctivitis**, but the prediction rests on the model score alone: there are **0 clinical trials** and **0 publications** for this indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antibacterial use (SAHPRA licence records contain no indication text) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.57% (model rank 2,567) |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 9 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Based on known information, trimethoprim blocks bacterial folate synthesis. Ophthalmically it is used together with polymyxin B for bacterial conjunctivitis, so the model may be linking it to other eye infections.

The mechanistic case for this specific prediction is weak. Punctate epithelial keratoconjunctivitis is often viral (adenoviral), and trimethoprim has no antiviral activity. The high score most likely reflects graph proximity to ocular anti-infective indications rather than a real biological mechanism. No study in the Evidence Pack tests trimethoprim for this condition.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Trimethoprim has 9 SAHPRA registrations. The 5 below are the ones supplied in the Evidence Pack.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 27/20.2/0335 | Dynazole | Suspension | Not listed in the data |
| Z/20.2/209 | Trixazole | Tablet | Not listed in the data |
| K/20.2.1/335 | Spectrim | Capsule | Not listed in the data |
| W/20.2/376 | Novatrim | Suspension | Not listed in the data |
| R/20.1.1/47 | Rocephin | Injection | Not listed in the data |

- **Check the Rocephin entry.** Rocephin is normally a ceftriaxone brand, so this record may be a mapping error.
- **No ophthalmic product.** The dosage forms supplied (oral suspension, tablet, capsule, injection) include no eye-drop or topical ocular form, so a route for the predicted indication is not confirmed.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications, and the mechanism is implausible for a frequently viral condition. Registered dosage forms also include no ocular product.

Separately, the pack lists **conjunctivitis** (rank 2, score 99.17%) with a completed Phase 4 trial (NCT00581542, n=124) of Polytrim (trimethoprim/polymyxin B) versus moxifloxacin. That indication is close to existing on-label ophthalmic use rather than true repurposing. Its results were not supplied, and it is a better candidate for follow-up than this one.

**To proceed, the following is needed:**
- Confirmation of whether the adenoviral or bacterial aetiology is the target, with an evidence search specific to punctate epithelial keratoconjunctivitis
- SAHPRA Professional Information (warnings and contraindications), which is currently a blocking gap for safety screening
- Mechanism of action data (DrugBank)
- A check of whether any ophthalmic trimethoprim product is registered in South Africa
- Verification of the Rocephin registration record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

