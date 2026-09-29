---
layout: default
title: Testosterone Undecanoate
parent: Model Prediction Only (L5)
nav_order: 439
evidence_level: L5
indication_count: 10
---

# Testosterone Undecanoate
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

# Testosterone Undecanoate: From an Androgen Injection to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Testosterone undecanoate is an androgen (testosterone ester) marketed in South Africa as an injectable (Nebido). The TxGNN model's top-ranked prediction is **homozygous familial hypercholesterolemia (HoFH)**, but there are **0 clinical trials** and **0 publications** for it, and there is no plausible mechanistic link. This top prediction is most likely a knowledge-graph artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 98.73% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Testosterone undecanoate is a testosterone ester, so its effects come from androgen receptor signalling. Its registered indication text was not supplied in the data.

The prediction is **not** mechanistically well supported. HoFH is caused by defects in the LDL receptor pathway (*LDLR*, *APOB*, *PCSK9*, *LDLRAP1*). Testosterone undecanoate does not target this pathway. Androgens also tend to lower HDL-C, which is unfavourable in this population. The high TxGNN score most likely reflects a knowledge-graph artifact.

The other predicted indications vary in plausibility:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Androgen insensitivity syndrome | 95.72% | L3 | Plausible only for partial AIS (residual receptor function). Not expected to work in complete AIS. |
| 3 | Leydig cell hypoplasia due to LH resistance | 94.50% | L5 | Plausible. Testosterone replacement bypasses the defect. No evidence was supplied. |
| 4 | 46,XY DSD due to impaired androgen production | 93.67% | L5 | Plausible. Androgen replacement addresses the deficiency. No evidence was supplied. |
| 5–10 | Fragile X female carrier, BPES (2 entries), telecanthus, OHSS, partial trisomy/tetrasomy 5p | 90.39–92.66% | L5 | No plausible mechanistic link. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for HoFH. No trials were found in ClinicalTrials.gov or ICTRP for any of the 10 predicted indications, and no SANCTR or PACTR records were supplied.

---

## Literature Evidence

Currently no related literature available for HoFH.

Two publications exist for the second-ranked prediction (androgen insensitivity syndrome). Their designs are inferred from the titles only and are unverified:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39039878](https://pubmed.ncbi.nlm.nih.gov/39039878/) | 2024 | Cohort (inferred) | Zhonghua Er Ke Za Zhi | Self-controlled study of oral testosterone undecanoate in genetically diagnosed children with AIS, assessing efficacy and safety. |
| [8246276](https://pubmed.ncbi.nlm.nih.gov/8246276/) | 1993 | Observational (inferred) | J Sex Marital Ther | Double-blind crossover of oral testosterone undecanoate (120 mg/day) vs placebo for 4 weeks in four gonadectomized women with complete testicular feminization, looking at hormones, mood and psychosexual functioning. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. A38/21.7/0641 | Nebido 4ml vial | Injection | Not provided in the supplied data |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No drug-interaction records were found in the DrugBank query.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (HoFH) has no supporting trials or literature and no plausible mechanism, and androgens may worsen the lipid profile in this population. The prediction is best treated as a knowledge-graph artifact.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications and approved indication), which is a blocking gap for safety screening.
- Mechanism of action data (DrugBank).
- A focused literature review for the plausible androgen-deficiency indications (Leydig cell hypoplasia, 46,XY DSD, and partial AIS with subtype stratification). These are better research questions than HoFH.
- Verification of the study designs and outcomes of the two AIS publications.

---

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

