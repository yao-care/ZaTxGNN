---
layout: default
title: Docetaxel
parent: High Evidence (L1-L2)
nav_order: 190
evidence_level: L1
indication_count: 10
---

# Docetaxel
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Docetaxel: From Registered Cytotoxic Chemotherapy to Female Breast Carcinoma

## One-Sentence Summary

Docetaxel is a taxane chemotherapy drug. The registration record supplied does not state its approved indication.
The TxGNN model predicts it may be effective for **female breast carcinoma**, supported by **more than 40 registered clinical trials** (including several large completed Phase 3 trials) and **20 publications**.
Breast cancer is very likely already a labelled use of docetaxel, so this may be confirmation of an established use rather than true repurposing. This should be checked against the SAHPRA Professional Information (PI).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA record supplied |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the database record. Docetaxel is a microtubule-stabilising taxane. It prevents the mitotic spindle from disassembling and causes G2/M cell-cycle arrest in rapidly dividing tumour cells. This mechanism fits the high TxGNN score of 0.999.

Breast tumours are highly proliferative, so an anti-mitotic agent is a sensible fit. The trial evidence supports this. Docetaxel appears as a named component in adjuvant, neoadjuvant and metastatic breast cancer regimens, including combinations with anthracyclines, cyclophosphamide, carboplatin, capecitabine, gemcitabine and HER2-targeted antibodies.

The original indication field is empty in the data supplied. If breast cancer is already on the registered label, this prediction is a confirmation of use and not a new indication. The label should be checked before this candidate is classed as repurposing.

---

## Clinical Trial Evidence

