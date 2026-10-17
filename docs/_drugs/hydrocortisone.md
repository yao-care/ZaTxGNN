---
layout: default
title: Hydrocortisone
parent: Model Prediction Only (L5)
nav_order: 254
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Hydrocortisone: predicted new indication Alopecia areata (evidence level L5). Approved use: Adrenocortical insufficiency / Addison disease, autoimmune disease…"
monitor_inn: "Hydrocortisone"
predicted_indications: ["alopecia areata", "alopecia mucinosa", "telogen effluvium", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions", "alopecia universalis onychodystrophy vitiligo"]
---

# Hydrocortisone
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

# Hydrocortisone: From Autoimmune and Adrenal Conditions to Alopecia Areata

## One-Sentence Summary

Hydrocortisone is a corticosteroid, originally used for conditions such as adrenocortical insufficiency, autoimmune disease, Crohn disease and tinea pedis.
The TxGNN model predicts it may be effective for **Alopecia Areata**,
but only **1 clinical trial** (in which hydrocortisone was the weak comparator) and **1 randomised trial publication** currently bear on this direction, so the evidence is limited.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Adrenocortical insufficiency / Addison disease, autoimmune disease, inflammatory bowel disease (Crohn disease), tinea pedis and others (taken from the knowledge-graph indication list, as SAHPRA indication text was not available) |
| Predicted New Indication | Alopecia areata |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 per the automated scoring rule, but the underlying trial was a comparator-arm study, so the practical level is closer to L2 (see below) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 12 |
| Recommended Decision | Hold |

**Note on evidence level:** The automated rule assigned L1, but the single Phase 3 trial used hydrocortisone 1% cream as the low-potency comparator against clobetasol 0.05%. It does not demonstrate hydrocortisone's own efficacy, and the trial was small (n=41). A conservative reading is therefore L2 at best.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, hydrocortisone is a glucocorticoid with well-established anti-inflammatory and immunosuppressive effects, and its efficacy in autoimmune and inflammatory conditions is proven.

Alopecia areata is an autoimmune, T-cell-mediated attack on hair follicles. Corticosteroids suppress local immune activity and inflammatory cytokines, so a plausible mechanism exists, and this is consistent with the prediction. Historical reports from 1955 to 1973 describe hair regrowth after intralesional hydrocortisone injections, but these are uncontrolled and outdated.

The key caveat is potency. In the only randomised trial, hydrocortisone 1% was the weaker comparator against clobetasol 0.05%, which shows relative inferiority to a potent steroid rather than hydrocortisone's own benefit. Potent topical or intralesional steroids are generally used for this condition rather than hydrocortisone.

Other predicted indications (ranks 2 to 10) have little or no supporting evidence. Telogen effluvium and atrichia with papular lesions lack a clear anti-inflammatory rationale. Steroid-sensitive nephrotic syndrome is already treated with glucocorticoids (usually prednisolone), and the single linked paper is not about hydrocortisone treatment.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | Completed | 41 | Randomised trial of clobetasol propionate 0.05% cream versus hydrocortisone 1% cream in children with alopecia areata (2002-2003). Hydrocortisone served as the active low-potency comparator. |

No SANCTR or PACTR identifiers were available in the data compiled for this report.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24226568](https://pubmed.ncbi.nlm.nih.gov/24226568/) | 2014 | RCT | JAMA Dermatology | Clobetasol 0.05% versus hydrocortisone 1% for alopecia areata in children |
| [13368875](https://pubmed.ncbi.nlm.nih.gov/13368875/) | 1956 | Historical case series | Medical Times | Treatment of alopecia areata with cortisone, hydrocortisone and analogues |
| [13610145](https://pubmed.ncbi.nlm.nih.gov/13610145/) | 1958 | Historical clinical report | Der Hautarzt | Hair growth after intracutaneous hydrocortisone injection (German) |
| [15692503](https://pubmed.ncbi.nlm.nih.gov/15692503/) | 2005 | Case report | J Am Acad Dermatol | Four cases of congenital alopecia areata treated with minoxidil and topical agents |
| [13525930](https://pubmed.ncbi.nlm.nih.gov/13525930/) | 1958 | Review | J Med Soc New Jersey | Overview of alopecia areata and common scalp problems |

Most remaining retrieved publications are historical intralesional injection reports without abstracts, or off-target papers (animal studies, a veterinary case, a survey), and are not listed.

## South Africa Market Information

All 12 registrations are single-ingredient, valid, and mostly topical or otic/rectal products. Approved indication text was not available in the data compiled for this report.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H/13.4.1/109 | Locoid | Ointment | Not available |
| 35/13.4.1/0384 | Vari-hydrocortisone | Cream | Not available |
| R/13.4.1/202 | Skincalm | Cream | Not available |
| 33/16.2/0024 | Ciprobay HC Otic Drops | Drops | Not available |
| 35/13.4.1/0392 | Elozart | Cream | Not available |

Seven further registrations exist (Neoderm, Daktacort, Fucidin H, Proctosedyl Suppositories, Viocort, Terracortril, Otosporin). Essential Medicines List status was not available in the data compiled. No oral or injectable hydrocortisone product appears among these registrations, so intralesional use would need separate confirmation of product availability.

## Safety Considerations

- **Disease-level cautions (knowledge graph, not label text):** Hydrocortisone is flagged in relation to hypertension, epilepsy, gastric ulcer, kidney disease, liver disease, gallbladder disease, hyperglycaemia, viral skin infections (anogenital HPV infection, common wart, measles, herpes simplex keratitis) and pituitary deficiency states.
- **Drug Interactions:** 100 interactions were identified. Notable ones include a **Major** interaction with adalimumab, and **Moderate** interactions with zidovudine, isotretinoin, acarbose, acebutolol, acetazolamide, ketorolac, ibuprofen, nifedipine, ethinylestradiol, aldesleukin, alemtuzumab and certain live or inactivated vaccines. Salbutamol and formoterol interactions are Minor.

Please refer to the SAHPRA-approved Professional Information (PI) for formal warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible, but the only controlled trial used hydrocortisone 1% as the weak comparator and does not show its own efficacy. Other evidence is small, historical and uncontrolled, and more potent corticosteroids are the practical standard. The other nine predicted indications have little or no hydrocortisone-specific evidence.

**To proceed, the following is needed:**
- Review of the full results of NCT01453686 to quantify the hydrocortisone arm's response
- Detailed mechanism of action data
- SAHPRA Professional Information warnings and contraindications for the relevant products
- Comparison against potent corticosteroids and current alopecia areata standards of care
- Confirmation of product availability and route (topical versus intralesional) in South Africa
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

