---
layout: default
title: Haloperidol
parent: Model Prediction Only (L5)
nav_order: 250
evidence_level: L5
indication_count: 9
monitor_inn: "HALOPERIDOL"
predicted_indications: ["congenital disorder of glycosylation with defective fucosylation", "retinal dystrophy with or without extraocular anomalies", "hydranencephaly (disease)", "myopia X-linked", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "myopia 26, X-linked, female-limited", "syndromic myopia", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "atypical glycine encephalopathy"]
last_modified_at: 2026-11-17
description: "Haloperidol: predicted new indication congenital disorder of glycosylation with defective fucosylation (evidence level L5). In South Africa: 16 SAHPRA registrations (4 valid)"
---

# Haloperidol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Haloperidol: dopamine D2 receptor antagonist (butyrophenone antipsychotic) → congenital disorder of glycosylation with defective fucosylation
{: .text-alpha }

## One-Sentence Summary

Haloperidol is a butyrophenone antipsychotic that blocks dopamine D2 receptors and is marketed in South Africa as oral tablets.
The TxGNN model predicts it may be relevant for **congenital disorder of glycosylation with defective fucosylation**,
but **no clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | congenital disorder of glycosylation with defective fucosylation |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 4 of 16) |
| Number of SAHPRA Registrations | 16 (valid: 4) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for haloperidol: "The mechanism of action of haloperidol decanoate for the treatment of schizophrenia in adults is unclear. However, its effect in schizophrenia could be mediated through its activity as an antagonist at central dopamine type 2 receptors." ([DailyMed: haloperidol decanoate prescribing information, BluePoint Laboratories](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3d011250-a517-4c27-8ce3-d59d441ea61c), label version 2026-11-03; accessed 2026-11-19.) Haloperidol is generally known as a dopamine D2 receptor antagonist.

For this prediction, no plausible mechanistic link could be identified. Congenital disorders of glycosylation with defective fucosylation involve fucose metabolism or transport (for example, GDP-fucose transport), and nothing in the compiled data connects dopamine D2 blockade to these pathways. The high TxGNN score is a purely computational output and has not been corroborated by any trial, publication or preclinical study. It should be treated as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 42/2.6.5/0065 | Gulf haloperidol | tablet | Valid |
| Q/2.6.5/169 | Haloperidol 1.5 oethmaan | tablet | Valid |
| Q/2.6.5/170 | Sandoz Haloperidol 5 | tablet | Valid |
| 56/2.6.5/0059 | Amperi 5Mg/Ml | injection | Valid |
| B/2.6.5/10 | Serenace 0.5Mg Capsules | capsule | Not on SAHPRA register; discontinued in MPR |

Showing 5 of 16 registrations (valid registrations first).

<!-- licenses:end -->

Essential Medicines List (EML) status is not available in the data compiled for this report.

<!-- review:begin za-lic-20261105-haloperidol-1 -->

> **Review correction (2026-11-05)**: Originally stated: "Both registrations are valid single-ingredient oral tablet products. Essential Medicines List (EML) status is not available in the data compiled for this report." Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 16 registrations for this drug, 8 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-haloperidol-1 -->

---

## Safety Considerations

- **Contraindications and conditions of concern (not label text):** The data compiled for this report flag caution in long QT syndrome and torsades de pointes, epilepsy, basal ganglia disease, liver disease, hypothyroidism, potassium deficiency, neutropenia, agranulocytosis and leukopenia, hypotension, and neuroleptic malignant syndrome. These should be verified against the SAHPRA-approved Professional Information (PI).
- **Drug Interactions:** 100 interactions are recorded. Examples classed as **Major**: bupropion, morphine, clarithromycin and dolasetron. Examples classed as Moderate: famotidine, epinephrine, hydrocortisone, amphotericin B, atropine and loperamide.

Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting trials, literature or plausible mechanism, so the evidence level is L5. There is no basis for clinical use in this condition.

**To proceed, the following is needed:**
- A plausible mechanistic rationale linking haloperidol to fucosylation pathways, with preclinical (cell or animal model) evidence
- Detailed mechanism of action data
- SAHPRA Professional Information warnings and contraindications for formal safety screening
- A risk-benefit assessment for the target population, given the QT, extrapyramidal and haematological safety concerns

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "Both registrations are valid single-ingredient oral tablet products" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: haloperidol decanoate prescribing information, BluePoint Laboratories](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3d011250-a517-4c27-8ce3-d59d441ea61c) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

