---
layout: default
title: Etonogestrel
parent: Model Prediction Only (L5)
nav_order: 218
evidence_level: L5
indication_count: 10
---

# Etonogestrel
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

# Etonogestrel: From Contraception to Amenorrhea

## One-Sentence Summary

Etonogestrel is a progestin used in hormonal contraception, marketed in South Africa as the vaginal ring Nuvaring.
The TxGNN model predicts it may be effective for **Amenorrhea**, but there are **0 clinical trials** and **0 publications** for this indication.
Amenorrhea is a known effect of the drug, so this prediction most likely reflects a side effect rather than a treatment use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Contraception (the registration record has no indication text, so this is based on the product type) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Etonogestrel is a progestin. It suppresses ovulation and thins the endometrium, and these are the effects behind its contraceptive action.

Amenorrhea is a well-known effect of etonogestrel-containing products. The high score (0.998) most likely reflects a drug-induced effect or adverse event, not a therapeutic use. Whether the drug would treat amenorrhea or simply cause it has not been resolved, and no trials or literature were supplied.

The other top predictions are mostly benign breast conditions (fibrocystic disease, adenosis, benign mammary dysplasia). A hormonal link is plausible for these, but each is prediction only. Some predictions have weak mechanistic support:
- **Breast abscess** is infectious, and a progestin has no plausible antimicrobial mechanism.
- **Fat necrosis of breast** is traumatic or ischaemic, with no clear hormonal target.
- **Acne** is a commonly reported adverse event with etonogestrel, so the direction of effect is uncertain.

## Clinical Trial Evidence

Currently no related clinical trials are registered for amenorrhea. No SANCTR or PACTR entries were identified.

Two completed trials exist for a lower-ranked prediction, **lactation disease** (rank 8, score 98.93%). They assess lactation safety of the etonogestrel implant (Nexplanon), not treatment of a lactation disorder:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03978598](https://clinicaltrials.gov/study/NCT03978598) | Phase 4 | Completed | 150 | Randomised comparison of implant placement within 24 hours of delivery vs 4-6 weeks later, with breastfeeding as the outcome |
| [NCT02657148](https://clinicaltrials.gov/study/NCT02657148) | N/A | Completed | 200 | Observational study of immediate postpartum implant placement vs standard care in opioid-dependent women, looking at contraceptive use and rapid repeat pregnancy |

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 38/34/0171 | Nuvaring | Vri (vaginal ring) | Not stated in the registration record |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5). Amenorrhea is a recognised effect of etonogestrel, so the model output probably captures an adverse effect, not a therapeutic opportunity. The only trial evidence, for lactation disease, addresses safety rather than treatment.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings and contraindications), which is a blocking gap for safety screening
- Mechanism of action data, for example from DrugBank
- Evidence on whether etonogestrel treats amenorrhea or only causes it
- Clarification of whether the breast-condition predictions carry any clinical signal, given that none has trials or literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

