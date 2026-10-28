---
layout: default
title: Latanoprostene Bunod
parent: Model Prediction Only (L5)
nav_order: 289
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Latanoprostene Bunod: predicted new indication Visceral calciphylaxis (evidence level L5). Approved use: Open-angle glaucoma"
monitor_inn: "Latanoprostene bunod"
predicted_indications: ["visceral calciphylaxis", "arterial thoracic outlet syndrome", "venous thoracic outlet syndrome", "neurogenic thoracic outlet syndrome", "vascular disease", "idiopathic spontaneous coronary artery dissection", "angiodysplasia of stomach", "lymphangiectasis", "hemangioendothelioma"]
---

# Latanoprostene Bunod
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Latanoprostene bunod: From Open-Angle Glaucoma to Visceral Calciphylaxis
{: .text-alpha }

## One-Sentence Summary

Latanoprostene bunod is an eye-drop medicine originally used to lower eye pressure in open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **visceral calciphylaxis**, but this is a model prediction only, with **0 clinical trials** and **0 publications** directly supporting it.
Among the other top-ranked predictions, only "vascular disease" has any related material (1 indirect trial and 1 review), and neither shows efficacy.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma; ocular hypertension (SAHPRA indication text not available) |
| Predicted New Indication | Visceral calciphylaxis |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 1 of 1) |
| Number of SAHPRA Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the pharmacology information available, latanoprostene bunod is broken down in the eye into two active parts: latanoprost acid (a prostaglandin F2-alpha analogue acting on the FP receptor) and nitric oxide (NO). Laboratory data show it increases guanylyl cyclase activity and cGMP formation. Together, these actions lower eye pressure by improving fluid drainage from the eye.

The link to visceral calciphylaxis (a condition of calcification and blockage of small blood vessels) is only theoretical. NO-mediated vasodilation could in principle relate to calcific vascular disease, but no clinical or published support exists. The drug is given as an eye drop, so very little reaches the rest of the body, which makes an effect on a visceral vascular disease unlikely. The prediction should be treated as a hypothesis only.

Other predictions in the top 10 are also weak:
- **Thoracic outlet syndromes (venous, arterial, neurogenic)**, **spontaneous coronary artery dissection**, **angiodysplasia of stomach** and **lymphangiectasis**: no plausible mechanistic link and no evidence. These scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.
- **Vascular disease** (score 0.9953): indirect ocular blood-flow rationale only.
- **Hemangioendothelioma** (score 0.9947): the only publication is a safety signal, not evidence of benefit.

## Clinical Trial Evidence

For the lead prediction (visceral calciphylaxis): currently no related clinical trials registered.

The only trial found for any top-10 prediction relates to "vascular disease" and is indirect:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03931317](https://clinicaltrials.gov/study/NCT03931317) | Not applicable | Completed | 70 | Randomised, masked crossover comparison of latanoprostene bunod and timolol on eye pressure and retinal blood vessel density in ocular hypertension or primary open-angle glaucoma. Does not establish efficacy in systemic vascular disease. |

## Literature Evidence

For the lead prediction (visceral calciphylaxis): currently no related literature available.

Publications found for other top-10 predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30028313](https://pubmed.ncbi.nlm.nih.gov/30028313/) | 2018 | Review | Neural Regeneration Research | Overview of treatment options for glaucomatous optic neuropathy. Not direct evidence in vascular disease. |
| [38113361](https://pubmed.ncbi.nlm.nih.gov/38113361/) | 2023 | Case report | Ophthalmic Surgery, Lasers & Imaging Retina | An 11-year-old girl with a port-wine birthmark, choroidal haemangioma and glaucoma developed serous retinal detachment on prostaglandin analogue therapy (bimatoprost, then latanoprostene bunod). Vision and the detachment improved after stopping the drug. This is a safety signal, not evidence of benefit. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 53/15.4/0226 | Vyzulta | Drops | Not available in the data compiled for this report |

Essential Medicines List (EML) status was not available in the data compiled for this report.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Additional points from the data compiled for this report:
- **Pharmacology interaction record**: the only interaction entry is the drug's own target, the prostanoid FP receptor. This is a pharmacological target, not a drug-drug interaction.
- **Case report signal**: serous retinal detachment was reported with prostaglandin analogue use in a child with a port-wine birthmark and choroidal haemangioma. Caution is advised in patients with vascular malformations.
- **Theoretical concern**: vasodilating agents could aggravate vascular malformations with bleeding risk (for example angiodysplasia). This is not supported by clinical data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The visceral calciphylaxis prediction rests on the model score alone (L5), with no trials or publications. The eye-drop route gives minimal systemic exposure, which further weakens plausibility. None of the other top-10 predictions has supportive evidence. "Primary hereditary glaucoma" is an extension of the current indication rather than true repurposing.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings, contraindications and approved indication text), which is currently a blocking gap for safety screening
- Detailed mechanism of action data
- Preclinical evidence (for example, calcification models) for a plausible mechanism in visceral calciphylaxis
- Evidence that adequate drug levels can reach the target tissue, or a different route of administration
- For primary hereditary glaucoma: paediatric or congenital glaucoma efficacy and safety data, handled as an indication extension
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

