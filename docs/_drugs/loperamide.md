---
layout: default
title: Loperamide
parent: Model Prediction Only (L5)
nav_order: 298
evidence_level: L5
indication_count: 10
---

# Loperamide
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

# Loperamide: From Diarrhoea to Acute Contagious Conjunctivitis

## One-Sentence Summary

Loperamide is an anti-diarrhoeal medicine that slows gut motility. The TxGNN model predicts it may be effective for **acute contagious conjunctivitis** with a very high score, but **0 clinical trials** and **0 publications** support this. The prediction is a computational signal only, and no plausible mechanism has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diarrhoea (from the prediction rationale; the SAHPRA registration records list no indication text) |
| Predicted New Indication | Acute contagious conjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 5 entries (4 unique registration numbers; Norimode appears twice under Y/11.9/0073) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Loperamide is generally described as a peripherally restricted mu-opioid receptor agonist. It acts on the gut to reduce motility and secretion, which is why it is used for diarrhoea.

For acute contagious conjunctivitis, no supported mechanistic link was found. Opioid receptor signalling on the ocular surface is not an established treatment target for conjunctivitis. Ocular exposure after oral dosing is also not expected. The high score most likely reflects the model's knowledge graph placing several eye diseases close together, not a pharmacological reason.

The same pattern applies to the other top predictions:

- **Conjunctivitis subtypes:** The pseudomembranous, chronic follicular, parasitic, serous and folliculosis subtypes, plus conjunctivitis itself, share near-identical scores. This points to a shared graph artefact. Angelucci syndrome also has no link to loperamide's pharmacology.
- **Amebic dysentery:** Loperamide may reduce stool frequency, but it has no antiamebic activity. Antimotility agents are generally cautioned against in invasive dysentery because slowed transit may worsen disease or mask progression. This is a safety concern, not a benefit.
- **Gastroduodenitis:** There is only weak, indirect plausibility, because loperamide acts on the gut. Slowing motility is not a recognised approach for this upper-GI inflammatory condition.

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov and ICTRP searches returned none; SANCTR and PACTR identifiers are not available in the source data).

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. Y/11.9/0073 | Norimode | Tablet |
| Reg. No. V/11.9/0213 | Gastron | Tablet |
| Reg. No. 31/11.9.2/0402 | Imodium Plus | Tablet |
| Reg. No. 28/11.9/0649 | Loperastat | Syrup |

Approved indication text and Essential Medicines List (EML) status are not available in the source data. All registered forms are oral (tablet and syrup); no ophthalmic formulation is registered.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no trials, no literature and no plausible mechanism. The registered products are oral only, so they would not reach the ocular surface. For amebic dysentery, loperamide could cause harm.

**To proceed, the following is needed:**
- SAHPRA Professional Information (PI) warnings and contraindications, which are currently missing and block any safety screening
- Detailed mechanism of action data (MOA)
- A credible mechanistic rationale, and preclinical or clinical evidence, for any ocular use
- A route-compatibility assessment, since only oral products are registered

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

