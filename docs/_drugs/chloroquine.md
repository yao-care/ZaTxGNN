---
layout: default
title: Chloroquine
parent: Model Prediction Only (L5)
nav_order: 113
evidence_level: L5
indication_count: 10
---

# Chloroquine
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

# Chloroquine: From Antimalarial Use to Rheumatoid Factor-Positive Polyarticular Juvenile Idiopathic Arthritis

## One-Sentence Summary

Chloroquine is an antimalarial. The SAHPRA registration record supplied does not state an approved indication.
The TxGNN model predicts it may be effective for **rheumatoid factor-positive polyarticular juvenile idiopathic arthritis (JIA)**, with a very high score.
However, there are **0 clinical trials** and only **2 publications** for this prediction, and neither publication tests chloroquine. The prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA record (indication text is blank) |
| Predicted New Indication | Rheumatoid factor-positive polyarticular juvenile idiopathic arthritis |
| TxGNN Prediction Score | 99.41% (model rank 3226) |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Chloroquine is an antimalarial. It is also historically used in rheumatic disease, and it may be applicable to JIA through immunomodulation.

The plausible link is suppression of lysosomal function, Toll-like receptor (TLR) signalling and inflammatory cytokines. This is the same reasoning behind antimalarial use as slow-acting antirheumatic drugs. **The retrieved records do not support this link for this specific indication.** The two publications concern leflunomide and methotrexate, not chloroquine.

The score is very high, but a high TxGNN score reflects proximity in the knowledge graph, not proof of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered. No SANCTR or PACTR records were found.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24334641](https://pubmed.ncbi.nlm.nih.gov/24334641/) | 2014 | Cohort | J Rheumatol | Long-term real-life experience with **leflunomide** in JIA. Not a chloroquine study. |
| [8627446](https://pubmed.ncbi.nlm.nih.gov/8627446/) | 1996 | Case series | J Pediatr | Accelerated nodulosis during **methotrexate** therapy in two RF-positive polyarticular JRA patients. Nodules were arrested with hydroxychloroquine (an analogue) in one patient. Not a chloroquine efficacy study. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Z/20.2.6/127 | Plasmoquine | Capsule (oral) | Not stated in the record |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Two items in the retrieved literature are relevant to a paediatric population, but they are not PI content:
- A case report of third-degree atrioventricular block during long-term chloroquine therapy ([PMID 9523387](https://pubmed.ncbi.nlm.nih.gov/9523387/)).
- A publication on chloroquine and QTc interval ([PMID 18078640](https://pubmed.ncbi.nlm.nih.gov/18078640/)).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials and no chloroquine-specific publications, so it sits at L5. The SAHPRA package insert warnings and contraindications are also missing, which blocks any safety screening.

Other predicted indications in the same pack have more support, notably knee and hand osteoarthritis (L2). It includes a completed Phase 4 chloroquine add-on trial ([NCT00805519](https://clinicaltrials.gov/study/NCT00805519)), and hydroxychloroquine trials and a meta-analysis. These would be better first candidates for review than this one.

**To proceed, the following is needed:**
- SAHPRA package insert (warnings, contraindications, paediatric dosing). This is a blocking gap.
- Mechanism of action data from DrugBank.
- Primary-source review of historical antimalarial trials in juvenile arthritis. This includes the 1991 Delagil (chloroquine) vs sulphasalazine study ([PMID 1688268](https://pubmed.ncbi.nlm.nih.gov/1688268/)) and the 1986 hydroxychloroquine trial ([PMID 3517643](https://pubmed.ncbi.nlm.nih.gov/3517643/)).
- A check on whether the registered capsule suits paediatric dosing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

