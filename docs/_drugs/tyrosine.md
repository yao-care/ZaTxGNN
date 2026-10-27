---
layout: default
title: Tyrosine
parent: Model Prediction Only (L5)
nav_order: 464
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tyrosine: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not stated in the registration data (products are amino acid-containi…"
monitor_inn: "Tyrosine"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "angle-closure glaucoma", "hyperthyroidism", "postural orthostatic tachycardia syndrome", "hyperthyroxinemia", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "aqueous misdirection", "traumatic glaucoma", "neovascular glaucoma"]
---

# Tyrosine
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

## Tyrosine: From Nutritional and Parenteral Amino Acid Component to Cauda Equina Syndrome
{: .text-alpha }

## One-Sentence Summary

Tyrosine is an amino acid found in several parenteral nutrition and dialysis solutions registered in South Africa, and no specific approved indication text is available in the data compiled for this report.
The TxGNN model ranks **cauda equina syndrome** as its top prediction (score 99.77%), but there are **no clinical trials and no publications** supporting this prediction.
The prediction is model-only, and the evidence is weak across all ten predicted indications.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data (products are amino acid-containing infusion and parenteral nutrition solutions) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Tyrosine is a proteinogenic amino acid and a precursor of catecholamines (dopamine, noradrenaline, adrenaline) and thyroid hormones. Its registered use appears to be as a nutritional component of multi-ingredient infusion products.

For cauda equina syndrome, the data compiled for this report do not support any mechanistic link. The condition is a compressive injury to the lumbosacral nerve roots, and nothing connects tyrosine to its treatment. The high TxGNN score is a model output only and should not be read as evidence of efficacy.

Other predicted indications were also reviewed:

- **Hyperthyroidism and hyperthyroxinemia:** Tyrosine is a substrate for thyroid hormone synthesis. Supplementation could theoretically worsen rather than treat these conditions, which is a safety concern rather than support for repurposing.
- **Resistance to thyroid hormone (THRB mutation):** This is a receptor-level defect, so supplying more substrate is unlikely to help.
- **Postural orthostatic tachycardia syndrome (POTS):** Catecholamine dysregulation is plausible, and this is the only indication rated as a research question (evidence level L4). The only retrieved item is a case report on alpha-methyl-p-tyrosine, a tyrosine hydroxylase inhibitor that acts in the opposite direction to tyrosine, so it does not support tyrosine efficacy.
- **Glaucoma-related conditions (angle-closure, traumatic, neovascular, aqueous misdirection):** No literature evaluates tyrosine as a treatment. One 2026 cohort study reports plasma amino acid changes in early primary angle-closure glaucoma, which is hypothesis-generating only.
- **Obsolete neurogenic bladder:** No evidence, and the disease term is flagged obsolete in the ontology.

---

## Clinical Trial Evidence

Only one registered trial was found across all predicted indications, and it relates to hyperthyroidism rather than the top-ranked prediction.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06264544](https://clinicaltrials.gov/study/NCT06264544) | Not applicable | Not yet recruiting | 150 | Placebo-controlled trial of a zinc, selenium and L-tyrosine supplement for preventing thyrotoxicosis in adults with elevated TPOAb and the SEPP1 r25191G/A polymorphism. Tyrosine is not the sole tested agent, and no results are available. |

There are no registered trials for cauda equina syndrome. No SANCTR or PACTR identifiers were found.

---

## Literature Evidence

There is no literature for cauda equina syndrome. The table below lists the most relevant items from other predicted indications; none of them tests tyrosine as a treatment.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42812246](https://pubmed.ncbi.nlm.nih.gov/42812246/) | 2026 | Cohort | Frontiers in Medicine | Plasma amino acid metabolic alterations associated with ocular parameters in early primary angle-closure glaucoma (observational, no tyrosine intervention) |
| [39063020](https://pubmed.ncbi.nlm.nih.gov/39063020/) | 2024 | Case report | Int J Mol Sci | Chronic fatigue syndrome responding to alpha-methyl-p-tyrosine, a tyrosine hydroxylase inhibitor (opposite mechanism to tyrosine) |
| [36848916](https://pubmed.ncbi.nlm.nih.gov/36848916/) | 2023 | Review | Lancet Diabetes Endocrinol | General review of hyperthyroidism aetiology, diagnosis and management |
| [35087972](https://pubmed.ncbi.nlm.nih.gov/35087972/) | 2021 | Review | Rom J Ophthalmol | Review of neovascular glaucoma aetiopathogenesis and treatment |
| [19169471](https://pubmed.ncbi.nlm.nih.gov/19169471/) | 2008 | Case report | Arq Bras Endocrinol Metabol | THRB E449X mutation with autoimmune thyroid disease and neuropsychomotor involvement |
| [10579356](https://pubmed.ncbi.nlm.nih.gov/10579356/) | 1999 | Preclinical | Endocrinology | Novel thyroid hormone receptor beta mutations impairing ligand binding |

Many of the thyroid-related papers retrieved concern tyrosine kinase inhibitors, which are unrelated to the amino acid tyrosine.

---

## South Africa Market Information

All eight registrations are valid single-ingredient entries. No approved indication text is recorded for any of them, and Essential Medicines List status is not available in the data compiled for this report.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 37/34/0243 | Nutrineal PD4 with 1.1% amino acids 2.5L | Infusion | Not stated |
| Reg. No. 38/34/0172 | Extraneal 2L single bag | Infusion | Not stated |
| Reg. No. 37/25.2/0503 | Oliclinomel N6 900E 2000ml | Infusion | Not stated |
| Reg. No. 52/25/0739 | Numeta G13E | Infusion | Not stated |
| Reg. No. 52/25/0740 | Numeta G16E | Infusion | Not stated |

Three further registrations exist: Smofkabiven (46/32.2/0518), Smofkabiven Peripheral (47/32.2/0036) and Adco-ipratropium (33/10.2.1/0271). The last is listed as a vial and its link to tyrosine should be verified.

---

## Safety Considerations

No warning, contraindication or drug interaction data were available in the data compiled for this report, and no contraindicated diseases were identified from the knowledge graph.

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

One theoretical concern arises from the biology: because tyrosine is a thyroid hormone precursor, supplementation in hyperthyroid states would need careful consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for cauda equina syndrome rests on the model score alone (evidence level L5), with no trials, no literature and no supported mechanism. None of the ten predicted indications has clinical evidence that tyrosine is effective.

**To proceed, the following is needed:**
- Retrieval of the SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data for tyrosine, to allow proper mechanistic analysis
- Clarification of approved indications for each registered product
- Any preclinical or clinical evidence linking tyrosine to nerve-root injury before further consideration
- If any indication is pursued, POTS is the only one rated as a research question, and it would need a purpose-designed study with safety review, particularly regarding thyroid effects
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

