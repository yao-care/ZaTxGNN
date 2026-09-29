---
layout: default
title: Magnesium Acetate
parent: Model Prediction Only (L5)
nav_order: 303
evidence_level: L5
indication_count: 10
---

# Magnesium Acetate
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

# Magnesium Acetate: From Parenteral Nutrition Component to Hypertensive Disorder

## One-Sentence Summary

Magnesium acetate is registered in South Africa as an ingredient of parenteral nutrition (TPN) infusion products. The TxGNN model predicts it may be useful for **hypertensive disorder**, but no clinical trial or publication directly supports this. All 3 retrieved trials were judged irrelevant, and the 3 retrieved papers are preclinical work on acetate, not on the magnesium salt.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data. Registered as a component of parenteral nutrition (TPN) products |
| Predicted New Indication | Hypertensive disorder |
| TxGNN Prediction Score | 97.42% |
| Evidence Level | L4 (preclinical only, indirect) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 entries (2 distinct registration numbers) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, magnesium acetate is an electrolyte component of multi-ingredient parenteral nutrition products. Its established role is supplying magnesium and acetate within TPN, not treating any specific disease.

The only mechanistic hint in the retrieved data is indirect. Three papers describe acetate, a short-chain fatty acid (SCFA) produced by gut microbiota, as having a blood-pressure-lowering effect in animal models. These studies do not test magnesium acetate, so they cannot show that the magnesium salt has any effect. A blood-pressure effect of the magnesium ion is plausible from general pharmacological knowledge, but the supplied data do not support it. The high TxGNN score is a computational prediction and should be treated as a hypothesis only.

## Clinical Trial Evidence

All three retrieved trials were graded C (not evidence for this indication). They appear to have been matched on the drug name or the word "acetate".

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05251402](https://clinicaltrials.gov/study/NCT05251402) | Phase 2/3 | Active, not recruiting | 323 | DASH diet in uncontrolled asthma. Not a hypertension study |
| [NCT07206524](https://clinicaltrials.gov/study/NCT07206524) | N/A | Recruiting | 15 | Magnesium concentration in hemodialysis dialysate and thromboinflammation. Magnesium exposure is relevant, the indication is not |
| [NCT00570479](https://clinicaltrials.gov/study/NCT00570479) | Phase 1 | Completed | 12 | Anecortave acetate for steroid-induced glaucoma. A different compound |

No SANCTR or PACTR registrations were identified.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35887270](https://pubmed.ncbi.nlm.nih.gov/35887270/) | 2022 | Preclinical | Int J Mol Sci | Maternal acetate supplementation reversed the blood-pressure rise in male offspring exposed to minocycline (animal model) |
| [33087738](https://pubmed.ncbi.nlm.nih.gov/33087738/) | 2020 | Preclinical | Sci Rep | Prebiotic fibre and acetate release did not override a genetic predisposition to heart failure in the model studied |
| [31295767](https://pubmed.ncbi.nlm.nih.gov/31295767/) | 2019 | Review (as classified) | Mol Nutr Food Res | Acetate supplementation examined for preventing programmed hypertension in offspring after a maternal high-fructose diet. The abstract describes an experimental animal study |

All three papers concern acetate as a gut-derived metabolite, not magnesium acetate, and none involves human patients.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 41/25/0757 | Nutriflex Lipid Peri | Infusion |
| Reg. No. 41/25/0757 | Nutriflex lipid peri 1875ml | TPN |
| Reg. No. 41/25/0759 | Nutriflex lipid special 625ml | TPN |

The registration data supplied contain no approved-indication text or manufacturer. All listed products are parenteral (infusion/TPN) presentations of fixed multi-ingredient nutrition mixtures.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The link to hypertension rests on a model score and on indirect animal data about acetate. The retrieved trials are irrelevant. The other nine predicted indications (including pulmonary hypertension, malignant hypertensive renal disease, gout and open-angle glaucoma) have no supporting trials or relevant literature and are also on Hold.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings and contraindications), needed before any safety screening
- Mechanism of action data for magnesium acetate, for example from DrugBank
- Magnesium-specific evidence on blood pressure, such as magnesium supplementation trials or meta-analyses
- A route and formulation assessment. The registered products are fixed-composition TPN infusions, so a hypertension use would probably need a different product or route
- Manual review of the trial records, particularly the truncated NCT02795754 record linked to the lower-ranked potassium deficiency prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

