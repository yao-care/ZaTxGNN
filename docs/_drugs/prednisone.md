---
layout: default
title: Prednisone
parent: High Evidence (L1-L2)
nav_order: 385
evidence_level: L2
indication_count: 10
---

# Prednisone
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Prednisone: From General Corticosteroid Use to Alopecia Areata

## One-Sentence Summary

Prednisone is an oral corticosteroid marketed in South Africa. The registry data supplied does not state its approved indications.
The TxGNN model predicts it may be effective for **alopecia areata**.
Support is limited: **1 directly relevant Phase 3 trial** (prednisone as an add-on to methotrexate) and **20 retrieved publications**, about a dozen of which address alopecia areata treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data supplied (prednisone is generally used as an anti-inflammatory and immunosuppressive corticosteroid) |
| Predicted New Indication | Alopecia areata |
| TxGNN Prediction Score | 99.99% (model rank 122) |
| Evidence Level | L2 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Prednisone is a glucocorticoid receptor agonist. The reasoning below comes from general glucocorticoid pharmacology, not from the supplied data.

Alopecia areata is an autoimmune disease in which T-cell-mediated attack on hair follicles follows loss of the follicle's immune privilege. Glucocorticoids suppress this kind of immune activity, which makes the prediction biologically plausible. Prednisone has been tried in alopecia areata since the 1950s, and systemic corticosteroids are described in the literature as an option for severe disease.

There are two limits on this reasoning:
- Relapse after withdrawal is common. A 1976 follow-up of 18 patients found an initial response, but long-term benefit was not thought to be substantial, and numerous steroid-related side effects were recorded.
- The only recent controlled evidence tested prednisone as a low-dose add-on to methotrexate, not as monotherapy.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02037191](https://clinicaltrials.gov/study/NCT02037191) | Phase 3 | Completed | 90 | Double-blind RCT in severe alopecia areata: methotrexate vs placebo, with secondary treatment of methotrexate plus low-dose prednisone. Results are not included in the supplied data. |

The search retrieved 31 other trials. They cover lupus, prostate cancer, lymphoma and other conditions, and prednisone appears only as background therapy or in the chemotherapy regimen. None is a trial in alopecia areata, so they are not listed.

No SANCTR or PACTR registrations were identified.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36884234](https://pubmed.ncbi.nlm.nih.gov/36884234/) | 2023 | RCT | JAMA Dermatology | Two-step double-blind trial of methotrexate alone vs methotrexate plus low-dose prednisone in alopecia areata totalis or universalis, the most severe forms |
| [37467740](https://pubmed.ncbi.nlm.nih.gov/37467740/) | 2023 | Case series | Clin Exp Dermatol | Eight-case series: baricitinib plus low-dose corticosteroids gave major improvement in very severe alopecia areata |
| [26735937](https://pubmed.ncbi.nlm.nih.gov/26735937/) | 2016 | Cohort | Dermatology | Methotrexate combined with low- to moderate-dose corticosteroids in severe alopecia areata |
| [1444509](https://pubmed.ncbi.nlm.nih.gov/1444509/) | 1992 | Review | Arch Dermatol | Review of therapy, efficacy, safety and mechanism. Studies were too heterogeneous to allow meaningful comparison between drugs. |
| [791152](https://pubmed.ncbi.nlm.nih.gov/791152/) | 1976 | Case series | Arch Dermatol | Follow-up of 18 patients on alternate-day prednisone: initial response, but long-term benefit not substantial, with many side effects |
| [4571041](https://pubmed.ncbi.nlm.nih.gov/4571041/) | 1973 | Case series | Arch Dermatol | Immunologic studies and treatment with prednisone |
| [911178](https://pubmed.ncbi.nlm.nih.gov/911178/) | 1977 | Case series | Arch Dermatol | Prednisone therapy for alopecia areata |
| [20804894](https://pubmed.ncbi.nlm.nih.gov/20804894/) | 2010 | Clinical study | Ann Dermatol Venereol | Efficacy and safety of once-monthly oral prednisone pulse |
| [8996277](https://pubmed.ncbi.nlm.nih.gov/8996277/) | 1997 | Clinical study | J Am Acad Dermatol | Systemic cyclosporine plus low-dose prednisone in chronic severe alopecia areata |
| [9732014](https://pubmed.ncbi.nlm.nih.gov/9732014/) | 1998 | Clinical study | Int J Dermatol | Severe alopecia areata treated with systemic corticosteroids |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| G3004 | Be-tabs prednisone | Tablet | Not stated in registry data |
| LX/25.5.1/269 | Meticorten | Tablet | Not stated in registry data |

Both products are oral tablets.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Two points come from the retrieved literature and the evidence review:
- Systemic steroid toxicity limits long-term use. The 1976 follow-up recorded acne, obesity, lenticular opacities and hypertension.
- No drug interaction records were found in the query.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 3 RCT and a 2023 JAMA Dermatology publication support prednisone as part of a combination regimen in severe alopecia areata. The evidence does not show that prednisone alone works, and relapse and steroid toxicity are known limits. This places the evidence at L2, not L1.

**To proceed, the following is needed:**
- The published results of NCT02037191 and the 2023 RCT, to confirm the effect size of the prednisone component
- The SAHPRA Professional Information for both registered products, to obtain warnings, contraindications and approved indications
- Mechanism of action data from DrugBank
- A defined regimen (dose, duration, combination partner) and a monitoring plan for steroid adverse effects

**Other predicted indications:** Tenosynovitis is a research question at L3. Alopecia mucinosa, telogen effluvium, folliculitis decalvans and the remaining predictions are on Hold. Their evidence is limited to case reports or model prediction alone, and for alopecia mucinosa, steroid use could confound a possible lymphoma diagnosis.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

