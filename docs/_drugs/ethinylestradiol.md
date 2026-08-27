---
layout: default
title: Ethinylestradiol
parent: 僅模型預測 (L5)
nav_order: 213
evidence_level: L5
indication_count: 1
---

# Ethinylestradiol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Ethinylestradiol: From Hormonal Contraception to Zinc, Elevated Plasma

## One-Sentence Summary

> Ethinylestradiol is a synthetic estrogen; the evidence pack does not specify its original indication in South African regulatory records, though the supporting literature describes it in the context of combined oral contraceptive use.
> The TxGNN model predicts a possible association with **Zinc, Elevated Plasma**, but this is currently supported only by **0 clinical trials** and **2 older literature reports** — both of which actually describe the *opposite* direction (oral contraceptives lowering, not raising, plasma zinc).
> Given this direct contradiction and multiple missing data points, this candidate does not currently support a "Go" decision.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (no `original_indications` or SAHPRA license data provided; literature context refers to combined oral contraceptive products) |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for ethinylestradiol in this evidence pack. Based on the supporting literature, ethinylestradiol is known clinically as a component of combined oral contraceptive formulations, where it is understood to alter hepatic synthesis of plasma-binding proteins (e.g. ceruloplasmin) and thereby influence trace-element distribution in blood.

However, the mechanistic direction reported in the literature does **not** support the TxGNN prediction. The two cited studies (Sing et al., 1978; Lei et al., 1976) both describe oral contraceptive/estrogen exposure **lowering** plasma zinc levels (while raising plasma copper), not elevating them. "Zinc, elevated plasma" is also not a well-established clinical disease entity, and may reflect a graph-relationship artifact in the TxGNN knowledge graph rather than a genuine pharmacological signal.

Because the original indication, MOA, and South African regulatory status are all unavailable or absent for this drug, there is currently no independent basis to corroborate or contextualize this prediction beyond the contradictory literature noted above.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [736629](https://pubmed.ncbi.nlm.nih.gov/736629/) | 1978 | Cohort | Archives of Gynecology | In women taking oral contraceptives (Ovulen-21, Demulen, Enovid-E, Ovral), plasma and endometrial **copper** rose significantly; plasma **zinc remained essentially unchanged** — no elevation observed. |
| [961877](https://pubmed.ncbi.nlm.nih.gov/961877/) | 1976 | Cohort (animal) | American Journal of Physiology | In rats, mestranol (a related estrogen) **depressed** plasma zinc along with tibial copper and magnesium — direction opposite to the predicted indication. |

---

## South Africa Market Information

No SAHPRA registrations are recorded in the evidence pack (`total_licenses: 0`); the drug's South African market status is Not Marketed. No product/dosage-form table is available.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The only available literature evidence directly contradicts the direction of the predicted indication (oral contraceptive/estrogen exposure is associated with *lower*, not elevated, plasma zinc), and no clinical trial evidence exists at all. Combined with missing MOA and safety data, this does not meet the bar to proceed.

**To proceed, the following is needed:**
- TFDA/SAHPRA-equivalent Professional Information (warnings and contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action data from DrugBank or equivalent source — currently a High-severity data gap (DG002)
- Independent resolution of the mechanistic direction conflict (does estrogen exposure raise or lower plasma zinc in humans?)
- Clarification of "zinc, elevated plasma" as a clinically meaningful, actionable indication before further evaluation
- Confirmation of South African regulatory/market status specific to this jurisdiction, since current data reflects an absence of local licensing records rather than a confirmed non-marketed determination
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

