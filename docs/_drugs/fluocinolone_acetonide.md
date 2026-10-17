---
layout: default
title: Fluocinolone Acetonide
parent: Model Prediction Only (L5)
nav_order: 236
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Fluocinolone Acetonide: predicted new indication Annular atrophic lichen planus (evidence level L5). Approved use: Inflammatory skin conditions, including atopic dermatitis…"
monitor_inn: "FLUOCINOLONE ACETONIDE"
predicted_indications: ["annular atrophic lichen planus", "hypertrophic lichen planus", "lichen planus pigmentosus", "lichen planus pemphigoides"]
---

# Fluocinolone Acetonide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Fluocinolone Acetonide: From Inflammatory Skin Conditions to Annular Atrophic Lichen Planus

## One-Sentence Summary

Fluocinolone acetonide is a topical corticosteroid, originally used for inflammatory and itchy skin conditions such as atopic dermatitis, contact dermatitis, seborrhoeic dermatitis and discoid lupus erythematosus.
The TxGNN model predicts it may be effective for **annular atrophic lichen planus**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Inflammatory skin conditions, including atopic dermatitis, contact dermatitis, seborrhoeic dermatitis, lichen disease and discoid lupus erythematosus (the SAHPRA record for the registered product has no indication text) |
| Predicted New Indication | Annular atrophic lichen planus |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

Other predicted indications with the same evidence profile (prediction only, no trials or literature):

| Predicted Indication | TxGNN Score | Evidence Level |
|------|------|------|
| Hypertrophic lichen planus | 99.42% | L5 |
| Lichen planus pigmentosus | 99.42% | L5 |
| Lichen planus pemphigoides | 99.34% | L5 |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, fluocinolone acetonide is a synthetic corticosteroid. Pharmacology data list the glucocorticoid receptor (NR3C1) as its target. Its efficacy in inflammatory and immune-mediated skin conditions is established, and mechanistically it may be applicable to lichen planus.

Lichen planus is a T-cell-mediated inflammatory skin disease. The anti-inflammatory and immunosuppressive action of corticosteroids is therefore biologically plausible for it, and potent topical corticosteroids are a standard drug class for this group of conditions. This reasoning rests on class-level knowledge rather than data specific to this drug.

Two caveats apply:
- "Lichen disease" is already among the drug's original indications. The prediction may therefore be a subtype extension of an existing use rather than true repurposing.
- Subtypes differ. Lichen planus pigmentosus has a pigmentary component that may respond less predictably. Lichen planus pemphigoides has an autoimmune blistering component that often needs systemic immunosuppression, so topical therapy may help only localised disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 56/16.2/0942 | Otixal | Drops | Not stated in the available record |

Only one valid single-ingredient registration exists, and it is a drops formulation. This is not a cream or ointment, so it is not directly suited to skin lichen planus. Route compatibility with the predicted indications has not been assessed. Essential Medicines List (EML) status is not available in the data compiled for this report.

## Safety Considerations

**Contraindications from the knowledge graph** (drug-disease links in the TxGNN knowledge graph, not label text): sunburn, herpes simplex infections (including herpes simplex keratitis), geniculate herpes zoster, adrenocortical insufficiency, Addison disease, glaucoma, skin atrophy, telangiectasis, hereditary haemorrhagic telangiectasia, capillary disease, peripheral vascular disease, peripheral arterial disease, intermittent vascular claudication, fungal eye infection, mycotic corneal ulcer, ocular tuberculosis, and dermatitis.

Skin atrophy is relevant to the predicted indication of *annular atrophic* lichen planus and warrants caution.

**Drug interactions:** The interaction search returned 10 entries. Nine have an unclassified severity level. They are dexamethasone, cetirizine, citalopram, valproic acid, acetaminophen, digoxin, levothyroxine, alendronic acid and clonazepam. The tenth is a pharmacology record for the glucocorticoid receptor. Clinical significance cannot be judged from these data.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and precautions, which were not available for this report. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (99.42%), but there are no clinical trials or publications, and the mechanism of action data are missing. The only registered product in South Africa is a drops formulation, and the PI safety information could not be obtained. The prediction may also overlap with the existing "lichen disease" indication.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications, approved indications) for safety screening. This is a blocking gap.
- Mechanism of action data, for example from DrugBank.
- A literature and trial search for topical fluocinolone acetonide in lichen planus subtypes.
- Confirmation of whether the predicted indications are covered by the existing "lichen disease" indication.
- Assessment of route compatibility, since the registered product is a drops formulation.
- Review of the skin atrophy risk in atrophic lichen planus, and of the severity of the listed drug interactions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

