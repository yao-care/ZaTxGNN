---
layout: default
title: Tocopherol
parent: Moderate Evidence (L3-L4)
nav_order: 448
evidence_level: L4
indication_count: 10
---

# Tocopherol
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Tocopherol: From Vitamin E (Fat-Soluble Vitamin) to Sclerosing Cholangitis

## One-Sentence Summary

Tocopherol is vitamin E, a fat-soluble antioxidant vitamin. No approved indication is recorded in the SAHPRA data supplied.
The TxGNN model predicts it may be relevant to **sclerosing cholangitis**.
Evidence is very thin: **1 clinical trial** and **1 publication**, and neither tests tocopherol as a treatment for the disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA data supplied (indication text is empty for all registrations) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 98.84% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 (2 distinct products; one entry is duplicated) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available. Tocopherol is generally known as a lipid-soluble antioxidant that limits lipid peroxidation.

The plausible link is nutritional rather than disease-modifying. Chronic cholestasis impairs absorption of fat-soluble vitamins (A, D, E, K), so tocopherol deficiency is likely in cholestatic liver disease. The one supporting paper notes that oxygen-derived free radicals have been suggested to contribute to chronic liver damage. This supports **correcting a deficiency**, not treating sclerosing cholangitis itself.

The model's high score most likely reflects knowledge-graph proximity between vitamin E and cholestatic conditions. It is not a signal of proven efficacy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05582447](https://clinicaltrials.gov/study/NCT05582447) | N/A | Active, not recruiting | 40 | Pilot study of red blood cell osmotic fragility in children with cholestatic liver disease (including primary sclerosing cholangitis). It is non-interventional and does not test tocopherol, so it gives no efficacy signal. |

No SANCTR or PACTR registrations were identified.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10735930](https://pubmed.ncbi.nlm.nih.gov/10735930/) | 2000 | Cross-sectional/observational | Aliment Pharmacol Ther | Plasma antioxidant levels in chronic cholestatic liver diseases. Cholestasis causes malabsorption of fat-soluble vitamins and free-radical scavengers. It is descriptive and shows no treatment benefit. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| G2667 (ACT 101/1965) | Gericomplex | Capsule (oral) | Not recorded |
| 41/10.2.1/0849 | Spiriva respimat inhaler 60 doses | Inhaler | Not recorded |

- Gericomplex (G2667) appears twice in the source data. It is shown once here.
- The Spiriva Respimat entry is an inhaler and is unlikely to contain tocopherol as an active ingredient. It looks like a possible mapping artifact and should be verified against the SAHPRA register.
- Essential Medicines List (EML) status was not supplied.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence rests on model prediction and a plausible deficiency link. The only trial does not test tocopherol, and the only paper is observational. Safety data from the SAHPRA package insert are missing, which blocks progression to safety screening.

Other predicted indications exist in the Evidence Pack. Rheumatoid arthritis has the most direct human evidence (a Phase 2/3 alpha-tocopherol trial, NCT06915701, currently recruiting). It could be evaluated separately.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (blocking)
- Mechanism of action data (e.g. from DrugBank)
- Verification of which SAHPRA registrations actually contain tocopherol, including the Spiriva entry
- Interventional trials of tocopherol in sclerosing cholangitis, or a decision to frame the use as deficiency correction only
- Route compatibility and similarity-to-original-indication assessments (currently pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

