---
layout: default
title: Mannitol
parent: Model Prediction Only (L5)
nav_order: 309
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Mannitol: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Congestive heart failure, brain oedema, ocular hypertension…"
monitor_inn: "Mannitol"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "acute pulmonary heart disease", "exercise-induced malignant hyperthermia", "malignant hyperthermia, susceptibility to", "familial periodic paralysis", "hypokalemic periodic paralysis", "congenital multicore myopathy with external ophthalmoplegia", "moderate multiminicore disease with hand involvement", "nephrogenic diabetes insipidus", "King-Denborough syndrome"]
---

# Mannitol
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

## Mannitol: From Congestive Heart Failure and Raised Intracranial Pressure to Nephrogenic Syndrome of Inappropriate Antidiuresis
{: .text-alpha }

## One-Sentence Summary

Mannitol is an osmotic diuretic, listed for conditions such as brain oedema, intracranial hypertension, ocular hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis**,
but there are **no registered clinical trials** and only **1 general review article** behind this prediction, and that review contains no mannitol-specific data.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Congestive heart failure, brain oedema, ocular hypertension, pseudotumor cerebri, intracranial hypertension, cystic fibrosis (from the knowledge graph; the SAHPRA record has no indication text) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, mannitol is an osmotic diuretic. It is filtered by the kidney but not reabsorbed, so it draws water into the urine and lowers pressure in fluid-filled compartments such as the brain and eye.

A theoretical link to disordered water handling therefore exists. However, nephrogenic syndrome of inappropriate antidiuresis is a condition of excessive water retention with low serum sodium. Mannitol raises serum osmolality and could worsen the dynamics of hyponatraemia, so the mechanism is more likely to cause harm than benefit. The high TxGNN score appears to reflect network proximity in the knowledge graph rather than a plausible therapeutic mechanism.

Other predictions in the list (ranks 3 to 10) mostly reflect indirect associations. For example, mannitol is an excipient in some intravenous dantrolene products and a diluent for potassium infusions in periodic paralysis. These do not represent therapeutic activity of mannitol itself.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | Eur J Intern Med | Common pitfalls in evaluating and treating hyponatraemia, including the risks of overtreatment. It contains no mannitol-specific data. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SX/34/0266 | Cardioplegic soln a 1000ml sxa3020 | Infusion | Not stated in the registration record |

This single registration is a cardioplegic solution, not a standalone mannitol osmotic diuretic product. Essential Medicines List status is not available in the data compiled for this report.

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these come from drug-disease links, not from label text, and need verification against the Professional Information): anuria, impaired renal function, pulmonary oedema, intracranial haemorrhage, liver failure, hepatic coma and encephalopathy, liver and gallbladder disease, porphyria, thrombocytopenia, neutropenia, agranulocytosis, anaemia, anxiety and neurotic disorders, dysthymic disorder, substance abuse or dependence, and sleep apnoea syndromes.
- **Drug interactions:** 100 interactions were identified, of which 20 are listed here. One is rated **Major**: **amikacin**. Most of the others are **Moderate**, including lamivudine, formoterol, salbutamol, arformoterol, amifostine, benazepril, captopril, bisacodyl, canagliflozin, dapagliflozin, carbamazepine, cisatracurium, citalopram, desvenlafaxine, picosulfuric acid, polyethylene glycol with electrolytes, iothalamic acid and diatrizoate. Doxycycline is rated **Minor**.
- **Indication-specific concern:** the literature describes mannitol precipitating pulmonary oedema in patients with water intoxication, and expanding intravascular volume in patients with heart or kidney dysfunction.

Warnings and contraindications from the SAHPRA-approved Professional Information (PI) were not available for this report. Please refer to the PI for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. No trials exist, the single review is not specific to mannitol, and mannitol's osmotic action may worsen water and sodium imbalance in this condition. The other nine predicted indications are also at Hold, with evidence limited to L4 or L5.

**To proceed, the following is needed:**
- Mechanism of action data and a mechanistic assessment showing a plausible benefit in nephrogenic syndrome of inappropriate antidiuresis rather than harm
- SAHPRA Professional Information, including warnings and contraindications, to complete the safety screen
- Clarification of the registered product, since the only SAHPRA registration is a cardioplegic solution
- Any mannitol-specific clinical or case data for this condition; none were found
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

