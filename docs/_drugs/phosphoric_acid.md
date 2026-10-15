---
layout: default
title: Phosphoric Acid
parent: Model Prediction Only (L5)
nav_order: 376
evidence_level: L5
indication_count: 10
---

# Phosphoric Acid
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

# Phosphoric Acid: From an Unspecified Original Indication to Osteoarthritis

## One-Sentence Summary

Phosphoric acid is a simple inorganic acid. In the data compiled for this report, its SAHPRA-registered products carry no stated indication, and the compound is mainly used as an excipient, acidulant and pH adjuster.
The TxGNN model predicts it may be effective for **osteoarthritis**, with a score of 98.2%.
However, there are **no clinical trials** and **no relevant supporting publications**, so this prediction is most likely a knowledge-graph artifact rather than a real therapeutic signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text in the SAHPRA registrations) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 98.21% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Phosphoric acid is a simple inorganic acid used mainly as an excipient, acidulant and pH adjuster. It is not an active drug with a defined pharmacological action on joint tissue.

No credible mechanistic link to osteoarthritis has been established. The high TxGNN score is most likely driven by graph proximity to phosphate- and phosphoric-acid-related nodes, not by a real effect on cartilage or synovium. The same pattern appears for the other top predictions (rheumatoid arthritis, gout and several rare liver diseases), several of which share an identical score. This suggests a structural artifact of the model.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The four publications retrieved for osteoarthritis do not test phosphoric acid as a treatment for the condition:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41344594](https://pubmed.ncbi.nlm.nih.gov/41344594/) | 2026 | Preclinical | Acta Biomaterialia | Kneading-responsive hyaluronic acid hydrogel for on-demand local anaesthetic release in osteoarthritis pain; not related to phosphoric acid as a therapy |
| [38723559](https://pubmed.ncbi.nlm.nih.gov/38723559/) | 2024 | Preclinical | J Pharm Biomed Anal | Metabolomic study of a herbal pair in osteoarthritic rats; no link to phosphoric acid therapy |
| [6373974](https://pubmed.ncbi.nlm.nih.gov/6373974/) | 1983 | Basic research | Nihon Seikeigeka Gakkai Zasshi | Lysosomal enzymes in synovial tissue from rheumatoid and non-rheumatoid joints |
| [8098576](https://pubmed.ncbi.nlm.nih.gov/8098576/) | 1993 | Pharmacokinetic | Aktuelle Traumatologie | Ciprofloxacin concentrations in bone of patients with coxarthrosis; phosphoric acid not studied as treatment |

For the second-ranked prediction (rheumatoid arthritis), the retrieved literature is mostly analytical chemistry papers, where phosphoric acid appears only as a mobile-phase or buffer component. No relevant efficacy evidence was found.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| N/24/83 | Sabax Neonatalyte 10% Gluc 200ml | Infusion | Not stated |
| B/2.9/1251 | Sabax Pethidine Ampoule 1ml | Injection | Not stated |

Both registrations are valid, single-component entries. Phosphoric acid in these products most likely serves as an excipient or pH adjuster rather than as the active ingredient. Essential Medicines List status could not be determined from the data compiled for this report.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). There are no clinical trials, no relevant efficacy literature and no plausible mechanism. Phosphoric acid is an excipient and pH adjuster in the registered products, and the high score appears to be a graph-based artifact. Safety review also cannot proceed because package insert data are missing.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (currently a blocking gap)
- Confirmation of whether phosphoric acid is an active ingredient or only an excipient in the registered products
- Mechanism of action data (for example from DrugBank)
- A credible pharmacological rationale and preclinical evidence before any clinical consideration for osteoarthritis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

