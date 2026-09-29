---
layout: default
title: Cycloserine
parent: Model Prediction Only (L5)
nav_order: 156
evidence_level: L5
indication_count: 10
---

# Cycloserine
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

# Cycloserine: From Drug-Resistant Tuberculosis to Irritable Bowel Syndrome

## One-Sentence Summary

Cycloserine is a second-line (reserve) antibiotic used for drug-resistant tuberculosis. The TxGNN model predicts it may be effective for **irritable bowel syndrome**, but **no clinical trials and no publications** currently support this prediction. It rests on the knowledge-graph score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Drug-resistant tuberculosis (from the Evidence Pack's narrative; no approved indication text is recorded in the SAHPRA data) |
| Predicted New Indication | Irritable bowel syndrome |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Cycloserine is known as a cell-wall synthesis inhibitor (alanine racemase and D-Ala-D-Ala ligase). Its efficacy in drug-resistant tuberculosis is established. Mechanistically, no link to irritable bowel syndrome (IBS) has been established.

The only speculative route is D-cycloserine's action as a partial agonist at the NMDA glycine site, which might influence gut-brain signalling. No supporting data were provided. The high score reflects patterns in the knowledge graph, not demonstrated biology or clinical results. Antibacterial action against tuberculosis has no clear bearing on a functional bowel disorder.

## Clinical Trial Evidence

Currently no related clinical trials registered for irritable bowel syndrome.

## Literature Evidence

Currently no related literature available for irritable bowel syndrome.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 37/34/0243 | Nutrineal PD4 with 1.1% amino acids 2.5L | Infusion | Not stated in the source data |

The only linked registration is a peritoneal dialysis amino-acid solution, which is not a typical cycloserine product. This looks like an ingredient-mapping artefact. Verify the actual cycloserine product registrations on the SAHPRA register before relying on the "Marketed" status.

## Safety Considerations

- **Neuropsychiatric effects**: A 2022 case report (PMID 36712725) describes cycloserine-induced insomnia and psychosis in multidrug-resistant TB. Cycloserine is generally associated with CNS toxicity, which is a concern for long-term use in a non-life-threatening condition such as IBS.

Please refer to the SAHPRA-approved Professional Information (PI) for full safety information (warnings, contraindications, interactions). Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials, no literature and no established mechanism, so it is L5 (model prediction only). Cycloserine's CNS toxicity and reserve-agent status make systemic use for IBS unfavourable without supporting evidence.

Other predicted indications (e.g. insomnia, conjunctivitis) also remain at Hold. Their retrieved studies are indirect or point to safety concerns.

**To proceed, the following is needed:**
- The SAHPRA Professional Information (PI) for a genuine cycloserine product, including warnings and contraindications
- Mechanism of action data (e.g. from DrugBank) and a plausible biological link to IBS
- Preclinical or early clinical evidence in IBS
- Confirmation of the correct SAHPRA registrations and available dosage forms (oral vs the registered infusion product)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

