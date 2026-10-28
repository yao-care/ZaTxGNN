---
layout: default
title: Misoprostol
parent: Model Prediction Only (L5)
nav_order: 328
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Misoprostol: predicted new indication Amenorrhea (evidence level L5). Approved use: Not available"
monitor_inn: "MISOPROSTOL"
predicted_indications: ["amenorrhea (disease)", "atypical coarctation of aorta"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Misoprostol: From Its Registered Use (Indication Text Not Available) to Amenorrhea
{: .text-alpha }

## One-Sentence Summary

Misoprostol is a prostaglandin E1 analogue, registered in South Africa in combination tablets (Arthrotec and Arthrotec 50). The registered indication text is not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **amenorrhea**, but there are **no registered clinical trials** and only **7 publications** retrieved. These concern pregnancy termination and uterine bleeding rather than treatment of amenorrhea itself, so the prediction is supported by **model output only**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the SAHPRA registration entries contain no indication text) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 0.9964 |
| Evidence Level | L5 (no clinical trials; the retrieved literature is indirect, so the data provide no direct evidence for amenorrhea) |
| South Africa Market Status | Marketed (valid licences: 2 of 2) |
| Number of SAHPRA Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacological knowledge, misoprostol is a prostaglandin E1 analogue that causes uterine contraction and cervical ripening.

The retrieved literature concerns medical abortion, missed abortion and abnormal uterine bleeding. Amenorrhea appears in these papers mainly as clinical context (for example, "amenorrhea ≤35 days" describing early pregnancy), not as a condition being treated. The link between misoprostol and amenorrhea is therefore **indirect**.

A plausible but unproven idea is that misoprostol might induce uterine evacuation or withdrawal bleeding in selected pregnancy-related amenorrhea. That is a different clinical goal from treating amenorrhea as a disorder. The very high TxGNN score is a computational prediction only and should not be read as clinical support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of these papers tests misoprostol as a treatment for amenorrhea. They are listed for context only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | RCT | Reprod Sci | 744 women with ultra-early pregnancy (amenorrhea ≤35 days) received low-dose mifepristone with hospital-administered vs self-administered misoprostol for medical abortion |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | RCT (dose-ranging) | Reprod Sci | 2,500 women with ultra-early pregnancy received mifepristone 50–150 mg followed by oral misoprostol 200 µg; primary endpoint was complete abortion without surgery |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Cohort | Hum Reprod | Low-dose mifepristone plus misoprostol before expected menstruation, studied for preventing unintended pregnancy |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Cohort | J Obstet Gynaecol Res | Safety and efficacy of low-dose mifepristone with self-administered misoprostol for early pregnancy termination |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Review | BMJ | Medical management of missed abortion and anembryonic pregnancy |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Review | J Obstet Gynaecol Can | Endometrial ablation in the management of abnormal uterine bleeding |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Case report | Cureus | Acute fatty liver of pregnancy in a woman presenting with amenorrhea; not a misoprostol treatment study |

## South Africa Market Information

Both registrations are valid single-ingredient entries. The data compiled for this report do not include indication text, manufacturer details or Essential Medicines List (EML) status.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 32/3.1/0353 | Arthrotec | Tablet (oral) | Not available |
| Reg. No. 28/3.1/0440 | Arthrotec 50 | Tablet (oral) | Not available |

## Safety Considerations

**Contraindications suggested by the knowledge graph.** These come from the TxGNN knowledge graph (drug–disease contraindication links), not from the label text, so they must be checked against the SAHPRA Professional Information (PI). Listed conditions include:
- Cardiovascular: hypertension, congestive heart failure, myocardial infarction, stroke and cerebrovascular disorders, coronary thrombosis, heart disease
- Hepatic: liver failure, liver disease, drug-induced liver injury, gallbladder disease
- Gastrointestinal: inflammatory bowel disease, active peptic ulcer disease
- Respiratory: asthma (including intrinsic and allergic asthma)
- Haematological: blood coagulation disease, hemoglobinopathy, anaemia (including macrocytic anaemia)
- Other: substance abuse/dependence, non-infectious meningitis

**Drug interactions.** 100 interactions were found in the DDInter database. The main ones among those retrieved:
- **Major:** dinoprostone (topical)
- **Moderate:** magnesium-containing antacids (magnesium oxide, magnesium carbonate, magnesium hydroxide, magaldrate) and quinapril
- **Minor:** sodium citrate, aluminium hydroxide, calcium carbonate, sodium bicarbonate and naproxen

**Pregnancy.** Misoprostol has uterotonic activity and is contraindicated in pregnancy. First-trimester exposure has been associated with congenital anomalies. This matters for any use in women of reproductive age with amenorrhea, since pregnancy is a common cause and must be excluded first.

The SAHPRA package insert warnings and contraindications were not available for this report. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 0.9964 TxGNN score has no direct clinical support. There are no registered trials, and the retrieved literature concerns pregnancy termination rather than treating amenorrhea. The safety profile, especially pregnancy-related risks, also works against this use. Because the SAHPRA label warnings could not be reviewed, safety screening cannot proceed.

**To proceed, the following is needed:**
- Download and review the SAHPRA package inserts for Arthrotec and Arthrotec 50 (warnings, contraindications and approved indications)
- Mechanism of action data from DrugBank
- A defined clinical rationale: which type of amenorrhea, and what treatment goal (for example, withdrawal bleeding vs uterine evacuation)
- Controlled clinical evidence for the amenorrhea indication
- A pregnancy-exclusion and contraception strategy for women of reproductive age
- Clarification of whether the registered Arthrotec products (which contain a second active ingredient) are appropriate for any investigation, or whether a single-ingredient misoprostol product would be needed

*Note on the second prediction (atypical coarctation of aorta, score 0.9930):* there is no clinical or literature evidence (L5), and the safety signal runs in the opposite direction. The decision for this prediction is also **Hold**.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

