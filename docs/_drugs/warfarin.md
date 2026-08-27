---
layout: default
title: Warfarin
parent: 僅模型預測 (L5)
nav_order: 463
evidence_level: L5
indication_count: 10
---

# Warfarin
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

# Warfarin: From Anticoagulation Therapy to Heparin Cofactor II Deficiency

## One-Sentence Summary

Warfarin is a long-established oral vitamin K antagonist used internationally for venous thromboembolism, atrial fibrillation, and mechanical heart valve thromboprophylaxis, though it currently holds no SAHPRA registration in South Africa. TxGNN predicts a potential role in **Heparin Cofactor II Deficiency**, a rare congenital thrombophilia, with the prediction currently supported only by **5 publications** (case reports, a methodology paper, and a review) and **no dedicated clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — Warfarin has no SAHPRA-registered product in South Africa, so no approved-indication text exists in the regulatory data; internationally it is used as an oral anticoagulant |
| Predicted New Indication | Heparin Cofactor II Deficiency |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for warfarin is not available in this evidence pack (flagged as a High-severity data gap). However, the model's own rationale for this candidate identifies warfarin as a **vitamin K epoxide reductase inhibitor**, which lowers the activity of clotting factors II, VII, IX, and X.

Heparin cofactor II deficiency is a rare inherited thrombophilia in which patients carry an elevated lifetime risk of venous and arterial thrombosis. Warfarin is the established standard anticoagulant for preventing recurrent thrombotic events in inherited thrombophilias generally — the mechanistic link here is to secondary thromboprophylaxis in affected patients, not to correcting the underlying cofactor deficiency itself.

This candidate does not stand alone: the same evidence pack surfaces three closely related, mechanistically consistent predictions — Factor V excess with spontaneous thrombosis, Antithrombin deficiency type 2, and Thrombophilia in general (the last of these has substantially stronger evidence: 14 clinical trials and 20 publications, evidence level L2). Together these form a coherent cluster around warfarin's known anticoagulant activity in inherited hypercoagulable states, which strengthens biological plausibility even though direct evidence for heparin cofactor II deficiency specifically remains sparse.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11177584](https://pubmed.ncbi.nlm.nih.gov/11177584/) | 2001 | Review | AIDS Patient Care and STDs | Review of thrombotic complications in HIV/AIDS, including acquired protein C/S and antithrombin/heparin cofactor deficiencies predisposing to a hypercoagulable state |
| [2214444](https://pubmed.ncbi.nlm.nih.gov/2214444/) | 1990 | Case Report | Kyobu Geka | 14-year-old with familial heparin cofactor II deficiency presenting with a right ventricular thrombus, managed surgically |
| [3778142](https://pubmed.ncbi.nlm.nih.gov/3778142/) | 1986 | Methodology/Lab | Archives of Pathology & Laboratory Medicine | Laboratory method for heparin cofactor II activity; low levels associated with liver disease, consumptive coagulopathy, and pre-eclampsia |
| [11570053](https://pubmed.ncbi.nlm.nih.gov/11570053/) | 2001 | Case Report | Journal of UOEH | Family with recurrent thrombosis (including infantile onset) not explained by known hereditary thrombophilias; recurrence occurred despite warfarin therapy |
| [2033902](https://pubmed.ncbi.nlm.nih.gov/2033902/) | 1991 | Case Report | Nihon Kyobu Shikkan Gakkai Zasshi | 48-year-old with congenital antithrombin II deficiency and pulmonary infarction, treated with warfarin for 7 years before a switch to heparin |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is sound and consistent with warfarin's well-established role in inherited thrombophilia, but direct evidence for heparin cofactor II deficiency specifically is limited to case reports and a lab-methodology paper — no trials or systematic reviews exist for this exact indication.

**To proceed, the following is needed:**
- SAHPRA-approved warfarin PI (key warnings and contraindications) — currently a blocking data gap for safety review
- Formal mechanism-of-action documentation from DrugBank/PI to support the mechanistic-link analysis
- Confirmation of an access pathway in South Africa, since warfarin holds no current SAHPRA registration (e.g., Section 21 named-patient access, given this is an ultra-rare congenital indication)
- Drug-drug interaction data, as none is currently on file
- Consideration of whether this candidate should be evaluated jointly with the related, better-evidenced "Thrombophilia" prediction (L2, 14 trials, 20 publications) rather than in isolation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

