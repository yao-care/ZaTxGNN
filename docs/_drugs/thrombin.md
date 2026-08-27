---
layout: default
title: Thrombin
parent: 僅模型預測 (L5)
nav_order: 436
evidence_level: L5
indication_count: 10
---

# Thrombin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

Using the evidence pack as provided — including the reviewers' own grading and mechanistic-rationale notes embedded in `predicted_indications[0]` — here is the evaluation report.

# Thrombin: From Topical Haemostasis to Primary Release Disorder of Platelets

## One-Sentence Summary

Thrombin is a coagulation serine protease used clinically as a topical/local haemostatic agent to control bleeding. The TxGNN model predicts a possible new application in **Primary Release Disorder of Platelets** (a platelet granule-release defect), with a prediction score of **96.82%**, but this signal is currently supported by **0 directly relevant clinical trials** and **0 publications** — expert review classifies it as a low-confidence, likely false-positive prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication on file (not marketed in South Africa); internationally recognised as a topical/local haemostatic agent |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 96.82% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Thrombin is not available in this evidence pack (flagged as a High-severity data gap). Based on well-established pharmacology, Thrombin is the terminal serine protease of the coagulation cascade — it converts fibrinogen to fibrin and is a potent agonist of platelet protease-activated receptors (PARs), triggering platelet activation and granule release. Clinically it is used as a topical/local haemostatic agent (e.g., surgical field haemostasis, endoscopic injection for bleeding varices) rather than as a systemic treatment for platelet disorders.

Primary Release Disorder of Platelets is a disease of impaired platelet granule storage and release — affected platelets fail to properly discharge granule contents (ADP, serotonin, coagulation factors) even when normally stimulated. The reviewer's mechanistic assessment notes that Thrombin can activate the PAR pathway and theoretically trigger release, but exogenous thrombin cannot repair the intrinsic granule-storage/release defect that defines this disease — the "mechanistic link" runs only as far as shared vocabulary in the knowledge graph ("platelet" + "thrombin" co-occurrence), not a genuine treatment rationale.

This is corroborated by the evidence search itself: of 50 clinical trials retrieved by keyword matching, none directly tests thrombin as a treatment for this condition, and no literature was retrieved at all. For these reasons, this specific prediction should be treated as probable model noise rather than a genuine repurposing opportunity.

## Clinical Trial Evidence

Currently no clinical trial directly evaluates Thrombin for the treatment of Primary Release Disorder of Platelets. A broad automated search returned 50 trials matching platelet/coagulation-related keywords, but these were thematically unrelated (COVID-19 coagulopathy, cardiac/trauma bleeding management, oncology trials, etc.). Two of the retrieved trials were formally reviewed and graded as irrelevant:

| Trial Number | Phase | Status | Enrollment | Reviewer Assessment |
|---------|------|------|------|---------|
| [NCT00043940](https://clinicaltrials.gov/study/NCT00043940) | Phase 3 | Completed | 50 | Bivalirudin anticoagulation in heparin-induced thrombocytopenia (HIT) — unrelated to thrombin supplementation; excluded (Grade C) |
| [NCT06710327](https://clinicaltrials.gov/study/NCT06710327) | Phase 4 | Not Yet Recruiting | 56 | Tranexamic acid for intraoperative blood loss in BPH surgery — different drug class and mechanism; excluded (Grade C) |

The remaining 48 trials in the search results are unreviewed ("pending") but, on title inspection, cover unrelated conditions (COVID-19, cardiac surgery, oncology, obesity, etc.) and were not included above as none show topical relevance to this predicted indication.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Thrombin currently holds no SAHPRA registration and is not marketed in South Africa. As a result, no local product name, dosage form, or approved-indication text is available for review.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA. Note: SAHPRA labelling data (warnings/contraindications) is currently recorded as a **Blocking** data gap, which by itself prevents this candidate from entering initial safety screening.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The TxGNN prediction for Primary Release Disorder of Platelets is not supported by any directly relevant clinical trial or literature evidence, and mechanistic review concludes it most likely reflects keyword co-occurrence ("platelet"/"thrombin") in the knowledge graph rather than genuine therapeutic potential — the target disease is a platelet granule-release defect that exogenous thrombin cannot correct.
- Thrombin is not currently registered or marketed in South Africa (0 SAHPRA registrations), and essential safety data (PI warnings/contraindications, confirmed mechanism of action) are recorded as data gaps, with the SAHPRA labelling gap classified as Blocking.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI), including warnings, contraindications, and drug interaction data
- Confirmed mechanism-of-action data from DrugBank or peer-reviewed pharmacology sources
- A genuine mechanistic or clinical rationale connecting thrombin to a platelet granule-release disorder, which is not present in the current evidence base

**Note for reviewers:** Among the ten TxGNN-predicted indications generated for Thrombin in this evidence pack, *"Esophageal Disease"* — specifically gastric/esophageal variceal bleeding managed by endoscopic thrombin injection — shows substantially stronger evidence (Evidence Level L3, multiple cohort studies plus a systematic review/meta-analysis, "Proceed with Guardrails" recommendation), reflecting thrombin's already-established use as a local haemostatic agent. That candidate may warrant a separate, dedicated evaluation report rather than the low-confidence signal assessed here.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

