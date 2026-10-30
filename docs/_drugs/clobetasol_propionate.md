---
layout: default
title: Clobetasol Propionate
parent: Model Prediction Only (L5)
nav_order: 135
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-30
monitor_inn: "CLOBETASOL PROPIONATE"
predicted_indications: ["vulvar inverted follicular keratosis", "acrodermatitis chronica atrophicans", "exanthem (disease)", "acne keloid", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "amyopathic dermatomyositis"]
description: "Clobetasol Propionate: predicted new indication Vulvar inverted follicular keratosis (evidence level L5). Approved use: Not recorded in the local data"
---

# Clobetasol Propionate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Clobetasol Propionate: Vulvar inverted follicular keratosis
{: .text-alpha }

## One-Sentence Summary

Clobetasol propionate is a super-potent topical corticosteroid, originally used for inflammatory skin conditions such as atopic eczema, contact dermatitis and seborrheic dermatitis.
The TxGNN model's top-ranked prediction is **vulvar inverted follicular keratosis**, but it has no supporting studies. The best-supported prediction is **exanthem (disease)** (rank 3), with **7 clinical trials** and no indexed publications, and most of those trials actually study **lichen planus**, not exanthem.

---

## Quick Overview

The top-ranked prediction (rank 1) has no evidence. The table below therefore shows the rank 1 prediction alongside the best-evidenced prediction (rank 3) for context.

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication (rank 1) | Vulvar inverted follicular keratosis |
| TxGNN Prediction Score (rank 1) | 0.9946 |
| Evidence Level (rank 1) | L5 (model prediction only) |
| Best-evidenced prediction (rank 3) | Vulvar inverted follicular keratosis |
| South Africa Market Status | Marketed (valid licences: 1 of 2) |
| Number of SAHPRA Registrations | 2 (valid: 1) |
| Recommended Decision | Hold (rank 1); Proceed with Guardrails as a research question for the lichen planus subset |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on known information, clobetasol propionate is a synthetic glucocorticoid that binds the glucocorticoid receptor (NR3C1). It is used to treat skin inflammation and itching in conditions such as allergic reactions, eczema and psoriasis. Its anti-inflammatory and immunosuppressive action is mechanistically plausible for other inflammatory skin and mucosal diseases.

**Rank 1, vulvar inverted follicular keratosis (0.9946):** This is a benign epithelial lesion related to seborrheic keratosis, which is among clobetasol's original indication classes. However, topical corticosteroids are not an established treatment for keratotic lesions of this type, and no clinical or literature evidence supports the link.

**Rank 3, exanthem (0.9926):** The disease mapping is imprecise. Most of the trials mapped to this term study oral or vulvar lichen planus or lichen sclerosus, inflammatory mucocutaneous diseases in which a glucocorticoid mechanism is plausible. The evidence supports a nearby indication, not exanthem itself, and should not be extrapolated to exanthems generally.

**Other predictions:**
- **Acne keloidalis (rank 4):** a plausible link, since potent steroids reduce inflammation, fibroblast proliferation and collagen synthesis. One 2005 open-label study exists.
- **Amyopathic dermatomyositis (rank 7):** topical steroids are a plausible adjunct for skin lesions, but there is no supporting evidence.
- **Neonatal dermatomyositis (rank 5):** a plausible mechanism, but a super-potent steroid raises safety concerns in neonates (HPA axis suppression, high percutaneous absorption).
- **Acrodermatitis chronica atrophicans (rank 2):** the cause is infectious (Lyme borreliosis) and the primary therapy is antibiotics. Topical steroids may worsen skin atrophy.
- **Childhood connective tissue disease-associated interstitial lung disease (rank 6):** clobetasol is topical and has no plausible route to lung tissue. The prediction likely reflects shared glucocorticoid biology.

---

## Clinical Trial Evidence

