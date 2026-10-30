---
layout: default
title: Medroxyprogesterone Acetate
parent: Model Prediction Only (L5)
nav_order: 311
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-30
monitor_inn: "Medroxyprogesterone acetate"
predicted_indications: ["amenorrhea (disease)", "breast fibrocystic disease", "benign mammary dysplasia", "renal hypoplasia, bilateral", "renal hypoplasia (disease)", "blunt duct adenosis of breast", "apocrine adenosis of breast"]
description: "Medroxyprogesterone Acetate: predicted new indication Amenorrhea (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Medroxyprogesterone Acetate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Medroxyprogesterone Acetate: Amenorrhea (disease)
{: .text-alpha }

## One-Sentence Summary

Medroxyprogesterone acetate (MPA) is a synthetic progestin, originally used for endometriosis, endometrial cancer and postmenopausal conditions such as osteoporosis and atrophic vaginitis.
The TxGNN model predicts it may be relevant for **amenorrhea**, but **no clinical trials** are registered and the **20 publications** retrieved are mostly older reviews of contraception, so support is limited.
The literature largely describes amenorrhea as a *side effect* of MPA rather than a treatment target, so this prediction may reflect an association rather than a true therapeutic indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 (no trials; mechanistic and review literature only) |
| South Africa Market Status | Marketed (valid licences: 2 of 4) |
| Number of SAHPRA Registrations | 4 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, MPA is a synthetic progestin. Its effects include suppression of the hypothalamic-pituitary-ovarian axis and atrophy of the endometrium, which are why amenorrhea is a well-known effect of depot formulations such as Depo-Provera.

The link to the original indications is hormonal. MPA acts on endometrial tissue in endometriosis and endometrial disease. A progestin challenge is also used in the diagnostic work-up of secondary amenorrhea.

There is an important caveat about direction. In the retrieved literature, MPA is mostly described as a *cause* of amenorrhea (a contraceptive side effect), not as a treatment for it. The high TxGNN score therefore likely reflects a network association. It should not be read as evidence that MPA treats amenorrhea.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Of the 20 publications retrieved, none is an RCT. The most relevant are listed below. All are reviews or overviews, mostly on contraception, and most are older.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23641480](https://pubmed.ncbi.nlm.nih.gov/23641480/) | 2013 | Systematic review | Cochrane Database Syst Rev | Combination injectable contraceptives are highly effective; bleeding pattern changes may limit acceptability |
| [18843662](https://pubmed.ncbi.nlm.nih.gov/18843662/) | 2008 | Systematic review | Cochrane Database Syst Rev | Earlier version of the review above |
| [8178904](https://pubmed.ncbi.nlm.nih.gov/8178904/) | 1994 | Review | Am J Obstet Gynecol | Depot MPA 150 mg IM every 3 months has contraceptive efficacy above 99% |
| [8725701](https://pubmed.ncbi.nlm.nih.gov/8725701/) | 1996 | Review | J Reprod Med | Counselling and management of side effects with depot MPA |
| [8829701](https://pubmed.ncbi.nlm.nih.gov/8829701/) | 1996 | Review | Int J Fertil Menopausal Stud | Long-acting contraceptive options, including injectables |
| [6119259](https://pubmed.ncbi.nlm.nih.gov/6119259/) | 1981 | Review | Int J Gynaecol Obstet | Postpartum contraception and its relation to postpartum amenorrhea |
| [6141923](https://pubmed.ncbi.nlm.nih.gov/6141923/) | 1984 | Review | Drug Intell Clin Pharm | Drug-induced infertility |
| [120837](https://pubmed.ncbi.nlm.nih.gov/120837/) | 1979 | Review | IARC Monogr | General monograph on MPA carcinogenic risk |
| [8492647](https://pubmed.ncbi.nlm.nih.gov/8492647/) | 1993 | Review | MCN Am J Matern Child Nurs | Overview of Depo-Provera |
| [7139435](https://pubmed.ncbi.nlm.nih.gov/7139435/) | 1982 | Commentary | Can Med Assoc J | Whether depot MPA should be considered for additional uses |

## South Africa Market Information

Four valid single-ingredient registrations are on record. Manufacturer and approved indication text are not available in the data compiled for this report. Essential Medicines List (EML) status is not available either.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 52/21.8.2/0991 | Mytricon | Injection | Not available |
| E/21.8.2/114 | Depo-provera 1ml | Injection | Not available |
| 32/21.8/0631 | Premelle Cycle-5 | Tablet | Not available |
| 36/21.8/0197 | Premelle Ld-0.3/1.5 | Tablet | Not available |

## Safety Considerations

Safety information from the product label is not available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

**Contraindication signals from the knowledge graph** (not label text, and requiring confirmation against the PI): hypertension, liver failure or liver disease, kidney disease, gallbladder disease, epilepsy, asthma, diabetes mellitus and diabetic ketoacidosis, hypothyroidism, systemic lupus erythematosus, osteoporosis, hypercalcaemia and related conditions, hypertriglyceridaemia, anxiety and neurotic disorders, substance abuse or dependence, and female breast carcinoma.

**Drug interactions:** The interaction screen returned 100 interactions, all rated Moderate in the 20 shown. Most involve glucose-lowering agents, which fits the diabetes signal above:
- Antidiabetic drugs: acarbose, alogliptin, saxagliptin, metformin, glimepiride, chlorpropamide, canagliflozin, dapagliflozin, empagliflozin
- GLP-1 agonists and insulins: albiglutide, dulaglutide, liraglutide, semaglutide, insulin aspart, degludec and detemir
- Others: aprepitant, dexamethasone, clarithromycin, pegvaliase

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No clinical trials are registered, and the literature is mostly old contraception reviews that describe amenorrhea as an effect of MPA rather than a treatment target. The prediction is probably an association artefact, so there is no basis to advance it as a repurposing candidate.

**To proceed, the following is needed:**
- Clarify the clinical intent (for example, treatment of secondary amenorrhea or abnormal bleeding versus the contraceptive side effect), and search for controlled studies in that setting
- Download and review the SAHPRA Professional Information, including indications, warnings and contraindications
- Obtain mechanism of action data from DrugBank
- Review the knowledge graph contraindication signals, especially breast carcinoma, liver disease, diabetes and hypertension, against the PI

## Other Predicted Indications (Context)

The model made nine further predictions. None has registered clinical trials.

| Predicted Indication | Evidence Level | Assessment |
|------|------|------|
| Breast fibrocystic disease | L3 | Two small, dated MPA reports (1983, 1988); HRT literature suggests progestins may worsen breast findings. This is the most developed of the other predictions, but it carries a safety concern. |
| Benign mammary dysplasia | L5 | Indirect and largely non-human evidence. |
| Cervix endometriosis | L4 | Plausible extension of the approved endometriosis indication, but no direct evidence. |
| Endometriosis of rectovaginal septum and vagina | L5 | Prediction only; likely an extension of the existing indication. |
| Endometriosis in cutaneous scar | L5 | Prediction only; surgery is the standard treatment. |
| Blunt duct adenosis and apocrine adenosis of breast | L5 | Prediction only; progestin effects on breast epithelium are mixed. |
| Renal hypoplasia (bilateral and unspecified) | L5 | No plausible mechanism; likely a network artefact. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

