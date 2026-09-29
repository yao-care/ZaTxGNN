---
layout: default
title: Budesonide
parent: Model Prediction Only (L5)
nav_order: 80
evidence_level: L5
indication_count: 10
---

# Budesonide
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

# Budesonide: From Marketed Corticosteroid Products to Atopic Eczema

## One-Sentence Summary

Budesonide is a glucocorticoid marketed in South Africa in capsule, inhaler, nebule and nasal-spray forms. The SAHPRA indication text was not available in the source data.
The TxGNN model predicts it may be effective for **atopic eczema**.
Only **2 registered clinical trials** and **20 publications** were retrieved, and none is a human efficacy study of budesonide in eczema.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Atopic eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 (preclinical/mechanism only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Budesonide is a glucocorticoid receptor agonist with broad anti-inflammatory activity. Detailed mechanism data are not available from DrugBank in this pack, so this description comes from the repurposing rationale.

Topical corticosteroids as a class are an established treatment for atopic dermatitis, so the mechanistic link is plausible. Budesonide has also been used topically in children with atopic dermatitis in small studies, and a 2024 preclinical study developed a budesonide hydrogel for this purpose.

The support is therefore class-effect reasoning plus formulation research. There are no budesonide-specific human trials for eczema. The SAHPRA-registered forms are oral, inhaled and nebulised, not dermal, so the route needed for eczema is not currently registered.

Note that "dermatitis, atopic" (rank 3) is a duplicate of this concept and should be merged with it.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01028560](https://clinicaltrials.gov/study/NCT01028560) | Phase 1/2 | Completed | 58 | Allergy immunotherapy to prevent asthma in atopic wheezing children. Not a budesonide trial, and the endpoint is asthma, not eczema. |
| [NCT04680117](https://clinicaltrials.gov/study/NCT04680117) | N/A | Unknown | 150 | Non-interventional endotyping of severe paediatric asthma. Does not test budesonide for eczema. |

Neither trial is relevant to budesonide treatment of eczema. No SANCTR or PACTR identifiers were found.

## Literature Evidence

Only 10 of the 20 retrieved publications are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21062310](https://pubmed.ncbi.nlm.nih.gov/21062310/) | 2010 | Randomised placebo-controlled crossover trial (dogs) | J Vet Pharmacol Ther | 0.025% budesonide leave-on conditioner reduced skin lesions and pruritus in canine atopic dermatitis. Veterinary evidence only. |
| [9496795](https://pubmed.ncbi.nlm.nih.gov/9496795/) | 1998 | Open longitudinal trial | Pediatr Dermatol | Short-term growth (knemometry) assessed in 14 children with atopic dermatitis treated with topical budesonide. This is a safety study, not an efficacy study. |
| [38275852](https://pubmed.ncbi.nlm.nih.gov/38275852/) | 2024 | Preclinical formulation study | Gels (Basel) | Budesonide-loaded pH-sensitive nanoparticles in hydrogels for local atopic dermatitis therapy. |
| [8864369](https://pubmed.ncbi.nlm.nih.gov/8864369/) | 1996 | Clinical study | Dermatology | Bone and collagen turnover and the IGF axis in children with atopic dermatitis on topical glucocorticoids. Drug identity unconfirmed. |
| [14616123](https://pubmed.ncbi.nlm.nih.gov/14616123/) | 2003 | Review | Allergy | Corticosteroid allergy in asthma. Glucocorticoids frequently cause delayed contact allergy. |
| [33931866](https://pubmed.ncbi.nlm.nih.gov/33931866/) | 2021 | Patch-test series | Contact Dermatitis | Budesonide patch testing in Italy. A decreasing trend of budesonide allergy has been observed. |
| [35133669](https://pubmed.ncbi.nlm.nih.gov/35133669/) | 2022 | Cohort | Contact Dermatitis | Contact sensitisation patterns in patients with and without atopic dermatitis. |
| [24603519](https://pubmed.ncbi.nlm.nih.gov/24603519/) | 2014 | Cohort | Dermatitis | Contact hypersensitivity, including corticosteroid series, in patients with atopic dermatitis. |
| [35184304](https://pubmed.ncbi.nlm.nih.gov/35184304/) | 2022 | Case report | Contact Dermatitis | Systemic allergic dermatitis after budesonide patch testing. |
| [37927648](https://pubmed.ncbi.nlm.nih.gov/37927648/) | 2023 | Case report | Cureus | Steroid-induced angioedema and urticaria in a patient with atopic dermatitis. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 36/21.5.1/0258 | Budeflam 200 Dp-Caps | Capsule | Not recorded in source data |
| Reg. No. 35/21,5,1/0405 | Symbicord Turbuhaler 60 dose 160mcg/4.5mcg | Tbh | Not recorded in source data |
| Reg. No. A40/21.5.1/0224 | Spec-Budesonide 10 ml 200 dose | Aqs | Not recorded in source data |
| Reg. No. 42/21.5.1/0955 | Arrow Budesonide 2 ml | Vial | Not recorded in source data |
| Reg. No. A39/21.5.1/0506 | Vannair 80/4.5mcg per inhalation 120 dose | Inhaler | Not recorded in source data |

Product names and dosage forms are shown as recorded. Essential Medicines List status is not available in the source data. None of the five registrations is a dermal (topical) formulation.

## Safety Considerations

- **Drug Interactions**: The DDI query returned no records.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

Safety signals from the literature include:
- **Contact and systemic allergy to budesonide**: reported in patch-test series and case reports (PMIDs 33931866, 35184304).
- **Systemic effects of topical corticosteroids in children**: growth and bone/collagen turnover have been studied because of percutaneous absorption (PMIDs 9496795, 8864369).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but the evidence is L4 (S0, research question). There are no budesonide-specific human efficacy trials in eczema, and the only direct support is a veterinary trial and a preclinical formulation study. The registered forms in South Africa are not dermal, and contact allergy to budesonide is a documented concern.

**To proceed, the following is needed:**
- SAHPRA Professional Information for each registration, to fill the warnings and contraindications gap (blocking).
- DrugBank mechanism of action data.
- Human clinical evidence of topical budesonide in atopic eczema, such as an RCT or systematic review, and a route-compatibility assessment against the registered forms.
- Merge the duplicate "atopic eczema" and "dermatitis, atopic" predictions.
- Note that the rank 2 prediction, **bronchitis** (L2, Phase 2 budesonide/formoterol data in bronchiolitis obliterans, Proceed with Guardrails), has far stronger evidence and may deserve priority review. Its indication scope needs to be defined first.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

