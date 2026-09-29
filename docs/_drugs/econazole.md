---
layout: default
title: Econazole
parent: Model Prediction Only (L5)
nav_order: 207
evidence_level: L5
indication_count: 10
---

# Econazole
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

# Econazole: From Topical Antifungal Use to Ectothrix Infectious Disease

## One-Sentence Summary

Econazole is an imidazole antifungal, marketed in South Africa as a vaginal cream and a cream (the SAHPRA records supplied contain no approved-indication text).
The TxGNN model predicts it may be effective for **ectothrix infectious disease** (dermatophyte infection on the outside of the hair shaft).
Currently there are **0 clinical trials** and **0 publications** supporting this specific prediction, so it is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied SAHPRA data (product forms and drug class suggest topical antifungal use) |
| Predicted New Indication | Ectothrix infectious disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, econazole is an imidazole antifungal that inhibits fungal lanosterol 14-alpha-demethylase (CYP51). This blocks ergosterol synthesis and damages the fungal cell membrane.

Ectothrix infections are caused by dermatophytes such as *Microsporum* and *Trichophyton*, which are fungi that econazole's mechanism can plausibly act against. This is the likely basis for the high TxGNN score. The link is mechanistic only, and no trial or publication in the input tests econazole in this condition.

There is also a practical limit. Fungi that invade hair, and deeper dermatophyte infections, are often hard to reach with topical products. Guidelines usually favour systemic therapy for scalp involvement. Whether econazole cream reaches the infected hair sheath at effective concentrations has not been shown here. Route compatibility has not yet been assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. R/18.6/179 | Gyno pevaryl depot | Vaginal cream | Not provided in the supplied data |
| Reg. No. Q/13.4.1/0220 | Pevisone | Cream | Not provided in the supplied data |

Both registered products are topical. No systemic econazole product appears in the data. Pevisone's name suggests a combination with a corticosteroid, but the supplied data does not confirm this. Check the PI.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a plausible antifungal mechanism alone. There are no trials, no literature, no verified original indication and no safety data. This is Evidence Level L5 (model prediction only), and the topical route may not suit hair-shaft infection.

**To proceed, the following is needed:**
- SAHPRA package insert (PI) warnings, contraindications and approved indications, which are a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Clinical or in vitro evidence of econazole activity against ectothrix dermatophytes, and evidence of topical penetration into the hair sheath
- Review of route compatibility (topical vs the systemic therapy usually needed)

**Note on other predictions in this pack:**
- **Vulvovaginal candidiasis** and **vulvovaginitis** (candidal) have the strongest support: L2, with several econazole comparative studies, including a double-blind study against clotrimazole ([7820892](https://pubmed.ncbi.nlm.nih.gov/7820892/)) and a South African study ([7403993](https://pubmed.ncbi.nlm.nih.gov/7403993/)). These are most likely existing labelled uses rather than true repurposing. Recommended decision: Proceed with Guardrails, after confirming the SAHPRA label status and considering azole resistance in non-albicans *Candida*.
- **Superficial mycosis** (L4) is probably also an existing labelled use. Its literature is mostly reviews of other azoles.
- **Majocchi granuloma, endothrix infection, tinea profunda, dermatophytosis of scalp or beard, acne** and **postmenopausal atrophic vaginitis** have no supporting econazole evidence (L4–L5, Hold). For atrophic vaginitis the antifungal mechanism has no clear therapeutic link, and the score is probably a knowledge-graph artefact.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

