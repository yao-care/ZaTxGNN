---
layout: default
title: Ferrous Sulfate Anhydrous
parent: Model Prediction Only (L5)
nav_order: 228
evidence_level: L5
indication_count: 4
---

# Ferrous Sulfate Anhydrous
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Ferrous Sulfate Anhydrous: From Iron Supplementation to Vitamin B12- and Folate-Independent Constitutional Megaloblastic Anemia

## One-Sentence Summary

Ferrous sulfate anhydrous is an oral iron salt. In South Africa it is registered only inside combination capsule products, and no approved indication text was recorded for them.
The TxGNN model predicts it may be useful for **vitamin B12- and folate-independent constitutional megaloblastic anemia** with a very high score, but **no clinical trials and no publications** support this prediction.
The prediction is therefore on hold. Among the other model predictions, **Plummer-Vinson syndrome** is the most biologically plausible and is worth a targeted evidence search.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA registration data supplied |
| Predicted New Indication | Vitamin B12- and folate-independent constitutional megaloblastic anemia |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ferrous sulfate is an iron salt used to replace iron, which is needed for haemoglobin synthesis and red cell production. Its role in iron-deficiency states is well established, but this cannot be checked against the registration data supplied.

For the top prediction, the mechanistic support is weak. Megaloblastic anemia is a defect in DNA synthesis, not a shortage of iron. Iron would help only if iron deficiency coexists. The high score likely reflects shared anemia-related nodes in the knowledge graph rather than a true therapeutic link.

The other three predictions vary in plausibility:

| Predicted Indication | TxGNN Score | Assessment |
|------|------|------|
| Plummer-Vinson syndrome | 99.77% | Plausible. It is classically linked with iron-deficiency anemia, dysphagia and esophageal webs, so iron repletion makes sense. Marked as a research question. |
| Biotin metabolic disease | 99.51% | No plausible mechanism. These disorders are enzymatic defects that iron does not address. Likely a graph-proximity artifact. |
| Non-syndromic esophageal malformation | 99.49% | No plausible mechanism. These are structural congenital anomalies, and the score probably reflects a graph link to Plummer-Vinson syndrome. |

Any upgrade in evidence level should rest on retrieved studies, not on background knowledge.

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov, ICTRP, SANCTR or PACTR).

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

The pack lists 5 registration entries, but two registration numbers appear twice. There are only 3 distinct registrations.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H2466 | Complenatal Ff | Capsule | Not recorded in the data supplied |
| G2667 (ACT 101/1965) | Gericomplex | Capsule | Not recorded in the data supplied |
| 41/10.2.1/0849 | Spiriva respimat inhaler 60 doses | Inhaler | Not recorded in the data supplied |

The Spiriva Respimat entry is an inhaler and is unlikely to contain an oral iron salt. It looks like a mapping error and should be checked against the SAHPRA register. Essential Medicines List (EML) status was not part of the data supplied.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction scores very high, but it is supported only by the model (L5). The top-ranked indication has weak biological plausibility, because megaloblastic anemia is not an iron-supply problem. Plummer-Vinson syndrome is the only prediction with a credible mechanism, and it needs its own evidence review.

**To proceed, the following is needed:**
- SAHPRA Professional Information (PI) for the registered products, to complete safety screening. This is currently blocking.
- Approved indication text and ingredient confirmation for each registration. This includes resolving the Spiriva Respimat entry and the duplicate rows.
- Mechanism of action data for ferrous sulfate from DrugBank.
- A targeted PubMed and ClinicalTrials.gov search for iron therapy in Plummer-Vinson syndrome, which could raise its evidence level.
- Confirmation of whether iron deficiency coexists in the megaloblastic anemia setting, before any further consideration.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

