---
layout: default
title: Ethinylestradiol
parent: Moderate Evidence (L3-L4)
nav_order: 217
evidence_level: L4
indication_count: 1
---

# Ethinylestradiol
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

# Ethinylestradiol: From Hormonal Contraception to Elevated Plasma Zinc

## One-Sentence Summary

Ethinylestradiol is a synthetic estrogen, widely used in oral contraceptive products. The supplied literature deals with contraceptives, and the registered indication text is not in the dataset.
The TxGNN model predicts a link to **elevated plasma zinc**, but this is a laboratory finding rather than a treatable disease.
There are **0 clinical trials** and **2 publications** (both from the 1970s), and neither shows a treatment benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA data supplied (literature context suggests oral contraception) |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for this drug, so the prediction cannot be checked against known pharmacology.

The high score probably reflects a real pharmacological association. Estrogens are known to alter circulating trace-element levels, for example by raising ceruloplasmin and copper and shifting zinc distribution. The knowledge graph may have picked up this link.

An association is not a therapeutic rationale. "Elevated plasma zinc" is a laboratory abnormality, and raising plasma zinc is not an obvious treatment goal. The retrieved papers describe the drug's effect on mineral levels, not a benefit from treating this condition. The prediction should therefore be read as a graph association, not a repurposing opportunity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [736629](https://pubmed.ncbi.nlm.nih.gov/736629/) | 1978 | Observational (human) | Archives of Gynecology | In women taking oral contraceptives, plasma and endometrial copper were significantly raised, while zinc stayed reasonably constant. It does not show that zinc rises. |
| [961877](https://pubmed.ncbi.nlm.nih.gov/961877/) | 1976 | Preclinical (rat) | American Journal of Physiology | Mestranol, a prodrug of ethinylestradiol, depressed plasma zinc in rats, the opposite direction to the prediction. It is only indirect evidence for ethinylestradiol. |

## South Africa Market Information

Five of the 20 registrations are shown. Approved indication text was not supplied for any of them, and Essential Medicines List (EML) status is not in the dataset.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 44/18.8/0397 | Ynez | Fct |
| Reg. No. 50/21.8.2/0590 | Contrezin | Tablet |
| Reg. No. 47/21.8.2/0141 | Drasira | Tablet |
| Reg. No. 34/20.2.2/0244 | Adco-dermed | Sha |
| Reg. No. 49/18.8/0711 | Merdeza | Tablet |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but the only evidence is two indirect studies from the 1970s. One shows no change in zinc and the other shows a fall in zinc. The target is a laboratory finding, not a disease with a therapeutic goal. The evidence is at the model-prediction and preclinical level (L4), and the safety review cannot start without the package insert.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, to allow a mechanistic-link analysis
- A clinical case for why raising plasma zinc is a valid therapeutic goal, or a decision to drop this candidate
- Modern human data on ethinylestradiol and plasma zinc levels

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

