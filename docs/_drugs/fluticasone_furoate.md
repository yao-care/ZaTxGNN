---
layout: default
title: Fluticasone Furoate
parent: Model Prediction Only (L5)
nav_order: 238
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-15
description: "Fluticasone Furoate: predicted new indication Atopic eczema (evidence level L5). Approved use: Asthma, allergic rhinitis"
monitor_inn: "FLUTICASONE FUROATE"
predicted_indications: ["atopic eczema", "bronchitis", "2-hydroxyethyl methacrylate sensitization", "dermatitis, atopic", "contact dermatitis", "occupational dermatitis", "phototoxic dermatitis"]
---

# Fluticasone Furoate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Fluticasone Furoate: From Asthma and Allergic Rhinitis to Atopic Eczema

## One-Sentence Summary

Fluticasone furoate is an inhaled and intranasal corticosteroid, originally used for asthma and allergic rhinitis.
The TxGNN model predicts it may be effective for **atopic eczema** (top-ranked prediction), but **no clinical trials** and **no directly relevant publications** currently support this direction. The evidence rests on model prediction and class-level reasoning.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma, allergic rhinitis (SAHPRA indication text not available; based on the knowledge graph) |
| Predicted New Indication | Atopic eczema |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, fluticasone furoate is a potent glucocorticoid receptor agonist with anti-inflammatory activity. Its efficacy in asthma and allergic rhinitis is established, and mechanistically it may be applicable to inflammatory skin disease.

Topical corticosteroids are standard therapy for atopic eczema, so a class-level rationale exists. Allergic rhinitis, asthma and atopic eczema are also commonly linked allergic (atopic) conditions.

There are important caveats:
- The retrieved literature does not evaluate fluticasone furoate for atopic eczema. One paper is a safety review of intranasal corticosteroids and adrenal suppression; the other is a case study of allergen immunotherapy.
- The very high TxGNN score is a computational prediction only.
- The South African products are inhaled or intranasal formulations, not designed for dermatological use. Route compatibility has not been assessed.

**Other predictions in the list**

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Bronchitis | 99.89% | L3 | Indirect evidence from asthma/COPD studies; largely an extension of existing respiratory use. Framed as a research question |
| 3 | 2-hydroxyethyl methacrylate sensitization | 99.87% | L5 | No literature or trials |
| 4 | Dermatitis, atopic | 99.81% | L5 | Same disease as rank 1 |
| 5 | Contact dermatitis | 99.46% | L5 | Class-level plausibility only |
| 6 | Asthma-related traits, susceptibility to | 99.37% | L5 | Genetic trait annotation, overlaps with approved asthma use; not a distinct opportunity |
| 7 | Occupational dermatitis | 99.33% | L5 | No drug-specific data |
| 8 | Phototoxic dermatitis | 99.12% | L5 | No drug-specific data |

## Clinical Trial Evidence

Currently no related clinical trials registered for atopic eczema. No trials were identified for the other predicted indications either.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Review | Neuroimmunomodulation | Intranasal corticosteroids in allergic rhinitis (which often coexists with asthma and atopic dermatitis); reviews adrenal (HPA axis) suppression and tests to detect it. Safety-focused, no efficacy data for eczema |
| [40066386](https://pubmed.ncbi.nlm.nih.gov/40066386/) | 2025 | Case report | Indian J Otolaryngol Head Neck Surg | Allergen immunotherapy in a patient with autoimmune disease. Not about fluticasone furoate |

For the second-ranked prediction (bronchitis), indirect literature exists, mainly from asthma and COPD:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38729884](https://pubmed.ncbi.nlm.nih.gov/38729884/) | 2024 | RCT | Arch Bronconeumol | Triple therapy (LABA/LAMA/ICS) vs LABA/LAMA for clinical control in symptomatic GOLD B COPD patients |
| [21977941](https://pubmed.ncbi.nlm.nih.gov/21977941/) | 2011 | RCT | Respir Res | Once-daily fluticasone furoate (200 or 400 mcg) vs placebo for 8 weeks in persistent asthma |
| [38733542](https://pubmed.ncbi.nlm.nih.gov/38733542/) | 2024 | Cohort | Lung | Fluticasone furoate 200 mcg for 3 weeks in 50 adults with chronic cough and FeNO ≥ 25 ppb; assessed FeNO, cough severity and LCQ |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guideline | Basic Clin Pharmacol Toxicol | Finnish guideline on diagnosis and pharmacotherapy of stable COPD |

## South Africa Market Information

All four registrations are valid single-ingredient registrations. Approved indication text was not available in the data compiled for this report, and Essential Medicines List status was not available.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 41/21.5.1/0967 | Genemist | Spray | Not available |
| 48/21.5.1/0247 | Revinty Ellipta 92/22 µg | Inhaler | Not available |
| 41/21.5.1/0968 | Avamys 120 dose | Aqueous nasal spray | Not available |
| 52/21.5.1/0177 | Trelegy Ellipta | Inhaler | Not available |

No topical (dermatological) formulation is registered among these products.

## Safety Considerations

SAHPRA package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Additional information from the data compiled for this report:

- **Knowledge-graph contraindication associations** (not label text, so they must be verified against the PI): measles, herpes simplex virus keratitis, adrenocortical insufficiency, Addison disease, varicella zoster infection, fungal infectious disease, dermatophytosis, pulmonary tuberculosis, ocular hypertension, glaucoma, parasitic infection, infectious disease, lower respiratory tract disease, paranasal sinus disease, nasal cavity disease, upper respiratory tract disease, adrenal gland hyperfunction, Cushing syndrome.
- **Systemic effects**: the retrieved review highlights the potential for adrenal (HPA axis) suppression with intranasal corticosteroids. This would matter if the drug were used on large skin areas or in children.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Atopic eczema is supported only by a model prediction (L5) and class-level reasoning. No trials exist, and the retrieved papers do not evaluate fluticasone furoate for this condition.
- The registered South African products are inhaled or nasal, with no dermatological formulation. Safety data from the package insert are also missing, which is a blocking gap.
- Bronchitis (L3) is a more tractable research question, but it largely extends existing respiratory use and has only indirect evidence.

**To proceed, the following is needed:**
- Download and review the SAHPRA package insert (warnings, contraindications, approved indications), which is the blocking gap.
- Mechanism of action data (for example from DrugBank).
- A targeted literature search for fluticasone furoate in atopic eczema or dermatitis, including any topical or dermatological formulation.
- Assessment of route and formulation compatibility for any skin indication, and a systemic exposure and HPA-axis safety review.
- For bronchitis, a focused review of whether the existing asthma/COPD evidence is sufficient, or whether a pragmatic study is warranted.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

