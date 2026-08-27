---
layout: default
title: Misoprostol
parent: 僅模型預測 (L5)
nav_order: 320
evidence_level: L5
indication_count: 2
---

# Misoprostol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Misoprostol: From Labour Induction/Pregnancy Termination to Amenorrhea

## One-Sentence Summary

> Misoprostol is a PGE1 analogue whose established clinical roles — per the evidence pack's own mechanistic notes — are inducing uterine contractions, cervical ripening, and (combined with mifepristone) pregnancy termination/missed abortion management.
> The TxGNN model predicts it may be effective for **amenorrhea (disease)**, with **0 clinical trials** and **7 publications** currently associated with this pairing — and critically, none of those publications study misoprostol as a *treatment* for amenorrhea.
> The evidence pack itself flags this as a likely knowledge-graph proximity artifact rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — the pack contains no `original_indications` or Taiwan/SAHPRA licence text; known clinical role (per rationale notes) is labour induction / cervical ripening / pregnancy termination |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L4 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this pack (flagged as a Blocking/High-severity data gap). Based on the mechanistic notes that are available, misoprostol is a PGE1 analogue whose pharmacological effect is to induce uterine contraction and cervical softening — i.e., to promote expulsion of uterine contents and bleeding. This is the mechanism exploited for labour induction, cervical preparation, and (with mifepristone) termination of pregnancy or management of missed abortion.

Amenorrhea, by contrast, generally requires mechanisms that *restore or induce* a menstrual cycle (hormonal regulation), which is functionally the opposite of what misoprostol does. The evidence pack's own repurposing rationale is explicit on this point: the seven associated publications are almost entirely about medical abortion, missed abortion, and endometrial ablation for heavy bleeding — not about treating amenorrhea. The pack's assessment is that the high TxGNN score most likely reflects graph proximity within a "female reproductive system" cluster rather than a real pharmacological signal.

A second, lower-ranked prediction in this pack (atypical coarctation of aorta, score 99.30%, evidence level L5) is even weaker: no clinical trials, no literature, and no known mechanistic pathway connecting a uterotonic/gastric-protective prostaglandin to a structural aortic anomaly. It is noted here for completeness but is not pursued further in this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | RCT | Reproductive Sciences | Low-dose mifepristone + self-administered misoprostol for ultra-early medical abortion (amenorrhea ≤35 days used only as a pregnancy-dating criterion, not as the treated condition) |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | RCT | Reproductive Sciences | Dose-ranging RCT of lower-dose mifepristone + misoprostol (200 µg) for termination of ultra-early pregnancy |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Cohort | Human Reproduction | Low-dose mifepristone + misoprostol before expected menstruation for unintended pregnancy prevention |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Cohort | J Obstet Gynaecol Res | Safety/efficacy of self-administered low-dose mifepristone + misoprostol for early medical abortion |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Review | BMJ | Medical management of missed abortion and anembryonic pregnancy |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Review | J Obstet Gynaecol Can | Endometrial ablation for abnormal uterine bleeding (does not evaluate misoprostol or amenorrhea treatment) |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Case Report | Cureus | Acute fatty liver of pregnancy case report; amenorrhea appears only as a presenting symptom, not as a treated indication |

None of these publications evaluate misoprostol as a therapeutic agent *for* amenorrhea; the association is indirect (shared reproductive-medicine context).

---

## South Africa Market Information

Misoprostol has **0 SAHPRA registrations** on file in this evidence pack and is classified as **Not Marketed** in South Africa. No product registrations, dosage forms, or approved indication text are available to summarize.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted amenorrhea indication has no clinical trials and no literature that actually studies misoprostol as a treatment for amenorrhea — the associated publications are about pregnancy termination and heavy uterine bleeding, mechanistically distinct from (and largely opposite to) restoring menstrual function. The pack's own rationale assesses this as a likely knowledge-graph artifact rather than a genuine signal.
- Misoprostol is not currently registered or marketed in South Africa (0 SAHPRA registrations), so there is no existing regulatory foothold to build a repurposing pathway on.
- The secondary prediction (atypical coarctation of aorta) is even weaker (L5, no trials, no literature, no plausible mechanism) and does not warrant further evaluation.

**To proceed, the following is needed:**
- SAHPRA/TFDA-equivalent Professional Information (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism of action data from DrugBank — currently a High-severity data gap
- Clarification of what "amenorrhea" denotes in this context (e.g., confirming non-pregnant status vs. therapeutic induction of menses) before any further evidence search is worthwhile
- Original/reference indication data (South Africa or another jurisdiction) to properly assess mechanistic overlap with the predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

