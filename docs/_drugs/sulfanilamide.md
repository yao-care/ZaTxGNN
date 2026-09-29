---
layout: default
title: Sulfanilamide
parent: Model Prediction Only (L5)
nav_order: 427
evidence_level: L5
indication_count: 10
---

# Sulfanilamide
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

# Sulfanilamide: From Antibacterial Use to Postmenopausal Atrophic Vaginitis

## One-Sentence Summary

Sulfanilamide is an older sulfonamide antibacterial, and no approved indication text was available in the South African registration records supplied.
The TxGNN model predicts it may be effective for **postmenopausal atrophic vaginitis**, but there are **0 clinical trials** and **0 publications** for this specific prediction.
The score is high but reflects knowledge-graph proximity rather than evidence, and the mechanistic rationale is weak.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Postmenopausal atrophic vaginitis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Sulfanilamide is a sulfonamide, and sulfonamides are known to act as PABA antagonists. They competitively inhibit bacterial dihydropteroate synthase and block folate synthesis. This is an antibacterial mechanism.

Postmenopausal atrophic vaginitis is driven by estrogen deficiency, not by a folate-dependent bacterial process. An antibacterial mechanism therefore does not address its underlying pathophysiology. The very high TxGNN score (0.999) is most likely an artefact of proximity to vaginal infection nodes in the knowledge graph.

There is no clear mechanistic link. Any benefit would have to come from treating a secondary infection, which is not the same as treating the disease itself.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

### Other Predicted Indications with Some Evidence

The model also predicted several infection-related vaginal conditions. These have historical or indirect literature, but none has controlled modern data for sulfanilamide.

| Predicted Indication | TxGNN Score | Evidence Level | Notable Literature |
|------|------|------|------|
| Trichomonal vulvovaginitis | 99.23% | L4 | [7330756](https://pubmed.ncbi.nlm.nih.gov/7330756/) (1981 review: metronidazole is the standard treatment); [13963774](https://pubmed.ncbi.nlm.nih.gov/13963774/) (1963 sulfonamide pessaries for vaginal discharge) |
| Vaginal discharge | 98.59% | L4 | [13963774](https://pubmed.ncbi.nlm.nih.gov/13963774/) (1963); [639118](https://pubmed.ncbi.nlm.nih.gov/639118/) (1978, sulfaguanidine combination); many retrieved papers concern UTI or resistance surveillance and are not relevant |
| Infective vaginitis | 91.87% | L4 | [9132982](https://pubmed.ncbi.nlm.nih.gov/9132982/) (1997 multicentre RCT in trichomoniasis comparing clotrimazole tablets, oral metronidazole and a sulfanilamide/aminacrine/allantoin suppository; the abstract supplied does not report outcomes) |

Other predictions (ulceration of vulva, vulvar neoplasm, vaginal leukoplakia, benign breast adenosis, herpetic vulvovaginitis) had no supporting evidence or only irrelevant case reports. They are graded L5 and Hold.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H990 (OM) | Achromide | Ointment | Not listed in the record |
| 33/10.2.1/0271 | Adco-ipratropium (ni201) | Vial | Not listed in the record |

The product name "Adco-ipratropium" suggests an ipratropium product. The link to sulfanilamide should be verified against the SAHPRA register before relying on this record. Approved indication text is missing for both entries.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No key warnings, contraindications or drug interaction records were available. Sulfonamide resistance is also a general concern for any antibacterial use.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is L5, with no trials, no literature, and no plausible mechanism. Estrogen deficiency, not infection, drives postmenopausal atrophic vaginitis, and the safety data needed to pass S1 screening are missing.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings and contraindications), which is currently a blocking gap
- Mechanism of action data from DrugBank
- Confirmation of the registered indications and product identity for both SAHPRA entries
- If the project wants an evidence-backed direction, re-prioritise toward infective vaginitis, trichomonal vulvovaginitis or vaginal discharge. Even there, metronidazole, clindamycin and azoles are established first-line agents, so any sulfanilamide work would be a research question only.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

