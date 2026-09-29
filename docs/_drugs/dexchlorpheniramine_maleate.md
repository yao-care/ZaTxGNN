---
layout: default
title: Dexchlorpheniramine Maleate
parent: Model Prediction Only (L5)
nav_order: 167
evidence_level: L5
indication_count: 10
---

# Dexchlorpheniramine Maleate
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

# Dexchlorpheniramine Maleate: Predicted New Indication – Acute Intermittent Porphyria

## One-Sentence Summary

Dexchlorpheniramine maleate is a first-generation H1 antihistamine that is marketed in South Africa. The TxGNN model predicts it may be effective for **Acute Intermittent Porphyria**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Acute intermittent porphyria |
| TxGNN Prediction Score | 99.12% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Dexchlorpheniramine is a first-generation H1 receptor antagonist. Its established role is blocking histamine-mediated allergic responses.

No plausible mechanistic link to acute intermittent porphyria has been identified. This is a disorder of heme biosynthesis, and H1 blockade has no known role in that pathway. The high score of 0.991 (model rank 4402) appears to be a knowledge-graph artefact rather than a biologically grounded signal.

The same applies to the third-ranked prediction, "porphyria", which is a broad parent term of the same disease. It is probably driven by the same graph neighbourhood.

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov, ICTRP, SANCTR or PACTR) for this indication.

## Literature Evidence

Currently no related literature available for this indication.

## Other Predictions Worth Noting

Among the top 10 predictions, only two have any literature. Neither supports the top-ranked indication.

- **Allergic urticaria (rank 6, score 96.96%, evidence level L3):** The mechanistic link is strong and direct, because histamine-mediated wheal and flare is the core mechanism of urticaria. Two retrieved papers are histamine-challenge pharmacodynamic studies, which use a surrogate endpoint rather than clinical efficacy. They are [PMID 39265704](https://pubmed.ncbi.nlm.nih.gov/39265704/) (2024, a phase I comparison of bilastine and parenteral dexchlorpheniramine) and [PMID 29723372](https://pubmed.ncbi.nlm.nih.gov/29723372/) (2018, wheal and flare suppression by H1 antihistamines). This is likely an existing class indication rather than true repurposing, so the current labelling should be confirmed before treating it as a new candidate.
- **Schizophrenia (rank 4, score 97.17%, evidence level L4):** The single retrieved paper, [PMID 19220286](https://pubmed.ncbi.nlm.nih.gov/19220286/) (2009), is a human experimental study of H1 blockade and sensorimotor performance. It does not study patients with schizophrenia. Sedation and cognitive impairment from first-generation antihistamines are more likely to be a liability than a benefit.
- **Remaining predictions:** The other seven have no trials or literature. They include nephrogenic syndrome of inappropriate antidiuresis, several myopia entries and rare congenital or metabolic syndromes. No plausible mechanistic link was identified for any of them.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 48/21.5.4/0075 | Betadexamine Tablets | Tablet (oral) |
| Reg. No. A40/21.5.4/0623 | Betadexamine | Syrup |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no clinical trials or literature and no plausible mechanistic link. It is a model output only (L5). Safety data from the SAHPRA package insert has not yet been obtained, which blocks progression to safety screening.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (download and parse the PI PDF)
- Mechanism of action data (for example, from DrugBank)
- The approved indication text for both registrations, to confirm the original indication
- For allergic urticaria, confirmation of current labelling to determine whether it is an existing indication, followed by a check for clinical efficacy trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

