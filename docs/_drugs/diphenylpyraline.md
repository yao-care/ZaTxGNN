---
layout: default
title: Diphenylpyraline
parent: Model Prediction Only (L5)
nav_order: 187
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Diphenylpyraline: predicted new indication Allergic urticaria (evidence level L5). Approved use: Allergic rhinitis"
monitor_inn: "Diphenylpyraline"
predicted_indications: ["acute laryngopharyngitis", "nasal cavity disease", "nasopharyngitis", "rosacea conjunctivitis", "recalcitrant atopic dermatitis", "IgE responsiveness, atopic", "anorectal stricture"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Diphenylpyraline: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Diphenylpyraline is a first-generation H1 antihistamine, originally used for allergic and vasomotor rhinitis, the common cold, allergic conjunctivitis and urticaria.
The TxGNN model predicts it may be effective for **allergic urticaria**, but **no clinical trials and no publications** were found for this specific prediction. Urticaria is already among the drug's original indications, so this is not a true repurposing candidate.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis (the SAHPRA licence records contain no approved indication text; original indications come from the TxGNN knowledge graph) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, diphenylpyraline is a first-generation H1 antihistamine with anticholinergic activity. Histamine released from mast cells drives the wheal-and-flare response in allergic urticaria, so H1 blockade is mechanistically plausible.

Urticaria and angioedema are already listed among the drug's original indications, so the prediction largely restates a known use. The same applies to several other predictions: acute laryngopharyngitis, nasal cavity disease, nasopharyngitis and rhinitis overlap with the original rhinitis, pharyngitis and common cold indications. For these, any benefit is symptomatic (drying of secretions) and does not treat underlying infection.

Cold urticaria is a plausible histamine-mediated condition. However, current practice prefers second-generation antihistamines for better tolerability.

Other predictions have weak or no mechanistic support:
- **Rosacea conjunctivitis:** driven mainly by meibomian gland dysfunction and inflammation rather than histamine.
- **Recalcitrant atopic dermatitis:** itch is only partly histamine-driven, so benefit is unlikely.
- **IgE responsiveness, atopic:** a phenotype rather than a treatable disease; antihistamines act downstream of IgE.
- **Anorectal stricture:** no plausible link; likely a knowledge-graph artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered for allergic urticaria.

## Literature Evidence

No publications were found for allergic urticaria. The only literature in the data relates to the lower-ranked prediction **rhinitis** (score 96.58%, evidence level L4), which is an already-approved use:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14039](https://pubmed.ncbi.nlm.nih.gov/14039/) | 1977 | Clinical study (double-blind per abstract; 63 on drug, 57 on placebo) | J Int Med Res | Better effect than placebo on all symptoms in allergic and vasomotor rhinitis; statistically significant for mucus discharge and eye redness |
| [13294977](https://pubmed.ncbi.nlm.nih.gov/13294977/) | 1956 | Historical clinical evaluation | J Allergy | General clinical evaluation of diphenylpyraline (no abstract available) |
| [13683344](https://pubmed.ncbi.nlm.nih.gov/13683344/) | 1961 | Historical clinical study | Svenska Lakartidningen | Long-acting formulation in hay fever (no abstract available) |
| [13125198](https://pubmed.ncbi.nlm.nih.gov/13125198/) | 1954 | Historical clinical evaluation | Ann Allergy | Evaluation in ragweed pollinosis (no abstract available) |

## South Africa Market Information

All three registrations are valid single-ingredient syrups. No approved indication text was available in the data compiled for this report. Essential Medicines List (EML) status was not available.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 27/10.1/0529 | Dynalex | Syrup | Not available |
| Reg. No. N/10.1/98 | Theophen Compound Elixir | Syrup | Not available |
| Reg. No. W/10.1/0194 | Actophlem | Syrup | Not available |

## Safety Considerations

Label warnings, contraindications and drug interaction data were not available. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The drug-disease knowledge graph lists the following conditions as contraindications (not taken from label text; verify against the PI):
- Hypertensive disorder and hypertension
- Peptic ulcer disease
- Benign prostatic hyperplasia
- Ocular hypertension, angle-closure glaucoma and closed-angle glaucoma
- Hyperthyroidism, Graves disease and thyrotoxicosis
- Bladder neck obstruction

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for allergic urticaria rests on model score and mechanistic plausibility alone (evidence level L5), with no supporting trials or literature. Urticaria is already an original indication, so this adds no new repurposing value. The safety review is also blocked because label warnings and contraindications are missing.

**To proceed, the following is needed:**
- SAHPRA package insert (PI) with approved indications, warnings and contraindications
- Mechanism of action data (for example from DrugBank)
- Any clinical evidence for diphenylpyraline in urticaria, ideally compared with second-generation antihistamines
- A safety plan for the sedating and anticholinergic effects, especially in the conditions listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

