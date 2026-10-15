---
layout: default
title: Oseltamivir
parent: Model Prediction Only (L5)
nav_order: 359
evidence_level: L5
indication_count: 10
---

# Oseltamivir
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

# Oseltamivir: From Influenza to Pyelonephritis

## One-Sentence Summary

Oseltamivir is an oral antiviral (neuraminidase inhibitor) originally used to treat influenza.
The TxGNN model predicts it may be effective for **pyelonephritis**, but there are **0 clinical trials** and only **1 loosely related publication** (a review on influenza in pregnancy that does not address pyelonephritis). This prediction is best treated as a computational artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Influenza (from the TxGNN knowledge graph; the South African registration entries do not state an indication) |
| Predicted New Indication | Pyelonephritis |
| TxGNN Prediction Score | 97.85% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, oseltamivir is a viral neuraminidase inhibitor. Its efficacy in influenza is established, but it is not expected to act on the organisms that cause pyelonephritis.

Pyelonephritis is typically a bacterial infection of the upper urinary tract. Oseltamivir has no known antibacterial activity, so no plausible mechanistic link exists. The only retrieved paper concerns influenza in pregnancy and does not mention pyelonephritis. The high TxGNN score (97.85%) most likely reflects graph proximity, such as shared infection-related annotations, rather than real biological or clinical relevance.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for pyelonephritis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26033556](https://pubmed.ncbi.nlm.nih.gov/26033556/) | 2015 | Review | Presse Médicale | Influenza in pregnant women: higher risk of pneumonia and hospitalisation. Does not address pyelonephritis, so relevance is indirect at best. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 54/20.2.8/0687 | Oseltamivir Adco 30 Mg | Capsule | Not stated in the data compiled for this report |
| 56/20.2.8/1086 | Ozetir | Suspension | Not stated in the data compiled for this report |

Both registrations are valid single-ingredient products. Oral capsule and suspension forms are available.

---

## Safety Considerations

- **Knowledge-graph contraindication signal**: delirium. This comes from drug-disease graph edges, not from label text. The literature compiled for other predicted indications also includes a case report of oseltamivir-associated delirium (PMID 21108186).
- **Drug Interactions**: 66 potential interactions were identified, with severity levels not classified. Examples include pantoprazole, vancomycin, prednisone, simvastatin, rosuvastatin, metformin, clarithromycin, morphine, ondansetron and metronidazole. Interaction severity should be verified against the product label or a clinical interaction reference.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). There are no trials, no relevant literature and no plausible mechanism for a neuraminidase inhibitor in a bacterial urinary tract infection. Pursuing it is not justified.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking neuraminidase inhibition to pyelonephritis (none currently exists)
- Any preclinical or clinical signal for pyelonephritis
- The SAHPRA Professional Information (warnings, contraindications and approved indication text) and DrugBank mechanism-of-action data

**Note on other predictions for oseltamivir:** Among the lower-ranked predictions, **pneumonia** has substantially stronger support. It has a completed Phase 3 influenza trial (NCT00707941, 1,190 participants), a Cochrane review of neuraminidase inhibitors (PMID 24718923) and an L1 rating. It is best viewed as an extension of the approved influenza indication, with guardrails limiting use to confirmed or suspected influenza. Oseltamivir has shown no benefit against COVID-19 pneumonia. **Streptococcal pneumonia** (L3) is a research question only, as an adjunct to antibiotics in post-influenza bacterial pneumonia. If this report is intended to support a practical repurposing decision, these indications merit a separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

