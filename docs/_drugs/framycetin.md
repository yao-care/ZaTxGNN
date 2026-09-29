---
layout: default
title: Framycetin
parent: Model Prediction Only (L5)
nav_order: 240
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

# Framycetin: From Topical Aminoglycoside Antibacterial to Sclerosing Cholangitis

## One-Sentence Summary

Framycetin is a poorly absorbed aminoglycoside antibiotic. It is registered in South Africa in two combination products (an "Eed" form and a suppository), but the retrieved data do not state their approved indications.
The TxGNN model predicts it may be effective for **sclerosing cholangitis**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the retrieved SAHPRA data (registered as an antibacterial aminoglycoside) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, framycetin is an aminoglycoside antibacterial that is poorly absorbed from the gut and skin. Mechanistically it may be applicable to sclerosing cholangitis.

Primary sclerosing cholangitis is thought to involve the gut-liver axis, meaning gut dysbiosis and bacterial translocation. A gut-restricted antibacterial could, in theory, act on this pathway. The idea is biologically coherent, but the high TxGNN score reflects graph similarity, not clinical findings. No trials or literature were retrieved to test it.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H1482 (ACT 101 1965) | Sofradex 8ml | Eed (as listed) | Not listed in retrieved data |
| E529 (ACT 101 1965) | Proctosedyl Suppositories | Suppository | Not listed in retrieved data |

## Safety Considerations

- **Drug Interactions**: The DDI query returned no records (not found in the database). This is not evidence that no interactions exist.
- **Class concerns (from the prediction rationale)**: Systemic aminoglycoside use carries nephrotoxicity and ototoxicity risk. Oral aminoglycosides may reduce vitamin K-producing gut flora, which could worsen coagulopathy.

Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is based on a model score alone (L5), with no registered trials or publications for sclerosing cholangitis. The gut-liver axis rationale is plausible, but it is unproven for framycetin. The SAHPRA safety data needed for screening are also missing.

Among the lower-ranked predictions, the only drug-specific signal is a 1956 report on framycetin in pneumology (PMID [13316238](https://pubmed.ncbi.nlm.nih.gov/13316238/), relevant to bronchitis). Its design is unverified and the mechanistic rationale is weak. Several other predictions (congenital prothrombin deficiency, vitamin deficiency disorder, genital herpes) have no plausible mechanism and are likely knowledge-graph artefacts.

**To proceed, the following is needed:**
- SAHPRA package inserts (warnings, contraindications, approved indications) for both registered products. This is a blocking gap.
- Mechanism of action data from DrugBank.
- A targeted literature search on oral or gut-restricted antibiotics in primary sclerosing cholangitis.
- Route compatibility assessment: the registered forms (an "Eed" form and a suppository) may not match the oral route the hypothesis would require.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

