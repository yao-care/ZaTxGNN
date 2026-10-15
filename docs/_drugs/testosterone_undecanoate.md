---
layout: default
title: Testosterone Undecanoate
parent: Model Prediction Only (L5)
nav_order: 443
evidence_level: L5
indication_count: 10
---

# Testosterone Undecanoate
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

# Testosterone undecanoate: From Hypogonadism to Homozygous Familial Hypercholesterolaemia

## One-Sentence Summary

Testosterone undecanoate is an androgen replacement therapy, originally used to treat hypogonadism (including primary ovarian failure and hypogonadotropic hypogonadism).
The TxGNN model's top-ranked prediction is **homozygous familial hypercholesterolaemia (HoFH)**, but **no clinical trials and no publications** support this direction, and the available mechanistic reasoning argues against benefit.
Among the other predictions, **androgen insensitivity syndrome (AIS)** has the most evidence (2 publications) and is the more credible research question.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypogonadism (primary ovarian failure, hypogonadotropic hypogonadism with or without anosmia). The SAHPRA registration text for the indication was not available. |
| Predicted New Indication | Homozygous familial hypercholesterolaemia |
| TxGNN Prediction Score | 98.73% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

The top-ranked prediction scores highly but lacks supporting evidence. Other predictions are summarised below for context.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|------|------|------|------|
| 1 | Homozygous familial hypercholesterolaemia | 98.73% | L5 | Hold |
| 2 | Androgen insensitivity syndrome | 95.72% | L3 | Research Question |
| 3 | Leydig cell hypoplasia due to LH resistance | 94.50% | L4 | Research Question |
| 4 | 46,XY disorder of sex development due to impaired androgen production | 93.67% | L4 | Research Question |
| 5 | Symptomatic fragile X syndrome in female carrier | 92.66% | L5 | Hold |
| 6 | Blepharophimosis-epicanthus inversus-ptosis | 91.57% | L5 | Hold |
| 7 | BPES due to 3q23 rearrangement syndrome | 90.88% | L5 | Hold |
| 8 | Telecanthus | 90.57% | L5 | Hold |
| 9 | Ovarian hyperstimulation syndrome | 90.50% | L5 | Hold |
| 10 | Partial trisomy/tetrasomy of the short arm of chromosome 5 | 90.39% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, testosterone undecanoate is an esterified form of testosterone used for androgen replacement, and its efficacy in hypogonadism rests on restoring circulating testosterone.

**For the top-ranked prediction (HoFH), the rationale is weak.** HoFH is caused by defects in the LDL receptor pathway. Androgens generally lower HDL cholesterol and have variable effects on LDL cholesterol, so there is no plausible reason to expect benefit, and a possible harmful effect on the lipid profile should be considered. The high score appears to be a graph-based artefact rather than a pharmacological signal.

**Better-supported predictions relate to androgen deficiency or resistance:**
- **Leydig cell hypoplasia and 46,XY DSD due to impaired androgen production:** these are testosterone-deficiency states, so replacement is mechanistically rational and overlaps with the approved hypogonadism use. This support is indirect, as no trials or literature were identified.
- **Androgen insensitivity syndrome:** partial AIS with residual receptor function may respond to higher-dose androgen, for example for phallic growth in children. In complete AIS the receptor is non-functional, so androgen effect is expected to be minimal or absent, although aromatisation to oestradiol may matter.
- **The remaining predictions** (fragile X carrier symptoms, BPES-related conditions, telecanthus, OHSS, chromosomal disorder) have no plausible androgen-based mechanism. Their scores likely reflect proximity in the knowledge graph.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the predicted indications.

---

## Literature Evidence

No literature was identified for the top-ranked prediction (HoFH). The following publications relate to the second-ranked prediction, androgen insensitivity syndrome. The abstracts supplied were truncated, so study designs are provisional and should be verified against the full texts.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39039878](https://pubmed.ncbi.nlm.nih.gov/39039878/) | 2024 | Cohort (presumed; self-controlled design stated in abstract) | Zhonghua Er Ke Za Zhi | Efficacy and safety of oral testosterone undecanoate in children with genetically diagnosed AIS, treated at Beijing Children's Hospital (2009–2021). Effect sizes not available in the supplied abstract. |
| [8246276](https://pubmed.ncbi.nlm.nih.gov/8246276/) | 1993 | Double-blind crossover study (4 patients) | J Sex Marital Ther | Oral testosterone undecanoate (120 mg/day) vs placebo for 4 weeks in four gonadectomised women with complete testicular feminisation, assessing hormone levels, mood, sociosexual functioning and body self-image. Very small sample. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| A38/21.7/0641 | Nebido 4 ml vial | Injection | Not available in the data compiled for this report |

Only one registration exists, and it is an injectable (depot) product. Essential Medicines List status could not be determined from the data compiled for this report.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Additional points from the compiled analysis:
- For HoFH, androgens may worsen the lipid profile (for example by lowering HDL).
- For women and girls (for example OHSS, ovarian conditions), androgen exposure raises virilisation concerns.
- No drug-drug interaction records were found in the data queried.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, homozygous familial hypercholesterolaemia, rests on a model score alone (L5), with no trials, no literature and no plausible mechanism. Possible harm to the lipid profile argues against pursuing it. Androgen insensitivity syndrome (L3), Leydig cell hypoplasia and 46,XY DSD (L4) are more credible research questions, but the evidence is small, indirect or unverified, and does not yet justify a move forward.

**To proceed, the following is needed:**
- Retrieve and review the SAHPRA Professional Information (PI) for Nebido, including approved indication, warnings and contraindications. This gap currently blocks safety screening.
- Obtain mechanism of action data (for example from DrugBank).
- Read the full texts of PMID 39039878 and 8246276 to confirm study design, dose, AIS subtype and effect sizes.
- Consider redirecting the evaluation to AIS (partial forms), Leydig cell hypoplasia and 46,XY DSD, with a targeted literature search on each.
- Note that the studied oral formulation differs from the registered injectable product, so route compatibility would need to be assessed.
- Do not pursue HoFH unless new mechanistic or clinical evidence emerges.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

