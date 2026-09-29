---
layout: default
title: Misoprostol
parent: Model Prediction Only (L5)
nav_order: 326
evidence_level: L5
indication_count: 2
---

# Misoprostol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Misoprostol: From NSAID-Associated Gastric Ulcer Prevention to Amenorrhea

## One-Sentence Summary

Misoprostol is a prostaglandin E1 analogue, marketed in South Africa as a component of the diclofenac/misoprostol tablets Arthrotec and Arthrotec 50.
The TxGNN model predicts it may be useful for **amenorrhea** (score 99.64%), but there are **0 registered clinical trials** and **no publication that tests it as a treatment for amenorrhea**.
The retrieved papers concern medical abortion, where amenorrhea only describes gestational timing, so the prediction currently rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA data supplied. Misoprostol's known use is gastric ulcer prevention in patients taking NSAIDs, which is the purpose of the Arthrotec combination. |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L5 (the input pack assigned L4, but no mechanistic or preclinical studies were supplied, so L5 fits the stated rules) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

It is not clearly reasonable on current evidence. Detailed mechanism of action data are not available in the pack. Misoprostol is known to be a prostaglandin E1 analogue that causes uterine contraction and cervical ripening.

Those effects fit obstetric uses such as pregnancy termination and management of missed abortion. They do not plausibly restore menstrual function in primary or secondary amenorrhea. The high score is probably driven by knowledge-graph proximity in reproductive-tract terms rather than a therapeutic rationale.

The literature that mentions amenorrhea uses it as a gestational marker (for example, "amenorrhea ≤35 days" in early pregnancy) or as a presenting symptom in a case report. It does not describe treatment of amenorrhea.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of these papers evaluates misoprostol as a treatment for amenorrhea. They are listed for transparency, and their relevance to the predicted indication is indirect or absent.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | RCT | Reproductive Sciences | 744 women with ultra-early pregnancy (amenorrhea ≤35 days) randomised to hospital or self-administered misoprostol after low-dose mifepristone. This is medical abortion, not amenorrhea treatment. |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | RCT | Reproductive Sciences | Dose-ranging trial of 2,500 women, comparing mifepristone 150 to 50 mg followed by misoprostol 200 µg for ultra-early pregnancy termination. |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Clinical study | J Obstet Gynaecol Res | Safety and efficacy of low-dose mifepristone with self-administered misoprostol for early pregnancy termination. |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Clinical study | Human Reproduction | Feasibility of low-dose mifepristone plus misoprostol before expected menstruation to prevent unintended pregnancy. This is pregnancy prevention, not amenorrhea treatment. |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Case series/Review | BMJ | Medical management of missed abortion and anembryonic pregnancy. Indirect relevance. |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Review | J Obstet Gynaecol Can | Endometrial ablation for abnormal uterine bleeding. Indirect relevance. |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Case report | Cureus | Acute fatty liver of pregnancy presenting with amenorrhea. Not relevant to the predicted indication. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 32/3.1/0353 | Arthrotec | Tablet | Not provided in the registration data supplied |
| Reg. No. 28/3.1/0440 | Arthrotec 50 | Tablet | Not provided in the registration data supplied |

Both registrations are oral tablets. Essential Medicines List (EML) status could not be confirmed from the data supplied.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No drug interaction records were found in the pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but no trial or publication tests misoprostol for amenorrhea. The mechanism (uterine contraction) does not plausibly address menstrual absence. Amenorrhea patients may be pregnant, and a uterotonic drug in that setting is a safety concern. A second predicted indication, atypical coarctation of aorta (score 99.30%), has no evidence at all and needs no follow-up.

**To proceed, the following is needed:**
- Retrieval of the SAHPRA Professional Information (warnings and contraindications), which is a blocking gap for safety screening
- Mechanism of action data (for example, from DrugBank) to test whether any credible link to menstrual function exists
- Evidence that misoprostol treats amenorrhea itself, such as trials or mechanistic studies, rather than pregnancy-termination literature
- Confirmation of the approved indications on the two Arthrotec registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

