---
layout: default
title: Levothyroxine
parent: Model Prediction Only (L5)
nav_order: 295
evidence_level: L5
indication_count: 4
monitor_inn: "Levothyroxine"
predicted_indications: ["renal hypodysplasia/aplasia", "bilateral renal agenesis", "Potter sequence", "Carney complex"]
last_modified_at: 2026-10-23
description: "Levothyroxine: predicted new indication Renal hypodysplasia/aplasia (evidence level L5). Approved use: Hypothyroidism and related thyroid conditions"
---

# Levothyroxine
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

## Levothyroxine: From Thyroid Hormone Replacement to Renal Hypodysplasia/Aplasia
{: .text-alpha }

## One-Sentence Summary

Levothyroxine is a thyroid hormone replacement used for hypothyroidism and related thyroid conditions.
The TxGNN model predicts it may be effective for **renal hypodysplasia/aplasia**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypothyroidism and related thyroid conditions (relations recorded in the knowledge graph; the local registration contains no indication text) |
| Predicted New Indication | Renal hypodysplasia/aplasia |
| TxGNN Prediction Score | 0.9967 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 1 of 1) |
| Number of SAHPRA Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for levothyroxine. It is a synthetic thyroid hormone, and the relations recorded in the knowledge graph centre on hypothyroidism, other thyroid diseases (including thyroid cancer) and hyperlipidaemia.

The link to renal hypodysplasia/aplasia is weak. Thyroid hormone contributes to general kidney development and maturation, but these structural malformations are mainly driven by genetic variants that affect nephrogenesis (for example PAX2, HNF1B, RET, GDNF). The defect is established in utero, so postnatal hormone replacement is biologically implausible as a treatment. The high score (0.9967) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as the co-occurrence of congenital anomalies with congenital hypothyroidism, not biological evidence or a therapeutic mechanism.

Other predictions for this drug have the same problem:
- **Bilateral renal agenesis** (score 0.9960): the kidneys are absent and levothyroxine cannot regenerate them. No supporting studies.
- **Potter sequence** (score 0.9933): management is supportive. There is no clinical evidence that levothyroxine alters its course.
- **Carney complex** (score 0.9918): the most biologically coherent, because thyroid nodules and neoplasia occur and TSH signals through cAMP, but levothyroxine would only manage a co-occurring thyroid condition, not the underlying disease. No evidence supports it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 56/21.3/0331 | Roidace 25 | Tablet | Not stated in the data compiled for this report |

This is a single-ingredient oral product and is currently valid. Essential Medicines List status is not available in the data compiled for this report.

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** The knowledge graph links levothyroxine to the following conditions as contraindications. These need to be verified against the approved Professional Information (PI).
  - Cardiovascular: hypertension, coronary artery disease, myocardial infarction
  - Pituitary and gonadal: hypopituitarism and pituitary hormone deficiencies, growth hormone deficiency, Sheehan syndrome, hypogonadotropic hypogonadism, Kallmann syndrome
  - Metabolic and bone: diabetes mellitus, diabetic ketoacidosis, osteoporosis (including postmenopausal)
  - Other: thymus gland disease
- **Drug Interactions:** 100 interactions were found, and 20 are listed in the data compiled for this report. Most are Moderate, and one (cimetidine) is Minor.
  - Antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, albiglutide, dulaglutide, chlorpropamide, and the SGLT2 inhibitors canagliflozin, dapagliflozin and empagliflozin): thyroid hormone may alter glycaemic control.
  - Acid-suppressing agents (omeprazole, rabeprazole, dexlansoprazole, cimetidine) and mineral products (calcium acetate, calcium phosphate, magnesium oxide): these may affect absorption.
  - Sympathomimetics (epinephrine, isometheptene, diethylpropion).

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and official contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or publication studies levothyroxine in renal hypodysplasia/aplasia, and the biological rationale is weak because these are structural, genetically driven developmental defects. The high TxGNN score is a computational signal only (evidence level L5).

**To proceed, the following is needed:**
- Any direct clinical or preclinical evidence that thyroid hormone alters renal development outcomes in this condition
- SAHPRA Professional Information (warnings, contraindications and approved indications) for Roidace 25
- Mechanism of action data
- If any pathway is pursued, Carney complex (thyroid management in a co-occurring condition) is the most plausible direction, but it still needs supporting studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

