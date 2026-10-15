---
layout: default
title: Framycetin
parent: Model Prediction Only (L5)
nav_order: 242
evidence_level: L5
indication_count: 10
---

# Framycetin
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

# Framycetin: From Its Registered Topical and Rectal Uses to Sclerosing Cholangitis

## One-Sentence Summary

Framycetin is a poorly absorbed aminoglycoside antibiotic, registered in South Africa in an ear/eye preparation (Sofradex) and a rectal suppository (Proctosedyl).
The TxGNN model predicts it may be effective for **sclerosing cholangitis** (top-ranked prediction), but **no clinical trials and no publications** currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the registration records have no indication text) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, framycetin is an aminoglycoside antibiotic that is poorly absorbed, so it acts mainly where it is applied (topically or in the gut lumen). Its antibacterial activity against Gram-negative organisms is well established, but the specific original indication could not be confirmed from the registration records.

A theoretical link exists through the gut-liver axis. Changing the intestinal microbiota with oral, non-absorbable antibiotics has been explored in primary sclerosing cholangitis (for example with vancomycin). Aminoglycosides are not an established approach in this condition.

The high TxGNN score is a computational prediction. It has no supporting clinical trials or literature. Systemic toxicity (nephrotoxicity and ototoxicity) also limits parenteral use.

### Other Predicted Indications

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|---|---|---|---|---|
| 2 | Urinary tract infection | 99.42% | L5 | Mechanistically plausible (Gram-negative activity), but no framycetin data. Better-characterised first-line agents exist. |
| 3 | Congenital prothrombin deficiency | 99.41% | L5 | No plausible mechanism. Likely a network artifact. |
| 4 | Gonococcal urethritis | 99.28% | L5 | Biologically plausible, but ceftriaxone is the established standard of care. |
| 5 | Ureaplasma urethritis | 99.28% | L5 | Aminoglycosides have poor activity against ureaplasmas. Weak support. |
| 6 | Uterine inflammatory disease | 99.18% | L5 | Would need anaerobic cover in combination. Weak link. |
| 7 | Xanthogranulomatous pyelonephritis | 99.18% | L5 | Nephrotoxicity is a major concern in a diseased kidney. |
| 8 | Bronchitis | 98.95% | L4 | Only a 1956 historical report. Most bronchitis is viral. |
| 9 | Genital herpes | 98.66% | L5 | Viral disease with no antiviral activity from framycetin. |
| 10 | Vitamin deficiency disorder | 96.79% | L5 | No therapeutic rationale. Oral aminoglycosides may cause rather than treat deficiency. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is available for sclerosing cholangitis. For the lower-ranked prediction of bronchitis, one historical report exists:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [13316238](https://pubmed.ncbi.nlm.nih.gov/13316238/) | 1956 | Historical clinical report (likely uncontrolled) | Bruxelles Medical | Trial therapy with framycetin in pneumology. No abstract is available, and it is anecdotal evidence only. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H1482 (Act 101 of 1965) | Sofradex 8 ml | Ear/eye drops (recorded as "Eed") | Not recorded |
| E529 (Act 101 of 1965) | Proctosedyl Suppositories | Suppository | Not recorded |

Both registrations are valid single-ingredient entries. Essential Medicines List (EML) status could not be determined from the data compiled for this report.

## Safety Considerations

Safety data from the product labels were not available for this report. Aminoglycosides as a class carry a risk of nephrotoxicity and ototoxicity when systemically absorbed. No drug-drug interaction records were found, and no disease contraindications were recorded in the knowledge graph.

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There are no trials or publications for sclerosing cholangitis, and the mechanistic link is only theoretical. Systemic toxicity also limits use.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications and approved indications), which is a blocking gap for safety screening
- Detailed mechanism of action data from DrugBank
- Preclinical or pilot evidence of gut-microbiota-directed benefit in sclerosing cholangitis, and a comparison with agents already explored (such as oral vancomycin)
- Assessment of route compatibility, since the registered forms are topical and rectal rather than oral
- If the team wishes to pursue another indication, urinary tract infection is the most mechanistically plausible, but it would need to be shown to offer an advantage over established first-line agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

