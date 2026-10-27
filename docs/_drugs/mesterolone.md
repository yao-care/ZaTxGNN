---
layout: default
title: Mesterolone
parent: Model Prediction Only (L5)
nav_order: 315
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Mesterolone: predicted new indication Gout (evidence level L5). Approved use: Not listed in the SAHPRA registration data compiled for this report"
monitor_inn: "Mesterolone"
predicted_indications: ["gout", "type 1 diabetes mellitus", "allergic asthma", "brain small vessel disease 1 with or without ocular anomalies", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "diabetic nephropathy", "intrinsic asthma", "autoimmune oophoritis", "Jeune syndrome situs inversus", "heart disease"]
---

# Mesterolone
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

## Mesterolone: From Male Androgen Deficiency to Gout
{: .text-alpha }

## One-Sentence Summary

Mesterolone is an oral androgen (a dihydrotestosterone derivative) registered in South Africa as a single-ingredient tablet (Proviron).
The TxGNN model predicts it may be effective for **gout**, but there are **0 clinical trials** and **0 publications** supporting this direction.
This is a model-based prediction only, and the available data suggest the prediction is mechanistically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the SAHPRA registration data compiled for this report |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 98.20% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Mesterolone is known to be an oral androgen derived from dihydrotestosterone (DHT) and is used in male hypogonadism. Its original indication is not recorded in the SAHPRA registration data.

For gout, no plausible mechanistic link has been identified. Mesterolone has no established role in urate metabolism or gouty inflammation, and androgens are generally associated with higher serum urate, so a benefit is unlikely. The high TxGNN score (98.20%) reflects graph-based proximity only and should not be read as clinical support.

**Other predicted indications (all Hold, no supporting evidence):**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Type 1 diabetes mellitus | 96.54% | L5 | The only linked paper (PMID 15025811) concerns diagnosing pituitary apoplexy and does not address mesterolone or type 1 diabetes |
| 3 | Allergic asthma | 96.32% | L5 | Only a weak, indirect immunomodulatory rationale for androgens |
| 4 | Brain small vessel disease 1 (with or without ocular anomalies) | 96.21% | L5 | COL4A1-related monogenic disorder; no mechanistic link |
| 5 | Autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome | 96.17% | L5 | Ultra-rare COL4A1-related syndrome; no evidence |
| 6 | Diabetic nephropathy | 96.04% | L5 | Androgenic effects on lipids and cardiovascular risk raise concern |
| 7 | Intrinsic asthma | 96.03% | L5 | Same weak rationale as allergic asthma |
| 8 | Autoimmune oophoritis | 95.99% | L5 | Virilization risk in women and possible further ovarian suppression |
| 9 | Jeune syndrome situs inversus | 94.80% | L5 | Ciliopathy; no plausible link |
| 10 | Heart disease | 94.74% | L4 | Only evidence is an adverse-effect signal (see below) |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature is available for gout, the top predicted indication. Literature linked to lower-ranked predictions is listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18808528](https://pubmed.ncbi.nlm.nih.gov/18808528/) | 2008 | Preclinical (adverse effect study) | Int J Exp Pathol | In transgenic mice with a human lipaemic phenotype, the anabolic-androgenic steroid mesterolone worsened cardiac remodelling and lipoprotein profile; aerobic exercise training attenuated these effects. This is a safety signal, not evidence of benefit. |
| [15025811](https://pubmed.ncbi.nlm.nih.gov/15025811/) | 2004 | Review | Ann Clin Biochem | Case-based discussion of the biochemistry department's role in diagnosing pituitary apoplexy in a patient with insulin-dependent diabetes. It does not address mesterolone, so it is not relevant evidence. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| B/21.7/137 | Proviron | Tablet (oral) | Not available in the data compiled for this report |

Essential Medicines List (EML) status was not available in the data compiled for this report.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Points drawn from the evidence compiled for this report:
- **Cardiovascular and lipid concern:** A preclinical study (PMID 18808528) reported that mesterolone worsened cardiac remodelling and lipoprotein profile.
- **Risk in women:** Exogenous androgens carry a virilization risk and may further suppress ovarian function.
- **Diabetic kidney disease:** Androgenic effects on lipids and cardiovascular risk raise concern in this population.
- **Gout:** Androgens are generally associated with higher serum urate, which could worsen rather than improve gout.

No drug-drug interaction records were found in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for gout rests on a graph-based score alone, with no clinical trials or publications. Pharmacological reasoning points the other way, since androgens tend to raise serum urate. None of the ten predicted indications has supportive clinical evidence, and the only relevant study signals an adverse cardiac and lipid effect.

**To proceed, the following is needed:**
- The SAHPRA Professional Information (package insert) warnings and contraindications, which are currently missing and block safety screening
- The approved indication text from the SAHPRA registration
- Mechanism of action data (for example, from DrugBank)
- Any clinical or mechanistic evidence for mesterolone in urate metabolism or gout; without it, repurposing is not supported
- Confirmation of the route of administration and its suitability for any new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

