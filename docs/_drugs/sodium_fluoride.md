---
layout: default
title: Sodium Fluoride
parent: 僅模型預測 (L5)
nav_order: 412
evidence_level: L5
indication_count: 7
---

# Sodium Fluoride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Sodium Fluoride: From No Approved Indication to Epiglottitis (Prediction Signal Only)

## One-Sentence Summary

Sodium fluoride has no registered indication and is not currently marketed in South Africa; detailed mechanism-of-action data is also unavailable in this evidence pack. The TxGNN model predicts a possible association with **epiglottitis**, but this signal is supported by **0 clinical trials** and **0 publications** — it is a knowledge-graph similarity score with no direct evidentiary or mechanistic backing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — drug is unregistered/not marketed; mechanism of action also not available |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for sodium fluoride in this evidence pack, and the drug has no registered indication or SAHPRA licence on file. Based on generally known pharmacology, fluoride ion's biological activity is essentially limited to two areas: dental enamel remineralisation (inhibiting demineralisation and converting hydroxyapatite to fluorapatite) and, in its radiolabelled form (¹⁸F-NaF), use as a PET bone-imaging tracer. Neither of these activities has any established mechanistic link to epiglottitis, which is predominantly an acute bacterial/infectious upper-airway condition.

The TxGNN score of 99.92% reflects embedding-space similarity within the knowledge graph rather than a pharmacological or clinical rationale. With zero clinical trials and zero publications retrieved for the drug–disease pair, there is no independent evidence to corroborate the prediction. This places the candidate at the lowest evidence tier (L5): a model-only signal that has not yet been tested against real-world or mechanistic data.

It is also worth noting that all seven TxGNN-predicted indications for sodium fluoride in this evidence pack (epiglottitis, urinary tract infection, gonococcal urethritis, Ureaplasma urethritis, uterine inflammatory disease, xanthogranulomatous pyelonephritis, laryngitis) share this same pattern — high embedding scores with essentially no supporting mechanistic or clinical evidence. The one exception, laryngitis, retrieved 5 publications, but on review none of them support a treatment effect (three are incidental ¹⁸F-NaF PET/CT imaging case reports in cancer patients, one is an unrelated diphtheria-toxin cell culture study, and one is an unrelated poultry-diet fluoride toxicity study).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Sodium fluoride is not currently registered with SAHPRA and has no marketed products on file in South Africa (0 licences, market status: not marketed).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (epiglottitis) is supported only by a TxGNN embedding score, with no clinical trials, no literature, and no plausible mechanistic link identified. Combined with the absence of SAHPRA registration and missing mechanism-of-action data, there is currently no basis to advance this candidate beyond the prediction stage.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data for sodium fluoride (DrugBank query currently unresolved)
- Product Information/label data (warnings, contraindications, DDI) if SAHPRA registration is ever pursued
- Targeted preclinical or mechanistic studies exploring any plausible fluoride–epiglottitis pathway before any clinical investigation is considered
- Re-screening against updated literature/trial registries, since the current pull returned zero hits for the epiglottitis indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

