---
layout: default
title: Etonogestrel
parent: Model Prediction Only (L5)
nav_order: 220
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Etonogestrel: predicted new indication Amenorrhea (evidence level L5). Approved use: Contraception"
---

# Etonogestrel
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Etonogestrel: From Contraception to Amenorrhea

## One-Sentence Summary

Etonogestrel is a progestin used in hormonal contraception, marketed in South Africa as a vaginal ring (Nuvaring).
The TxGNN model predicts it may be effective for **amenorrhea**, but there are currently **0 clinical trials** and **no relevant publications** supporting this direction (the only linked paper is unrelated to this drug or condition).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Contraception (the registration record has no indication text; this is based on the drug's known use) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, etonogestrel is a progestin, a class that can suppress the endometrium and ovulation, so a theoretical hormonal rationale exists for menstrual-pattern disorders.

However, amenorrhea is a well-known **side effect** of etonogestrel-containing contraceptives (a change in bleeding pattern), not a therapeutic use. The prediction is therefore likely to reflect a graph association with a drug effect rather than a true treatment opportunity. Using a drug to treat a condition it is known to cause is not a reasonable repurposing direction without specific supporting evidence.

Other predictions were also reviewed. Most were benign breast conditions (fibrocystic disease, adenosis, benign mammary dysplasia, fat necrosis, breast abscess), and all are supported by model prediction only. Two predictions point toward harm or irrelevance: acne is a reported adverse event of etonogestrel implants, and breast abscess is an infection with no plausible hormonal treatment mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | RCT protocol | Trials | Study protocol for BIO101 in preventing respiratory deterioration in COVID-19 pneumonia. **Unrelated** to etonogestrel or amenorrhea. |

No relevant literature supports etonogestrel for amenorrhea.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 38/34/0171 | Nuvaring | Vaginal ring (recorded as "Vri") | Not recorded in the data compiled for this report |

The Essential Medicines List (EML) inclusion status is not available in the data compiled for this report.

## Safety Considerations

**Contraindication signals from the knowledge graph (not label text):** The TxGNN knowledge graph links etonogestrel to the following conditions, which should be verified against the approved Professional Information (PI):
- Cardiovascular and metabolic: hypertension, coronary artery disease, thrombophlebitis, diabetes mellitus, diabetic ketoacidosis, hypertriglyceridemia, hyperlipidemia (including familial), obesity
- Hepatic, renal and biliary: liver disease, gallbladder disease, kidney disease
- Neurological and psychiatric: epilepsy, migraine, anxiety disorder, neurotic disorder, dysthymic disorder
- Other: female breast carcinoma, systemic lupus erythematosus, asthma, porphyria

**Drug Interactions:** 100 interactions were identified in the DDInter database; the 20 reviewed were all rated Moderate. The main groups were:
- Antidiabetic agents (metformin, acarbose, glimepiride, chlorpropamide, SGLT2 inhibitors such as canagliflozin, dapagliflozin and empagliflozin, DPP-4 inhibitors such as alogliptin and saxagliptin, and GLP-1 agonists such as albiglutide, dulaglutide and semaglutide), and insulins (aspart, degludec, detemir, glargine, glulisine), where glycaemic control may be affected
- Others: aprepitant, clarithromycin, linaclotide

**Adverse events relevant to the predictions:** Acne is a reported adverse event with etonogestrel implants, and amenorrhea is a known bleeding-pattern change.

Please refer to the SAHPRA-approved Professional Information (PI) for formal warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Amenorrhea is a known effect of etonogestrel rather than a treatable indication. There are no clinical trials and no relevant literature, so the prediction rests on the model score alone (L5). The other predicted indications are also unsupported by clinical evidence.

**To proceed, the following is needed:**
- Review of the SAHPRA package insert for warnings, contraindications and approved indication text
- Mechanism of action data (e.g. from DrugBank)
- Clarification of whether the prediction reflects a therapeutic opportunity or only a drug effect
- Clinical or literature evidence directly linking etonogestrel to the proposed indication
- Confirmation of the EML status of etonogestrel products in South Africa
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

