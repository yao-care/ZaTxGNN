---
layout: default
title: Lorazepam
parent: Model Prediction Only (L5)
nav_order: 300
evidence_level: L5
indication_count: 10
---

# Lorazepam
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

# Lorazepam: From Benzodiazepine Anxiolytic to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Lorazepam is a benzodiazepine that enhances GABA-A receptor signalling. Its registration records here do not list an approved indication, so its usual role as an anxiolytic and sedative comes from general pharmacology. The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, but there are **0 clinical trials** and **0 publications** supporting this prediction. It rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the registration records (benzodiazepine; anxiolytic and sedative use per general pharmacology) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. From general pharmacology, lorazepam is a positive allosteric modulator of the GABA-A receptor. This produces sedation, anxiolysis and anticonvulsant effects.

There is no plausible direct link between this mechanism and treating a tumour of the trigeminal nerve. Nothing suggests an antineoplastic effect. The very high score (99.87%) most likely reflects ontology or graph-neighbourhood artefacts rather than a real therapeutic signal. At most, lorazepam could give symptomatic relief in tumour patients, such as anxiety control or seizure control. That would be supportive care, not treatment of the neoplasm.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Lorazepam is marketed in South Africa under 3 SAHPRA registrations. The registration records do not include approved indication text.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| R/2.6/319 | Ativan SL | Slt (as recorded) |
| D/2.6/128 | Ativan | Tablet |
| X/2.6/82 | Ativan | Tablet |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature and no plausible mechanistic link. It is a model-only signal (L5) that most likely reflects graph artefacts. For context, the same evidence pack ranks insomnia second (L3, Research Question), but that use is closer to an established use than to true repurposing. Its guardrails are tolerance, dependence, next-day impairment and risk in elderly patients.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for any safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence that links lorazepam to trigeminal nerve neoplasm, beyond supportive care
- Confirmation of the approved indications for the three registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

