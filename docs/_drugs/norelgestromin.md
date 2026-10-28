---
layout: default
title: Norelgestromin
parent: Model Prediction Only (L5)
nav_order: 347
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-29
description: "Norelgestromin: predicted new indication Amenorrhoea (evidence level L5). Approved use: Not stated in the registration data compiled for this report (the pro…"
monitor_inn: "NORELGESTROMIN"
predicted_indications: ["amenorrhea (disease)"]
---

# Norelgestromin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Norelgestromin: From Contraception to Amenorrhoea
{: .text-alpha }

## One-Sentence Summary

Norelgestromin is a progestin delivered through a transdermal contraceptive patch (Evra), registered in South Africa for hormonal contraception use.
The TxGNN model predicts it may be effective for **amenorrhoea**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so this is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data compiled for this report (the product is a contraceptive patch) |
| Predicted New Indication | Amenorrhoea |
| TxGNN Prediction Score | 0.9951 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 1 of 1) |
| Number of SAHPRA Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, norelgestromin is the active progestin metabolite of norgestimate and is delivered in a transdermal patch together with ethinyl estradiol. As a progestin, it acts on progesterone receptors and suppresses the hypothalamic-pituitary-ovarian axis.

Progestins are used in some amenorrhoea settings, for example to induce withdrawal bleeding or to provide cycle control and endometrial protection in hormone-deficient states. A mechanistic rationale is therefore plausible.

However, the direction of effect is ambiguous. Hormonal contraceptives can themselves suppress menses or cause amenorrhoea, so the drug could help in some settings and cause the problem in others. The very high TxGNN score is a computational prediction only, with no supporting trial or publication in the data compiled for this report. Clinical interpretation is needed before this is treated as a genuine repurposing candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 36/18.7/0491 | Evra | Patch | Not stated in the data compiled for this report |

Essential Medicines List (EML) inclusion status could not be determined from the data compiled for this report.

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** The TxGNN knowledge graph links norelgestromin to contraindications in the following areas:
  - Cardiovascular and metabolic: hypertension, coronary artery disease, thrombophlebitis, hyperlipidaemia (including familial), hypertriglyceridaemia, diabetes mellitus, diabetic ketoacidosis, hyperglycaemia
  - Hepatic, renal and biliary: liver disease, gallbladder disease, kidney disease, pyoureter
  - Neurological and psychiatric: epilepsy, migraine (including with aura), anxiety disorder, neurotic disorder, dysthymic disorder
  - Metabolic and autoimmune: porphyria (inherited porphyria, porphyrin metabolism disease), systemic lupus erythematosus (including paediatric), asthma (intrinsic and allergic)
  - Other: female breast carcinoma, functional visual loss
- **Drug Interactions:** One interaction was identified: **Sugammadex** (Major, DDInter).

These signals must be confirmed against the SAHPRA-approved Professional Information (PI). Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no clinical trials or publications. The direction of effect is also unclear, since hormonal contraceptives can cause amenorrhoea. The SAHPRA package insert safety data has not been obtained, which blocks safety screening.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings, contraindications and approved indication text)
- Mechanism of action data (e.g. from DrugBank)
- Systematic literature and trial searches for progestin or contraceptive use in primary and secondary amenorrhoea, clarifying whether the drug treats or causes amenorrhoea
- Assessment of route and formulation suitability, since only a transdermal patch is registered
- Review of the knowledge-graph contraindications (cardiovascular, thromboembolic, hepatic, migraine) against the intended patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

