---
layout: default
title: Nomegestrol Acetate
parent: Model Prediction Only (L5)
nav_order: 343
evidence_level: L5
indication_count: 10
---

# Nomegestrol Acetate
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

# Nomegestrol Acetate: From Progestogen Hormonal Therapy to Candidiasis

## One-Sentence Summary

Nomegestrol acetate is a progestogen (a progesterone receptor agonist) and is marketed in South Africa as Zoely, a combined tablet with estradiol.
The TxGNN model predicts it may be effective for **candidiasis**, but **0 clinical trials** and **0 publications** currently support this direction.
This is a model-only prediction, and hormonal exposure is generally linked to a higher risk of vulvovaginal candidiasis, not a therapeutic effect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA registration data (the registered product is a combined hormonal tablet, Zoely 2.5mg/1.5mg) |
| Predicted New Indication | Candidiasis |
| TxGNN Prediction Score | 98.78% (rank 5560) |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, nomegestrol acetate is a progestogen with anti-gonadotropic activity. It is used in a combined estrogen-progestogen product.

No established mechanistic link to candidiasis was identified. The prediction most likely reflects proximity between nodes in the TxGNN knowledge graph, not biology. Hormonal exposure is generally associated with an increased risk of vulvovaginal candidiasis, so the direction of effect is questionable.

The other top-ranked predictions (antithrombin deficiency type 2, heparin cofactor 2 deficiency, factor 5 excess with thrombosis, plasma cell myeloma, gout, rheumatoid arthritis and others) also lack retrieved trials or literature and have no plausible mechanism. The thrombosis-related predictions run against the known safety profile of hormonal products.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 45/18.8/0064 | Zoely 2.5mg/1.5mg | Tablet (oral) | Not stated in the registration record |

Essential Medicines List (EML) inclusion status could not be confirmed from the available data.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Context from retrieved evidence for a different predicted indication (thrombotic disease): the literature addresses venous thromboembolism (VTE) risk during oral estrogen-progestogen therapy, including the nomegestrol acetate/estradiol combination. This is a class safety concern for hormonal products, and it argues against repurposing for any thrombophilic condition.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials or publications. The known association between hormonal exposure and candidiasis runs opposite to a therapeutic effect.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence of antifungal or anti-candidal benefit, or a documented mechanism
- Mechanism of action (MOA) data from DrugBank
- The SAHPRA package insert (warnings and contraindications), which is currently a blocking gap for safety screening
- Route and formulation compatibility assessment, since only an oral combined tablet is registered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

