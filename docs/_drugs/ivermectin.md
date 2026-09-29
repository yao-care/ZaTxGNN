---
layout: default
title: Ivermectin
parent: Model Prediction Only (L5)
nav_order: 279
evidence_level: L5
indication_count: 10
---

# Ivermectin
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

# Ivermectin: From Antiparasitic Use to Vulvovaginal Candidiasis

## One-Sentence Summary

Ivermectin is an antiparasitic drug, and in South Africa it is registered as a cream (Soolantra).
The TxGNN model predicts it may be effective for **vulvovaginal candidiasis**, but **no clinical trials and no publications** currently support this direction.
The prediction rests on the knowledge-graph score alone (Evidence Level L5).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied registration record (ivermectin is an antiparasitic agent) |
| Predicted New Indication | Vulvovaginal candidiasis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the supplied data. Ivermectin is known to act on glutamate-gated chloride channels in invertebrates, which is how it kills parasites. Fungi such as *Candida* do not have these channels. No antifungal mechanism is therefore supported.

The high score most likely reflects closeness in the knowledge graph. Ivermectin sits near other candidiasis and vaginitis nodes, and this is not a drug-specific finding. The prediction should be treated as a hypothesis to test, not a treatment option.

The same pattern appears in the other top-ranked predictions:

| Rank | Predicted Indication | Score | Evidence Level | Note |
|------|------|------|------|------|
| 2 | Esophageal candidiasis | 99.73% | L5 | The one linked paper is a case report of strongyloidiasis, not candidiasis |
| 3 | Anogenital HPV infection | 99.48% | L5 | No data; antiviral link is speculative |
| 4 | Vulvovaginitis | 99.36% | L5 | No data |
| 5 | Congenital candidiasis | 99.25% | L5 | The one linked paper is a case series of crusted scabies; neonatal and paediatric safety would need separate review |
| 6 | Neonatal candidiasis | 99.25% | L5 | Same score as rank 5, probably a shared graph artefact |
| 7 | *Candida glabrata* | 99.25% | L5 | A pathogen, not a clinical indication |
| 8 | Postmenopausal atrophic vaginitis | 99.18% | L5 | Driven by estrogen deficiency, no plausible link |
| 9 | Invasive candidiasis | 99.16% | L5 | High-stakes condition with effective approved therapies |
| 10 | Vulvitis | 98.98% | L5 | No data |

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov, ICTRP, SANCTR or PACTR) for vulvovaginal candidiasis.

## Literature Evidence

Currently no related literature available for vulvovaginal candidiasis.

Two papers were linked to other predicted indications, and neither supports an antifungal effect:
- [35835488](https://pubmed.ncbi.nlm.nih.gov/35835488/) (2022, case report, BMJ Case Reports): disseminated strongyloidiasis after prolonged corticosteroid treatment. This is an approved antiparasitic setting.
- [10098288](https://pubmed.ncbi.nlm.nih.gov/10098288/) (1999, case report/series, Australasian Journal of Dermatology): oral ivermectin for crusted scabies in two immunocompromised children, one of whom had chronic mucocutaneous candidiasis. Ivermectin was used against scabies, not candidiasis.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 49/13.12/0906 | Soolantra | Cream | Not stated in the supplied record |

The registered product is a cream. Whether any route or formulation would suit vulvovaginal use has not been assessed.

## Safety Considerations

- **Drug Interactions**: The interaction query returned no records (0 interactions found). This is not confirmation that none exist.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials, no supporting literature, and no known antifungal mechanism. Effective approved treatments already exist for candidiasis.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Laboratory evidence of antifungal activity against *Candida* at clinically achievable exposures
- A route and formulation compatibility assessment
- Registered trials or published studies in vulvovaginal candidiasis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

