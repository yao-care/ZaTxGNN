---
layout: default
title: Valsartan
parent: Moderate Evidence (L3-L4)
nav_order: 468
evidence_level: L4
indication_count: 6
last_modified_at: 2026-11-24
monitor_inn: "VALSARTAN"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease", "Prinzmetal angina"]
description: "Valsartan: predicted new indication Malignant hypertensive renal disease (evidence level L4). In South Africa: 255 SAHPRA registrations (216 valid)"
---

# Valsartan
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

## Valsartan: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Valsartan is an angiotensin II receptor blocker, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but currently there are **no registered clinical trials** and only **1 indirect publication** (a preclinical study of a different drug), so this prediction rests mainly on mechanistic plausibility.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L4 |
| South Africa Market Status | Marketed (valid licences: 216 of 255; 2 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 255 (valid: 216, of which 2 not confirmed by SAHPRA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for valsartan: "Angiotensin II is formed from angiotensin I in a reaction catalyzed by angiotensin-converting enzyme (ACE, kininase II). Angiotensin II is the principal pressor agent of the renin-angiotensin system, with effects that include vasoconstriction, stimulation of synthesis and release of aldosterone, cardiac stimulation, and renal reabsorption of sodium. […] Diovan (valsartan) blocks the vasoconstrictor and aldosterone-secreting effects of angiotensin II by selectively blocking the binding of angiotensin II to the AT 1 receptor in many tissues, such as vascular smooth muscle and the adrenal gland." ([DailyMed: Diovan (valsartan) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5ddba454-f3e6-43c2-a7a6-58365d297213), label version 2026-08-11; accessed 2026-11-19.) Based on known information, valsartan is an angiotensin II type 1 (AT1) receptor blocker, its efficacy in hypertension is established, and mechanistically it may be applicable to malignant hypertensive renal disease.

Malignant hypertensive nephropathy is driven largely by overactivation of the renin-angiotensin-aldosterone system (RAAS). Blocking the AT1 receptor is therefore biologically plausible. In practice, this condition is essentially a severe variant of the already-approved indication of hypertension.

An animal study (PMID 11560862) found that AT1 receptor blockade prevented lethal malignant hypertension, which supports the drug class mechanistically. However, ARBs can reduce renal function in bilateral renal artery stenosis, so clinical caution is needed.

Other lower-ranked predictions have weaker support:
- **Pulmonary hypertension (lung disease/hypoxia)** (0.9997): only preclinical or mechanistic papers, many involving the sacubitril/valsartan combination rather than valsartan alone (Evidence Level L4).
- **Pulmonary hypertension, unclear multifactorial mechanism** (0.9997) and **Braddock syndrome** (0.9996): no trials or literature (L5).
- **Chronic pulmonary heart disease** (0.9958): one Phase 1 trial not directly testing valsartan, plus heart-failure studies of sacubitril/valsartan (L4).
- **Prinzmetal angina** (0.9945): the only paper is not relevant, and standard therapy is calcium channel blockers and nitrates (L5).

## Clinical Trial Evidence

Currently no related clinical trials registered for malignant hypertensive renal disease.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24368192](https://pubmed.ncbi.nlm.nih.gov/24368192/) | 2014 | Preclinical (different drug) | Pharmacological Research | Avosentan, an endothelin antagonist (not valsartan), protected against hypertensive nephropathy in transgenic rats at doses that did not cause fluid retention. Indirect evidence only. |

## South Africa Market Information

Approved indication text and Essential Medicines List (EML) status are not available. The five main registrations are listed below.

<!-- review:begin za-lic-20261105-valsartan-1 -->

> **Review correction (2026-11-05)**: Originally stated: "All 20 registrations are valid single-ingredient registrations according to the data compiled. Approved indication text and Essential Medicines List (EML) status are not available." Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-valsartan-1 -->

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 36/7.1.3/0034 | Diovan | tablet | Valid |
| 36/7.1.3/0035 | Diovan | tablet | Valid |
| 36/7.1.3/0067 | Tareg | tablet | Valid |
| 36/7.1.3/0068 | Tareg | tablet | Valid |
| 36/7.1.3/0382 | Diovan | tablet | Valid |

Showing 5 of 255 registrations (valid registrations first).

<!-- licenses:end -->

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):** the TxGNN knowledge graph links valsartan to contraindications in the following areas:
- Liver and biliary: liver failure, liver disease, hepatic coma/encephalopathy, pancreatitis, gallbladder disease, neonatal jaundice
- Angioedema: including hereditary, acquired and RAAS-blocker-induced forms
- Renal: anuria, impaired renal function, renal artery obstruction
- Metabolic and electrolyte: diabetes mellitus, diabetic ketoacidosis, potassium deficiency, hypercalcaemia, hyperparathyroidism, gout/hyperuricaemia
- Other: systemic lupus erythematosus, neutropenia, agranulocytosis, hypotension

These come from graph edges and may partly reflect combination products (for example, those containing a thiazide diuretic), so they must be checked against the approved label.

**Drug Interactions:** 100 interactions were identified (20 shown in the data). Notable ones:
- **Major:** potassium bicarbonate and potassium chloride (risk of hyperkalaemia)
- **Moderate:** insulins (many formulations), exenatide, hydrocortisone, eluxadoline, polyethylene glycol with electrolytes

Please refer to the SAHPRA-approved Professional Information (PI) for official warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis (RAAS blockade in malignant hypertensive renal disease) is plausible and valsartan is widely marketed in South Africa. However, there are no clinical trials, and the only retrieved paper concerns a different drug in animals. Evidence is limited to model prediction and indirect mechanistic reasoning (L4).

**To proceed, the following is needed:**
- Valsartan-specific clinical or high-quality preclinical evidence in malignant hypertensive nephropathy
- SAHPRA package insert warnings and contraindications (not yet obtained, and needed for safety screening)
- Detailed mechanism of action data
- A renal safety plan, including monitoring of renal function and potassium, and screening for renal artery stenosis
- Review of the product-specific approved indications for the registrations

<!-- review:begin za-lic-20261124b-valsartan-1 -->

> **Review correction (2026-11-24)**: Originally stated: "approved indications for the 20 registrations" Corrected: this next-step item stated a fixed number of registrations that does not match the SAHPRA registration data as of 2026-11-23; the number was removed and the suggested step is unchanged. The Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261124b-valsartan-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "All 20 registrations are valid single-ingredient registrations according to the data compiled" | Corrected (revised 2026-11-24; earlier version kept in the record) | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Diovan (valsartan) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5ddba454-f3e6-43c2-a7a6-58365d297213) |
| 2026-11-24 | Corrected: "approved indications for the 20 registrations" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

