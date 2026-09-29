---
layout: default
title: Bismuth Subcarbonate
parent: Model Prediction Only (L5)
nav_order: 71
evidence_level: L5
indication_count: 10
---

# Bismuth Subcarbonate
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

# Bismuth Subcarbonate: From Gastrointestinal Mucosal Protection to Insomnia

## One-Sentence Summary

Bismuth subcarbonate is a poorly absorbed, gut-local mucosal protectant. It is registered in South Africa as the product Pawmag, but no approved indication text is recorded for it.
The TxGNN model predicts it may be effective for **insomnia**, with a very high score, but **0 clinical trials** and **0 publications** support this prediction.
This is a model-only signal with no known sleep-related pharmacology, so the prediction should not be acted on.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (the SAHPRA licence has no approved indication text) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Bismuth subcarbonate is a bismuth salt that acts locally in the gut. Bismuth salts are generally described as having mucosal-protective, antisecretory and antimicrobial effects, and systemic absorption is minimal.

**The insomnia prediction is not mechanistically supported.** No plausible link has been identified between a gut-local agent with minimal systemic exposure and CNS or sleep pharmacology. The high score (0.994) is a knowledge-graph output only. Its raw rank of 3,357 is not corroborated by any trial or publication. A closely related prediction, "sleep disorder, initiating and maintaining sleep" (score 92.81%), has the same weakness.

**Other predictions are more biologically sensible, though weakly evidenced.**

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Enterocolitis | 96.94% | L4 | Biologically plausible. The only evidence is a 1980 veterinary report in dogs (see note below), with no human data. |
| 3 | Irritable bowel syndrome | 96.80% | L5 | Indirect plausibility only. Gut-local activity could plausibly affect diarrhoea and microbiota-related inflammation, but no studies were found. |

The remaining predictions (neurocirculatory asthenia, acute intermittent porphyria, and several myasthenia gravis and peripheral autoimmune neuropathy terms) have no identifiable mechanistic basis. Several appear to result from clustering among related nodes in the graph. For myasthenia gravis, bismuth toxicity is itself neurological, which argues against benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for insomnia.

For context, the only publication retrieved for any prediction concerns enterocolitis (rank 2):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6247810](https://pubmed.ncbi.nlm.nih.gov/6247810/) | 1980 | Veterinary clinical report | Veterinary Medicine, Small Animal Clinician | "Amforol" reported as effective for enteritis in dogs. No abstract was available, and the role of bismuth subcarbonate in that product is unverified. This is indirect animal evidence only. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| E/11.4.1/683 | Pawmag | Powder | Not recorded in the available data |

Essential Medicines List (EML) status could not be confirmed from the available data.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No drug interaction records were found in the queried source.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The insomnia prediction rests only on a knowledge-graph score. There are no trials or publications, and the drug has no known CNS or sleep pharmacology. Safety information from the SAHPRA package insert is also missing, which blocks progression to safety screening.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications and approved indication), to unblock safety screening
- Mechanism of action data (for example, via DrugBank)
- If any repurposing work is pursued, redirect it to the gastrointestinal predictions (enterocolitis, irritable bowel syndrome). Start with a human literature and trial search, since current evidence is limited to one veterinary report.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

