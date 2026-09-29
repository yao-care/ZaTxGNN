---
layout: default
title: Diphenylpyraline
parent: Model Prediction Only (L5)
nav_order: 185
evidence_level: L5
indication_count: 10
---

# Diphenylpyraline
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

# Diphenylpyraline: From First-Generation Antihistamine (Original Indication Not Recorded) to Allergic Urticaria

## One-Sentence Summary

Diphenylpyraline is a first-generation H1 antihistamine, and its original indication is not recorded in the data supplied.
The TxGNN model predicts it may be effective for **allergic urticaria**, but there are currently **0 clinical trials** and **0 publications** for this indication, so the prediction rests on the model score and mechanistic plausibility alone.
Rhinitis is the only predicted indication with any clinical signal (4 historical publications, 1954-1977).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records supplied |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, diphenylpyraline is a first-generation H1 antihistamine. H1 receptor blockade is a well-established way to reduce histamine-mediated symptoms, and mechanistically it may be applicable to allergic urticaria.

Allergic urticaria is driven largely by histamine released from mast cells. Blocking H1 receptors would therefore be expected to reduce itch and wheals.

The 99.61% score is a model output only. Neither a clinical trial nor a publication supports diphenylpyraline in urticaria in the data supplied. Because the drug's original indication is also unrecorded, it is unclear how far urticaria departs from its existing use.

The other nine predictions (ranks 2-10) are weaker. Some are plausible only as symptom relief (nasopharyngitis, acute laryngopharyngitis, atopic dermatitis). Others have no clear mechanistic link (rosacea conjunctivitis, anorectal stricture). Cold urticaria is mechanistically plausible but has no evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for allergic urticaria.

The only predicted indication with published clinical work is **rhinitis** (rank 7, TxGNN score 96.58%, evidence level L3). These publications are old and were classified from titles and abstracts only:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14039](https://pubmed.ncbi.nlm.nih.gov/14039/) | 1977 | Clinical study (double-blind, placebo-controlled per abstract) | J Int Med Res | 63 patients on diphenylpyraline vs 57 on placebo for allergic and vasomotor rhinitis. Diphenylpyraline was better on all symptoms, with significant differences for mucus discharge and red eyes. |
| [13294977](https://pubmed.ncbi.nlm.nih.gov/13294977/) | 1956 | Clinical evaluation | J Allergy | Clinical evaluation of diphenylpyraline (no abstract available). |
| [13125198](https://pubmed.ncbi.nlm.nih.gov/13125198/) | 1954 | Clinical evaluation | Ann Allergy | Evaluation in ragweed pollinosis (no abstract available). |
| [13683344](https://pubmed.ncbi.nlm.nih.gov/13683344/) | 1961 | Clinical study | Svensk Lakartidningen | Long-acting formulation (Durettes) in hay fever (no abstract available). |

Rhinitis may overlap with the drug's original use. Its label and indication history should be verified before it is treated as repurposing.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 27/10.1/0529 | Dynalex | Syrup | Not provided |
| Reg. No. N/10.1/98 | Theophen Compound Elixir | Syrup | Not provided |
| Reg. No. W/10.1/0194 | Actophlem | Syrup | Not provided |

All three registered products are oral syrups. Essential Medicines List (EML) status was not included in the data supplied.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Allergic urticaria is supported only by a model prediction (L5), with no trials or publications. Safety information from the SAHPRA package insert is missing, so the candidate cannot proceed to safety screening.

**To proceed, the following is needed:**
- The SAHPRA package insert for each of the 3 registered products, to obtain warnings, contraindications and approved indications
- Mechanism of action data (for example, from DrugBank)
- Confirmation of the drug's original indication, to judge whether rhinitis or urticaria is truly a new use
- Any clinical evidence in urticaria (trials, case series, guideline mentions) before the decision is revisited
- Optionally, a separate research-question track for rhinitis (L3), given the 1977 double-blind study and the older clinical reports
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

