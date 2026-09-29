---
layout: default
title: Hydrocortisone Acetate
parent: Model Prediction Only (L5)
nav_order: 253
evidence_level: L5
indication_count: 10
---

# Hydrocortisone Acetate
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

# Hydrocortisone Acetate: From Topical Corticosteroid Use to Alopecia Areata

## One-Sentence Summary

Hydrocortisone acetate is a low-potency corticosteroid, and in South Africa it is registered only as topical creams. The TxGNN model predicts it may be effective for **alopecia areata**. Support is thin: **1 Phase 3 trial** in which it was only the comparator, and **2 old publications** (a 1973 case series and a 1979 review). This is a research question, not a treatment recommendation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA records supplied (both registered products are creams) |
| Predicted New Indication | Alopecia areata |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 (nominally L1, downgraded because the trial evidence is indirect) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Based on known information, hydrocortisone acetate is a glucocorticoid receptor agonist. Its anti-inflammatory and immunosuppressive effects are established for corticosteroids as a class, and could mechanistically apply to alopecia areata. This rationale is at class level and has not been shown for this specific drug.

Alopecia areata is a T-cell-mediated autoimmune attack on hair follicles, and corticosteroids are commonly used in it. However, hydrocortisone is a low-potency topical steroid, so clinical efficacy is doubtful. The one controlled trial found used it as the weaker comparator against clobetasol propionate, a high-potency steroid.

The other nine predictions are much weaker. Telogen effluvium, alopecia mucinosa, folliculitis decalvans, several rare genetic hair disorders, seborrheic keratosis and steroid-sensitive nephrotic syndrome all have no trials or literature. Alopecia areata is the only prediction with any supporting evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | Completed | 41 | Randomised trial in children with alopecia areata comparing clobetasol propionate 0.05% cream with hydrocortisone 1% cream. Hydrocortisone was the comparator, so the trial shows the drug has been tested in this disease but does not show that it works. |

No SANCTR or PACTR registrations were identified.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4755919](https://pubmed.ncbi.nlm.nih.gov/4755919/) | 1973 | Case series (uncontrolled) | Przeglad dermatologiczny | Intralesional injections of hydrocortisone acetate suspension for severe alopecia areata. No abstract is available, and an uncontrolled series cannot show efficacy. |
| [153470](https://pubmed.ncbi.nlm.nih.gov/153470/) | 1979 | Review | MMW, Munchener medizinische Wochenschrift | General review of topical skin therapy. It uses hydrocortisone acetate only as a potency reference for a newer steroid and is not specific to alopecia areata. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| G2022 | Biocort (stx) | Cream | Not listed in the record |
| 45/13.4.1/0568 | Fucidin h | Cream | Not listed in the record |

Both registrations are topical creams. No injectable or intralesional product is registered, although the 1973 case series used an injected suspension. Essential Medicines List status was not available in the data.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only controlled evidence uses hydrocortisone as a low-potency comparator, and the remaining literature is a decades-old uncontrolled series and a general review. The registered cream is a weak steroid, and SAHPRA safety data have not yet been reviewed. This is a hypothesis worth studying, not a candidate for use.

**To proceed, the following is needed:**
- Retrieve and review the SAHPRA package inserts, which are currently missing and block safety screening
- Obtain mechanism of action data from DrugBank
- Check the full NCT01453686 results for the hydrocortisone arm's outcomes
- Establish route compatibility, since the registered products are creams only and the historical use was intralesional
- Compare against higher-potency steroids already registered in South Africa for alopecia areata, to see whether hydrocortisone adds anything

*These are research predictions only and do not constitute medical advice. Any repurposing candidate requires clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