No SANCTR or PACTR identifiers were found in the data supplied. TARMAC is the only African trial listed (Nigeria).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003782](https://clinicaltrials.gov/study/NCT00003782) | Phase 3 | Completed | 5351 | Compares adjuvant AC followed by docetaxel, AT, and ATC in node-positive breast cancer |
| [NCT00002707](https://clinicaltrials.gov/study/NCT00002707) | Phase 3 | Completed | 2411 | Preoperative AC versus AC followed by docetaxel (before or after surgery) in operable breast cancer |
| [NCT00054587](https://clinicaltrials.gov/study/NCT00054587) | Phase 3 | Completed | 3010 | Docetaxel plus epirubicin versus FEC100 in node-positive breast cancer, with sequential trastuzumab in HER2-positive disease |
| [NCT00593697](https://clinicaltrials.gov/study/NCT00593697) | Phase 3 | Completed | 2168 | Trastuzumab plus docetaxel followed by FEC, with or without further trastuzumab, in early HER2-positive breast cancer |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3270 | Adjuvant chemotherapy (docetaxel-cyclophosphamide or AC followed by paclitaxel) with or without trastuzumab in HER2-low breast cancer |
| [NCT01547741](https://clinicaltrials.gov/study/NCT01547741) | Phase 3 | Unknown | 1871 | Docetaxel plus cyclophosphamide versus anthracycline-based regimens in HER2-negative, node-positive or high-risk breast cancer |
| [NCT00193011](https://clinicaltrials.gov/study/NCT00193011) | Phase 3 | Completed | 150 | Weekly docetaxel versus CMF in high-risk breast cancer patients over 65 or unsuitable for anthracyclines |
| [NCT00217672](https://clinicaltrials.gov/study/NCT00217672) | Phase 2 | Completed | 76 | Docetaxel with or without bevacizumab as first-line therapy for HER2-negative metastatic breast cancer |
| [NCT03639948](https://clinicaltrials.gov/study/NCT03639948) | Phase 2 | Active, not recruiting | 120 | Neoadjuvant pembrolizumab plus carboplatin plus docetaxel in triple-negative breast cancer |
| [NCT06291064](https://clinicaltrials.gov/study/NCT06291064) | Phase 2 | Recruiting | 85 | Epirubicin-cyclophosphamide followed by docetaxel-carboplatin in Nigerian women with triple-negative breast cancer, with biomarker analysis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | RCT | J Clin Oncol | ABC trials: docetaxel-cyclophosphamide (TC) compared with standard taxane-anthracycline regimens in early breast cancer |
| [11481357](https://pubmed.ncbi.nlm.nih.gov/11481357/) | 2001 | RCT (Phase IIb) | J Clin Oncol | Preoperative dose-dense doxorubicin and docetaxel, with or without tamoxifen, in operable breast cancer |
| [26874836](https://pubmed.ncbi.nlm.nih.gov/26874836/) | 2017 | Phase 2 | Breast Cancer | Docetaxel, cyclophosphamide and trastuzumab as neoadjuvant therapy in HER2-positive breast cancer |
| [15585076](https://pubmed.ncbi.nlm.nih.gov/15585076/) | 2004 | Phase 2 | Clin Breast Cancer | Docetaxel-cisplatin as primary chemotherapy in locally advanced breast cancer, with pathological complete response as the endpoint |
| [16020974](https://pubmed.ncbi.nlm.nih.gov/16020974/) | 2005 | Phase 2 | Oncology | Weekly docetaxel and gemcitabine as first-line therapy for metastatic breast cancer |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Phase 2 | Cancer | Capecitabine with docetaxel and epirubicin in untreated advanced breast cancer |
| [15074734](https://pubmed.ncbi.nlm.nih.gov/15074734/) | 2004 | Case series | Clin Oncol | Trastuzumab plus docetaxel in HER2-overexpressing metastatic breast cancer, an experience from India |
| [7595719](https://pubmed.ncbi.nlm.nih.gov/7595719/) | 1995 | Review | J Clin Oncol | Early review of the preclinical and clinical profile of docetaxel |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug Ther Bull | Review of paclitaxel and docetaxel in breast and ovarian cancer |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Cohort | Anti-Cancer Drugs | Retrospective study of adjuvant docetaxel-based chemotherapy and breast cancer-related lymphedema, a fluid-retention safety question |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| A39/26/0551 | Docetere 80Mg | Infusion | Not stated in the record supplied |

The EML status is not included in the data supplied.

---

## Cytotoxicity

Docetaxel is an antineoplastic drug. No DrugBank toxicity data were supplied, so the entries below are based on drug class. Please refer to the Professional Information (PI) warnings and precautions.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (taxane, microtubule stabiliser) |
| Myelosuppression Risk | High (neutropenia is the main concern) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | FBC with differential, liver function (dose adjustment may be needed in hepatic impairment), renal function; watch for hypersensitivity, fluid retention and peripheral neuropathy |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The retrieved literature notes that docetaxel-based chemotherapy can cause fluid retention and peripheral oedema. A retrospective study (PMID 27997437) examined its link with breast cancer-related lymphedema.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several large, completed Phase 3 trials (up to 5,351 participants) include docetaxel in breast cancer regimens. The mechanism is plausible, so the evidence for breast cancer is strong (L1). The local record has no approved-indication text or safety data, and breast cancer may already be a labelled use. These gaps are why the decision carries guardrails.

**To proceed, the following is needed:**
- The SAHPRA package insert (PI) for Docetere 80Mg, to confirm the approved indications and to obtain warnings, contraindications and interactions. This is a blocking gap.
- Confirmation of whether breast cancer is already on the registered label, to decide whether this is true repurposing.
- Verified mechanism of action data from DrugBank.
- Confirmation of the docetaxel-specific contribution in trials where it is one component of a combination regimen.

**Other predictions in this pack:**
- Ewing sarcoma and rhabdomyosarcoma have small Phase 2 evidence, mostly gemcitabine-docetaxel combinations. These are research questions only.
- The lung and lymphoma predictions appear to reflect NSCLC trials in which docetaxel was the comparator, not evidence in the predicted diseases. These are on hold.
- The remaining rare sarcoma predictions have no retrieved trials or literature and are on hold.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

