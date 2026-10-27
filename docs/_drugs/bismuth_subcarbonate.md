---
layout: default
title: Bismuth Subcarbonate
parent: Model Prediction Only (L5)
nav_order: 72
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Bismuth Subcarbonate: predicted new indication Insomnia (evidence level L5). Approved use: Not stated in the registration data compiled for this report"
monitor_inn: "Bismuth subcarbonate"
predicted_indications: ["insomnia (disease)", "enterocolitis (disease)", "irritable bowel syndrome", "neurocirculatory asthenia", "acute intermittent porphyria", "sleep disorder, initiating and maintaining sleep", "adult-onset myasthenia gravis", "myasthenia gravis with thymus hyperplasia", "neonatal myasthenia gravis", "autoimmune disease of peripheral nervous system"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Bismuth Subcarbonate: From an Unspecified Original Indication to Insomnia
{: .text-alpha }

## One-Sentence Summary

Bismuth subcarbonate is a poorly absorbed gastrointestinal agent. The registration data compiled for this report do not state its approved indication.
The TxGNN model predicts it may be effective for **insomnia**, but there are **0 clinical trials** and **0 publications** supporting this direction.
This is a model-only prediction with no mechanistic rationale, and the evidence is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data compiled for this report |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Bismuth subcarbonate is a poorly absorbed gastrointestinal agent. No central nervous system or sleep-regulating activity is known for it.

The registration record lists no approved indication, so the relationship between the original and new indications cannot be verified. The high TxGNN score (0.994) is a graph-based prediction. It is likely driven by network proximity to unrelated drugs or targets rather than a real biological link. **No credible mechanistic link to insomnia is established.**

### Other Predictions from the Model

None of the other top-ranked predictions has any supporting trials or literature. All are L5 with a recommendation of Hold.

| Rank | Predicted Indication | Score | Assessment |
|------|------|------|------|
| 2 | Enterocolitis | 96.94% | Biologically plausible: bismuth salts have antimicrobial, mucosal-protective and antisecretory properties. It probably overlaps with the drug's existing GI use rather than being true repurposing. |
| 3 | Irritable bowel syndrome | 96.80% | Plausible GI rationale (luminal antimicrobial effect, possible effect on secretion and diarrhoea). A targeted literature search (e.g. bismuth for IBS-D or diarrhoea) is needed. |
| 4 | Neurocirculatory asthenia | 95.49% | No identifiable mechanistic link. |
| 5 | Acute intermittent porphyria | 93.33% | No mechanistic link. Heavy-metal effects on haem synthesis would argue for caution rather than benefit. |
| 6 | Sleep disorder (initiating and maintaining sleep) | 92.81% | Essentially the same phenotype as insomnia, with the same lack of rationale. |
| 7 | Adult-onset myasthenia gravis | 92.00% | No immunomodulatory or neuromuscular activity is known. |
| 8 | Myasthenia gravis with thymus hyperplasia | 91.76% | Likely clusters with other myasthenia entries in the knowledge graph. |
| 9 | Neonatal myasthenia gravis | 91.34% | No relevant activity is known, and use in neonates would raise additional safety concerns. |
| 10 | Autoimmune disease of peripheral nervous system | 91.31% | No known mechanism. Bismuth compounds have been associated with neurotoxicity (encephalopathy) at high systemic exposure. |

Among all ten, **enterocolitis and irritable bowel syndrome** are the only ones with a plausible rationale, because they are gastrointestinal. They would be the more sensible candidates to investigate first.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| E/11.4.1/683 | Pawmag | Powder | Not stated in the registration data |

The data compiled for this report do not include Essential Medicines List (EML) status.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The following general observations come from the model's rationale. They are not label information:
- Bismuth compounds have historically been associated with neurotoxicity (encephalopathy) at high systemic exposure.
- Heavy-metal effects on haem synthesis argue for caution in porphyria.
- Use in neonates would raise additional safety concerns.

No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The insomnia prediction rests only on a graph-based score. There are no trials, no literature, and no known CNS or sleep-related mechanism. It also lacks safety documentation and a documented original indication, so it should not advance.

**To proceed, the following is needed:**
- The SAHPRA package insert (Professional Information), covering the approved indication, warnings and contraindications
- Mechanism of action data for bismuth subcarbonate
- A targeted literature search, prioritising GI indications (enterocolitis, IBS-D or diarrhoea), where a plausible rationale exists
- Assessment of route and formulation compatibility, which is currently pending (the only registered product is an oral powder)
- Evidence of any link to insomnia, which would be required before this prediction is reconsidered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