The trials below are mapped to the rank 3 prediction (exanthem). Ranks 1, 2 and 4 to 7 have no registered trials in the data compiled.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02573883](https://clinicaltrials.gov/study/NCT02573883) | Phase 3 | Completed | 52 | Clobetasol 0.05% ointment vs fractionated CO2 laser in vulvar lichen sclerosus. The only completed Phase 3 trial. |
| [NCT04364555](https://clinicaltrials.gov/study/NCT04364555) | Phase 2/3 | Active, not recruiting | 90 | Multicentre, placebo-controlled trial of topical clobetasol in symptomatic oral lichen planus. Results not yet available. |
| [NCT03592342](https://clinicaltrials.gov/study/NCT03592342) | Phase 2 | Completed | 140 | Randomised, double-blind, placebo-controlled trial of Rivelin®-CLO intra-oral patches (0, 1, 5 or 20 μg clobetasol) in oral lichen planus, applied up to 6 patches twice daily for 4 weeks. |
| [NCT03026478](https://clinicaltrials.gov/study/NCT03026478) | Phase 2 | Unknown | 30 | Clobetasol vs betamethasone in Orabase with clotrimazole in oral lichen planus. Small and unverified. |
| [NCT07278999](https://clinicaltrials.gov/study/NCT07278999) | Not applicable | Recruiting | 60 | Photobiomodulation vs photodynamic therapy vs topical clobetasol (standard of care) in erosive oral lichen planus. |
| [NCT07536737](https://clinicaltrials.gov/study/NCT07536737) | Not applicable | Completed | 65 | Photodynamic therapy vs topical corticosteroid, with taste perception and salivary oxidative stress as outcomes. Not an efficacy trial of clobetasol. |
| [NCT03386643](https://clinicaltrials.gov/study/NCT03386643) | Phase 2 | Completed | 22 | Probiotic *B. lactis* HN019 in oral lichen planus. Clobetasol is likely background or comparator, so the evidence is indirect. |

No SANCTR or PACTR identifiers were available in the data compiled.

---

## Literature Evidence

Publications are available only for the rank 4 prediction (acne keloidalis).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16047868](https://pubmed.ncbi.nlm.nih.gov/16047868/) | 2005 | Open-label study (non-randomised) | Cutis | Clobetasol propionate 0.05% and betamethasone valerate 0.12% foams in 20 African American patients with mild to moderate acne keloidalis, using a pulsed-dose regimen for 8 to 12 weeks. The abstract notes that no earlier studies had tested topical steroid effectiveness. Results are truncated in the data compiled. |

No related literature was available for the other predicted indications.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 46/13.4.1/0556 | Clobex 120ml | Spray | Not available in the data compiled |
| Reg. No. 27/13.4.1/0122 | Dovate | Ointment | Not available in the data compiled |

Both registrations are valid single-ingredient products. Essential Medicines List (EML) inclusion status was not available in the data compiled.

---

## Safety Considerations

**Contraindications / conditions of concern (from a knowledge-graph drug-disease contraindication list, not label text):**
hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, adrenocortical insufficiency, Addison disease, folliculitis, seborrheic dermatitis, glaucoma, skin atrophy, peripheral vascular disease (including intermittent claudication and peripheral arterial disease).

**Additional considerations from the prediction analysis:**
- Topical corticosteroids may worsen skin atrophy, which is relevant to acrodermatitis chronica atrophicans.
- Neonatal use carries a risk of HPA axis suppression because of high percutaneous absorption of a super-potent steroid.

**Drug interactions:** No drug-drug interactions were identified. The only pharmacology entry is its target, the glucocorticoid receptor (NR3C1).

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications, which were not available for this report. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold (rank 1 and ranks 2, 5, 6, 7); Proceed with Guardrails as a research question for lichen planus (rank 3 subset)**

**Rationale:**
- The top-ranked prediction, vulvar inverted follicular keratosis, rests on model score alone (L5) with no trials or literature, and topical steroids are not an established treatment for it.
- The strongest signal is for lichen planus and lichen sclerosus, not exanthem. It comes from one completed Phase 3 trial (n=52) and a placebo-controlled Phase 2/3 trial that has not yet reported. Many other trials are small, or use clobetasol as a comparator. Acne keloidalis has only a single small open-label study (L3).

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Results of NCT04364555 and NCT03592342, and a systematic review of clobetasol in oral and genital lichen planus
- A re-mapped disease term (lichen planus or lichen sclerosus instead of exanthem) before any evidence grade is applied
- Full results of the acne keloidalis study, ideally with a controlled trial
- A safety plan covering HPA axis suppression, skin atrophy, and use in diabetes, glaucoma and children, particularly neonates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

