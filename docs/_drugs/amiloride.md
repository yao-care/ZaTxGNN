---
layout: default
title: Amiloride
parent: Moderate Evidence (L3-L4)
nav_order: 25
evidence_level: L4
indication_count: 6
---

# Amiloride
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

# Amiloride: From Potassium-Sparing Diuretic Use to Malignant Renovascular Hypertension

## One-Sentence Summary

Amiloride is an oral potassium-sparing diuretic that blocks the epithelial sodium channel (ENaC). It is marketed in South Africa mainly in combination tablets. The TxGNN model predicts it may be useful for **malignant renovascular hypertension**, but there are currently **0 registered clinical trials** and only **1 indirectly related review** supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA records provided (all four registrations have blank indication text) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in DrugBank for this record. Based on general pharmacology, amiloride blocks ENaC in the distal nephron, which reduces sodium reabsorption and conserves potassium. It is a recognised option for mineralocorticoid-type hypertension, where excess sodium retention and hypokalaemia drive the high blood pressure. This gives a plausible pathway to hypertension in general.

The link to the predicted indication is weak, though. Malignant renovascular hypertension is driven mainly by renin-angiotensin activation from renal artery stenosis, not by primary sodium-channel overactivity. No retrieved record shows amiloride being used or tested in this setting. The model score most likely reflects the drug's general antihypertensive profile and its position in the knowledge graph.

The other predictions are weaker still. Malignant hypertensive renal disease and the two pulmonary hypertension entries are model-only, with no relevant trials or literature. One further prediction, chronic pulmonary heart disease (score 99.68%), has some indirect support. It comes from small heart failure studies of amiloride as an add-on diuretic, plus a rat study of increased alveolar fluid reabsorption. That is a possible research question, but not direct evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov, ICTRP, SANCTR or PACTR records were not found in the Evidence Pack).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12929904](https://pubmed.ncbi.nlm.nih.gov/12929904/) | 2003 | Review | J Hypertens Suppl | Overview of investigating mineralocorticoid hypertension: hypokalaemic hypertension with low plasma renin is the typical finding, and primary aldosteronism is the most frequent cause. It gives general context for sodium-driven hypertension and does not address renovascular hypertension directly. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Q/18.1/168 | Sandoz Co-Amilozide | Tablet | Not stated in the record |
| V/18.1/260 | Adco-retic 50mg/5mg | Tablet | Not stated in the record |
| L/18.1/396 | Amiloretic | Tablet | Not stated in the record |
| U/18.1/0040 | Amiloretic hs 25mg/2.5mg | Tablet | Not stated in the record |

All four products are oral tablets. Essential Medicines List inclusion was not verified from the data provided.

---

## Safety Considerations

- **Hyperkalaemia signal**: A case report retrieved for a related indication (PMID 8615380) describes severe hyperkalaemia (potassium 9.3 meq/L) in a 96-year-old woman receiving trimethoprim-sulfamethoxazole. Amiloride was among the contributing drugs in that report. It is a reminder that potassium-sparing agents carry this risk, especially in older patients, in renal impairment, and when combined with other potassium-raising drugs. Renovascular disease often involves impaired renal function, which makes this especially relevant.
- **Drug interactions**: No interaction records were found in the query.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score and general pharmacology. There are no clinical trials, and the only related paper is a general review of mineralocorticoid hypertension. The mechanism of malignant renovascular hypertension (renin-angiotensin driven) also does not match amiloride's primary action well, and potassium risk is a concern in patients with renal artery disease.

**To proceed, the following is needed:**
- The SAHPRA package insert warnings, contraindications and approved indications, which are blocking for safety screening
- Mechanism of action data from DrugBank
- Any direct clinical or preclinical evidence of amiloride in renovascular or malignant hypertension
- A potassium and renal function monitoring plan for this patient group
- Consideration of chronic pulmonary heart disease as a better-supported research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

